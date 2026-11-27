"""Testy serwera przez klienta MCP w tym samym procesie: tak, jak widzi go aplikacja."""
import asyncio
import json

import pytest
from mcp import Client

from fikus.server import mcp


def _run(coro_fn):
    async def go():
        async with Client(mcp) as client:
            return await coro_fn(client)
    return asyncio.run(go())


def _call(name, args=None):
    return _run(lambda c: c.call_tool(name, args or {}))


def test_every_tool_is_read_only_and_has_output_schema():
    tools = _run(lambda c: c.list_tools()).tools
    assert {t.name for t in tools} == {"get_parameter", "list_parameters", "list_profiles",
                                       "deadlines", "get_schema", "changes"}
    for t in tools:
        assert t.title and t.description
        assert t.annotations.read_only_hint and t.annotations.open_world_hint is False
        assert t.output_schema, t.name
        for name, prop in t.input_schema.get("properties", {}).items():
            assert prop.get("description"), f"{t.name}.{name} bez opisu"


def test_result_has_structured_content_and_matching_text():
    r = _call("get_parameter", {"id": "zdrowotna.minimum", "as_of": "2026-03-15"})
    assert not r.is_error
    assert r.structured_content["value"] == 432.54
    assert json.loads(r.content[0].text)["value"] == 432.54


@pytest.mark.parametrize("name,args,expected", [
    ("get_parameter", {"id": "nie.ma"}, "Nieznany parametr"),
    ("get_parameter", {"id": "zdrowotna.minimum", "as_of": "2026-13-01"}, "as_of"),
    ("list_parameters", {"profile": "nie_ma"}, "Nieznany profil"),
    ("deadlines", {"profile": "przyklad_ryczalt", "year": 2026, "month": 13}, "month"),
    ("changes", {"since": "wczoraj"}, "since"),
])
def test_bad_arguments_are_tool_errors(name, args, expected):
    r = _call(name, args)
    assert r.is_error
    assert expected in r.content[0].text


def test_missing_version_is_a_result_not_an_error():
    r = _call("get_parameter", {"id": "zdrowotna.ryczalt.skladka", "as_of": "2027-01-01"})
    assert not r.is_error and r.structured_content["found"] is False


def test_deadlines_through_protocol():
    r = _call("deadlines", {"profile": "przyklad_liniowy", "year": 2026, "month": 12})
    assert not r.is_error
    assert r.structured_content["non_working_days"] == ["2026-12-24", "2026-12-25", "2026-12-26"]


def test_get_schema_follows_settlement_period():
    r = _call("get_schema", {"form": "JPK_V7M", "as_of": "2026-01-01"})
    assert not r.is_error and r.structured_content["value"]["system_code"] == "JPK_V7M (2)"
    r = _call("get_schema", {"form": "JPK_V7M", "as_of": "2026-02-01"})
    assert r.structured_content["value"]["system_code"] == "JPK_V7M (3)"
    r = _call("get_schema", {"form": "VAT-7", "as_of": "2026-02-01"})
    assert not r.is_error and r.structured_content["found"] is False


def test_get_schema_jpk_ewp():
    r = _call("get_schema", {"form": "JPK_EWP", "as_of": "2026-01-01"})
    assert not r.is_error and r.structured_content["found"] is True
    value = r.structured_content["value"]
    assert value["variant"] == 4 and value["system_code"] == "JPK_EWP (4)"
    tools = {t.name: t for t in _run(lambda c: c.list_tools()).tools}
    assert "JPK_EWP" in tools["get_schema"].description


def test_deadlines_list_revenue_record_entry_for_flat_rate_only():
    ids = {d["id"] for d in _call("deadlines", {"profile": "przyklad_ryczalt", "year": 2026, "month": 11})
           .structured_content["deadlines"]}
    assert {"termin.ewidencja_przychodow_wpis", "termin.zaliczka_ryczalt"} <= ids
    ids = {d["id"] for d in _call("deadlines", {"profile": "przyklad_liniowy", "year": 2026, "month": 11})
           .structured_content["deadlines"]}
    assert "termin.ewidencja_przychodow_wpis" not in ids


def test_get_schema_zus_dra_by_filing_date():
    r = _call("get_schema", {"form": "ZUS_DRA", "as_of": "2026-05-01"})
    assert not r.is_error and r.structured_content["value"]["legal_act"] == "Dz.U. 2026 poz. 518"
    r = _call("get_schema", {"form": "ZUS_DRA", "as_of": "2026-04-30"})
    assert r.structured_content["found"] is False


def test_confidence_reports_medium_level_scope_and_unconfirmed_fields():
    rule = _call("get_parameter", {"id": "zasada.ulgi_liniowy", "as_of": "2027-02-01"})
    conf = rule.structured_content["confidence"]
    assert conf["level"] == "średnia" and conf["open_issue_scope"] == "edge_case"
    schema = _call("get_parameter", {"id": "schemat.jpk_v7m", "as_of": "2026-11-26"})
    assert "system_code" in schema.structured_content["confidence"]["unconfirmed_fields"]
    levels = {c["confidence"] for c in _call("changes", {"since": "2026-01-01"}).structured_content["result"]}
    assert levels <= {"wysoka", "średnia", "niska"} and "średnia" in levels


def test_get_schema_accepts_hyphen_and_lowercase():
    for form in ("PIT-36L", "pit_36l", "PIT_36L", "pit-36l"):
        r = _call("get_schema", {"form": form, "as_of": "2026-01-01"})
        assert not r.is_error and r.structured_content["id"] == "schemat.pit_36l"
        assert r.structured_content["found"] is True
    r = _call("get_schema", {"form": "PIT-28", "as_of": "2025-01-01"})
    assert r.structured_content["found"] is True and r.structured_content["value"]["form"].startswith("PIT-28")

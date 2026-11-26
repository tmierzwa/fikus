"""Testy wykrywania zmian na podstawionych odpowiedziach API ELI (bez sieci)."""
from datetime import date

import pytest

from fikus.model import Parameter
from fikus.store import Store
from fikus.zmiany import cited_acts, check_act, detect, eli_id, ending_versions, load_reviewed

TODAY = date(2026, 11, 26)


def _store(*params):
    s = Store()
    s.params = {p["id"]: Parameter.model_validate(p) for p in params}
    return s


def _param(pid, url, valid_from="2026-01-01", valid_to=None):
    return {"id": pid, "name": pid, "versions": [{
        "valid_from": valid_from, "valid_to": valid_to, "value": 1,
        "sources": [{"title": "akt", "url": url}],
        "verification": {"checked_at": "2026-01-01"}}]}


def _with_control(param, url):
    param["versions"][0]["sources"].append({"title": "portal", "url": url, "kind": "control"})
    return param


def _fake(acts):
    calls = []

    def fetch(act):
        calls.append(act)
        return acts[act]
    fetch.calls = calls
    return fetch


TJ_CURRENT = {"inForce": "IN_FORCE", "status": "obowiązujący", "references": {
    "Tekst jednolity dla aktu": [{"id": "DU/2004/2135"}],
    "Nowelizacje po tekście jednolitym": [{"id": "DU/2026/986", "date": "2026-06-11"},
                                          {"id": "DU/2025/1739", "date": "2025-11-21"}]}}
BASE = {"inForce": "IN_FORCE", "references": {
    "Inf. o tekście jednolitym": [{"id": "DU/2024/146"}, {"id": "DU/2025/1461"}]}}


def test_eli_id_from_both_url_shapes():
    assert eli_id("https://api.sejm.gov.pl/eli/acts/DU/2025/1461/text.pdf") == "DU/2025/1461"
    assert eli_id("https://eli.gov.pl/eli/MP/2026/117/ogl") == "MP/2026/117"
    assert eli_id("https://www.zus.pl/-/komunikat") is None


def test_only_primary_sources_of_current_or_future_versions_are_checked():
    s = _store(_param("a", "https://eli.gov.pl/eli/DU/2025/1/ogl"),
               _param("b", "https://eli.gov.pl/eli/DU/2024/2/ogl", "2024-01-01", "2024-12-31"),
               _with_control(_param("c", "https://www.zus.pl/-/komunikat"), "https://eli.gov.pl/eli/DU/2025/3/ogl"),
               _param("d", "https://eli.gov.pl/eli/DU/2027/4/ogl", "2027-01-01"))
    assert cited_acts(s, TODAY) == {"DU/2025/1": {"a"}, "DU/2027/4": {"d"}}


def test_historical_consolidated_text_cited_for_valid_from_is_not_checked():
    p = _param("a", "https://api.sejm.gov.pl/eli/acts/DU/2026/592/text.pdf", "2020-01-01")
    p["versions"][0]["sources"].append({"title": "dawny tekst jednolity", "as_of": "2020-07-23",
                                        "url": "https://api.sejm.gov.pl/eli/acts/DU/2020/1426/text.pdf",
                                        "role": "historical"})
    assert cited_acts(_store(p), TODAY) == {"DU/2026/592": {"a"}}


def test_historical_source_needs_as_of_primary_kind_and_a_current_primary():
    from fikus.model import Source, Version
    url = "https://eli.gov.pl/eli/DU/2020/1426/ogl"
    with pytest.raises(ValueError, match="as_of"):
        Source(title="t", url=url, role="historical")
    with pytest.raises(ValueError, match="pierwotnego"):
        Source(title="t", url=url, role="historical", kind="control", as_of="2020-07-23")
    with pytest.raises(ValueError, match="role: current"):
        Version(valid_from="2020-01-01", value=1, verification={"checked_at": "2026-01-01"},
                sources=[{"title": "t", "url": url, "role": "historical", "as_of": "2020-07-23"}])


def test_amendments_after_current_consolidated_text_are_reported_except_reviewed():
    f = _fake({"DU/2025/1461": TJ_CURRENT, "DU/2004/2135": BASE})
    out = check_act("DU/2025/1461", {"p"}, f, reviewed={"DU/2025/1739"})
    assert [(x.kind, x.detail) for x in out] == [("nowelizacja", "DU/2026/986, wchodzi w życie 2026-06-11")]


def test_newer_consolidated_text_replaces_amendment_list():
    base = {"inForce": "IN_FORCE", "references": {"Inf. o tekście jednolitym": [{"id": "DU/2026/50"}]}}
    out = check_act("DU/2025/1461", {"p"}, _fake({"DU/2025/1461": TJ_CURRENT, "DU/2004/2135": base}), set())
    assert [(x.kind, x.detail) for x in out] == [("nowy_tekst", "nowszy tekst jednolity: DU/2026/50")]


def test_act_out_of_force_and_amended_regulation():
    act = {"inForce": "NOT_IN_FORCE", "status": "wygaśnięcie aktu",
           "references": {"Akty zmieniające": [{"id": "DU/2026/7", "date": "2026-03-01"}]}}
    kinds = [x.kind for x in check_act("DU/2025/9", {"p"}, _fake({"DU/2025/9": act}), set())]
    assert kinds == ["nie_obowiazuje", "nowelizacja"]


def test_citing_base_act_instead_of_consolidated_text_is_reported():
    out = check_act("DU/2004/2135", {"p"}, _fake({"DU/2004/2135": BASE}), set())
    assert [x.kind for x in out] == ["nowy_tekst"] and "DU/2025/1461" in out[0].detail


def test_versions_ending_without_successor():
    s = _store(_param("konczy", "https://eli.gov.pl/eli/DU/2025/1/ogl", valid_to="2026-12-31"),
               _param("daleko", "https://eli.gov.pl/eli/DU/2025/1/ogl", valid_to="2027-12-31"),
               _param("bez_konca", "https://eli.gov.pl/eli/DU/2025/1/ogl"))
    assert [f.params for f in ending_versions(s, TODAY, 60)] == [("konczy",)]


def test_network_error_is_a_finding_not_a_crash():
    def broken(act):
        raise OSError("timeout")
    out = detect(_store(_param("a", "https://eli.gov.pl/eli/DU/2025/1/ogl")), TODAY, fetch=broken)
    assert [(f.kind, f.act) for f in out] == [("blad", "DU/2025/1")]


def test_reviewed_file_requires_note(tmp_path):
    p = tmp_path / "z.yaml"
    p.write_text("- {act: DU/2026/1, checked_at: 2026-11-26}\n", encoding="utf-8")
    with pytest.raises(ValueError, match="note"):
        load_reviewed(p)


def test_repository_reviewed_file_is_valid():
    from fikus.store import DATA
    load_reviewed(DATA / "zmiany_sprawdzone.yaml")

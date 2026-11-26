from datetime import date

import pytest

from fikus.cytaty import cached_text, quote_in
from fikus.model import Parameter, Version
from fikus.store import Store

store = Store()


def test_all_data_loads():
    assert store.params and store.profiles


def test_query_as_of():
    r = store.get("zdrowotna.minimum", date(2026, 3, 15))
    assert r["found"] and r["value"] == 432.54
    assert "cytat" in r["confidence"]["evidence"]
    jan = store.get("zdrowotna.minimum", date(2026, 1, 15))   # ostatni miesiąc roku składkowego 2025/2026
    assert jan["found"] and jan["value"] == 314.96


def test_profile_filter():
    ids = {r["id"] for r in store.for_profile("przyklad_ryczalt", date(2026, 6, 1))}
    assert {"zdrowotna.ryczalt.skladka", "zasada.ryczalt_podstawa"} <= ids
    assert "zdrowotna.minimum" not in ids


def test_deadlines_are_rules_not_dates():
    r = store.deadlines("przyklad_liniowy", 2026, 12)
    days = {d["id"]: d["day_of_month"] for d in r["deadlines"]}
    assert days == {"termin.zus": 20, "termin.jpk_v7m": 25, "termin.zaliczka_liniowy": 20}
    assert r["non_working_days"] == ["2026-12-24", "2026-12-25", "2026-12-26"]
    assert r["shift_rule"]["found"]
    assert "due" not in str(r)  # serwer nie podaje wyliczonych dat


def test_annual_deadline_only_in_its_month():
    may = {d["id"] for d in store.deadlines("przyklad_ryczalt", 2026, 5)["deadlines"]}
    june = {d["id"] for d in store.deadlines("przyklad_ryczalt", 2026, 6)["deadlines"]}
    assert "termin.roczne_rozliczenie_zdrowotnej" in may and "termin.roczne_rozliczenie_zdrowotnej" not in june


def test_overlap_rejected():
    v = {"value": 1, "sources": [{"title": "x", "url": "https://example.org"}],
         "verification": {"checked_at": "2026-01-01"}}
    with pytest.raises(ValueError):
        Parameter.model_validate({"id": "t", "name": "t", "versions": [
            {**v, "valid_from": "2026-01-01", "valid_to": "2026-12-31"},
            {**v, "valid_from": "2026-06-01"}]})


def test_zus_spoleczne_2026_for_full_zus():
    d = date(2026, 6, 1)
    ids = {r["id"] for r in store.for_profile("przyklad_ryczalt", d)}
    assert {"zus.podstawa_minimalna", "zus.stawka.emerytalna", "zus.stawka.rentowa",
            "zus.stawka.chorobowa", "zus.stawka.wypadkowa_do_9",
            "zus.stawka.fundusz_pracy", "zus.stawka.fundusz_solidarnosciowy"} <= ids
    assert "zus.podstawa_minimalna" not in {r["id"] for r in store.for_profile("przyklad_liniowy", d)}
    assert store.get("zus.podstawa_minimalna", d)["value"] == 5652.00
    assert store.get("zus.stawka.wypadkowa_do_9", date(2026, 3, 31))["value"] == 1.67


def test_quarterly_vat_deadlines():
    ids = lambda m: {d["id"] for d in store.deadlines("przyklad_ryczalt", 2026, m)["deadlines"]}
    assert "termin.jpk_v7k_kwartal" in ids(10) and "termin.jpk_v7k_ewidencja" not in ids(10)
    assert "termin.jpk_v7k_ewidencja" in ids(11) and "termin.jpk_v7k_kwartal" not in ids(11)
    assert "termin.jpk_v7m" not in ids(11)
    assert not {"termin.jpk_v7k_kwartal", "termin.jpk_v7k_ewidencja"} & {
        d["id"] for d in store.deadlines("przyklad_liniowy", 2026, 10)["deadlines"]}


def test_ryczalt_health_follows_calendar_year():
    jan = store.get("zdrowotna.ryczalt.skladka", date(2026, 1, 1))
    assert jan["value"]["powyzej_300000"] == 1495.04
    assert store.get("zdrowotna.ryczalt.skladka", date(2025, 12, 31))["value"]["powyzej_300000"] == 1384.97
    assert not store.get("zdrowotna.ryczalt.skladka", date(2027, 1, 1))["found"]
    progi = store.get("zdrowotna.ryczalt.progi", date(2026, 1, 1))["value"]
    assert set(progi) == set(jan["value"]) - {"powyzej_300000"}
    ids = {r["id"] for r in store.for_profile("przyklad_ryczalt", date(2026, 1, 15))}
    assert {"zdrowotna.ryczalt.progi", "zasada.ryczalt_zdrowotna_prog_poprzedni_rok"} <= ids


def _version(**ver):
    return Version.model_validate({
        "valid_from": "2026-01-01", "value": 1,
        "sources": [{"title": "akt", "url": "https://example.org/1", "quote": "wynosi 1 %"},
                    {"title": "komunikat", "url": "https://example.org/2", "kind": "control"}],
        "verification": {"checked_at": "2026-01-01", **ver}})


def test_confidence_needs_quote_and_two_more_kinds_of_evidence():
    assert _version().confidence()["level"] == "niska"                     # cytat + drugie źródło
    assert _version(agent_check="2026-01-02").confidence()["level"] == "wysoka"
    assert _version(agent_check="2026-01-02", open_issue="sprzeczne źródła").confidence()["level"] == "niska"


def test_open_question_about_an_edge_case_gives_medium_confidence():
    edge = _version(agent_check="2026-01-02", open_issue="przypadek brzegowy", open_issue_scope="edge_case")
    assert edge.confidence()["level"] == "średnia"
    assert edge.confidence()["open_issue_scope"] == "edge_case"
    # Bez zakresu pytanie dotyczy wartości, a przy niepełnych dowodach zakres nie podnosi pewności.
    assert _version(agent_check="2026-01-02", open_issue="?").confidence()["open_issue_scope"] == "value"
    assert _version(open_issue="?", open_issue_scope="edge_case").confidence()["level"] == "niska"
    with pytest.raises(ValueError):
        _version(open_issue_scope="edge_case")


def _composite(*sources):
    return Version.model_validate({
        "valid_from": "2026-01-01", "value": {"variant": 3, "code": "X (3)"},
        "sources": list(sources), "verification": {"checked_at": "2026-01-01", "agent_check": "2026-01-02"}})


def test_composite_value_can_be_confirmed_field_by_field():
    a = {"title": "broszura", "url": "https://example.org/a", "quote": "q", "confirms": ["variant", "code", "period"]}
    b = {"title": "strona", "url": "https://example.org/b", "quote": "q", "confirms": ["variant", "period"]}
    c = {"title": "rejestr", "url": "https://example.org/c", "quote": "q", "confirms": ["code"]}
    assert _composite(a, b, c).confidence()["level"] == "wysoka"
    assert _composite(a, b).confidence()["level"] == "niska"          # kod podaje tylko jeden dokument
    assert _composite(a, b).confidence()["unconfirmed_fields"] == ["code"]
    assert "unconfirmed_fields" not in _version().confidence()
    same_doc = {**c, "url": a["url"]}
    assert _composite(a, b, same_doc).confidence()["level"] == "niska"  # jeden dokument liczy się raz
    with pytest.raises(ValueError):
        _composite(a, {**b, "confirms": ["wersja"]})                    # nieznane pole
    with pytest.raises(ValueError):
        _composite(a, {**b, "confirms": []})                            # pusta lista
    with pytest.raises(ValueError):
        _composite(a, {k: v for k, v in b.items() if k != "quote"})     # confirms bez cytatu
    # Źródło kontrolne bez confirms nie zastępuje potwierdzania pól, gdy wersja go używa.
    control = {"title": "portal", "url": "https://example.org/d", "kind": "control"}
    assert _composite(a, b, control).confidence()["level"] == "niska"
    with pytest.raises(ValueError):
        Version.model_validate({"valid_from": "2026-01-01", "value": {"period": 1}, "sources": [a],
                                "verification": {"checked_at": "2026-01-01"}})


def test_quote_matching_ignores_layout_but_not_content():
    text = "Składka wynosi\n9 % podstawy wy-\nmiaru – na „ubezpieczenie”"
    assert quote_in('składka wynosi 9 % podstawy wymiaru - na "ubezpieczenie"', text)
    assert not quote_in("Składka wynosi 8 % podstawy", text)
    assert quote_in("Schemat_JPK_PKPIR(3)_v1-0", "Schemat\u200b_JPK\u200b_PKPIR(3)\u200b_v1-0")


def test_quotes_match_cached_official_texts():
    checked = 0
    for p in store.params.values():
        for v in p.versions:
            for s in v.sources:
                text = s.quote and cached_text(s.url)
                if text:
                    assert quote_in(s.quote, text), f"{p.id} {v.valid_from}: cytatu nie ma w {s.url}"
                    checked += 1
    if not checked:
        pytest.skip("brak tekstów źródeł w .cache/zrodla (uruchom scripts/sprawdz_cytaty.py)")


def test_unknown_profile_and_bad_month_return_reasons():
    assert store.for_profile("nie_ma", date(2026, 6, 1))[0]["known"] == sorted(store.profiles)
    assert store.deadlines("nie_ma", 2026, 6)["found"] is False
    assert store.deadlines("przyklad_ryczalt", 2026, 13)["found"] is False


def test_source_url_must_be_https():
    with pytest.raises(ValueError):
        _version().model_validate({"valid_from": "2026-01-01", "value": 1,
                                   "sources": [{"title": "x", "url": "file:///etc/passwd"}],
                                   "verification": {"checked_at": "2026-01-01"}})


def test_deadline_version_starting_mid_month_is_listed():
    src = [{"title": "akt", "url": "https://example.org/a"}]
    ver = {"checked_at": "2026-01-01"}
    p = Parameter.model_validate({"id": "termin.test", "name": "t", "kind": "deadline", "versions": [
        {"valid_from": "2026-01-01", "valid_to": "2026-03-14", "value": {"day_of_month": 20},
         "sources": src, "verification": ver},
        {"valid_from": "2026-03-15", "value": {"day_of_month": 25}, "sources": src, "verification": ver}]})
    s = Store()
    s.params[p.id] = p
    days = [d["day_of_month"] for d in s.deadlines("przyklad_ryczalt", 2026, 3)["deadlines"]
            if d["id"] == "termin.test"]
    assert days == [20, 25]


def test_source_fetch_refuses_redirect_outside_https():
    import urllib.error
    import urllib.request

    from fikus.cytaty import _HttpsOnlyRedirects
    req = urllib.request.Request("https://example.org/a")
    with pytest.raises(urllib.error.URLError):
        _HttpsOnlyRedirects().redirect_request(req, None, 302, "Found", {}, "http://example.org/b")


def test_deadline_without_day_is_rejected_at_load():
    with pytest.raises(ValueError, match="day_of_month"):
        Parameter.model_validate({"id": "termin.x", "name": "t", "kind": "deadline", "versions": [
            {"valid_from": "2026-01-01", "value": {"day": 20},
             "sources": [{"title": "akt", "url": "https://example.org/a"}],
             "verification": {"checked_at": "2026-01-01"}}]})

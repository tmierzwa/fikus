"""Wykrywanie zmian w aktach, na których opierają się obowiązujące wersje parametrów.

Skrypt pyta API ELI Sejmu (api.sejm.gov.pl/eli) o każdy akt cytowany jako źródło pierwotne
w wersji, która obowiązuje dziś albo zacznie obowiązywać później. Wersje zamknięte pomija,
bo ich źródła mają prawo być nieaktualne. Zgłasza:

- akt, który przestał obowiązywać;
- nowszy tekst jednolity niż cytowany;
- nowelizacje opublikowane po cytowanym tekście jednolitym (albo zmiany aktu, który tekstu
  jednolitego nie ma), z pominięciem tych, które ktoś już przejrzał i zapisał w
  data/zmiany_sprawdzone.yaml;
- wersje parametrów, które kończą się w ciągu `horizon` dni i nie mają następczyni.

Niczego nie zmienia w danych. Wynik to lista rzeczy do sprawdzenia przez człowieka albo agenta.
"""
from __future__ import annotations

import json
import re
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Callable

import yaml

from .store import Store

API = "https://api.sejm.gov.pl/eli/acts/"
MAX_BYTES = 5 * 1024 * 1024        # metadane aktu mają kilkadziesiąt kB
_ELI_ID = re.compile(r"^https://(?:api\.sejm\.gov\.pl/eli/acts|eli\.gov\.pl/eli)/(DU|MP)/(\d{4})/(\d+)(?:/|$)")

Fetch = Callable[[str], dict]


@dataclass(frozen=True)
class Finding:
    kind: str          # nie_obowiazuje | nowy_tekst | nowelizacja | koniec_wersji | blad
    act: str | None    # identyfikator ELI, np. DU/2025/1461
    params: tuple[str, ...]
    detail: str


def eli_id(url: str) -> str | None:
    """Adres źródła → identyfikator ELI (DU/2025/1461) albo None, gdy to nie akt z ELI."""
    m = _ELI_ID.match(url)
    return f"{m[1]}/{m[2]}/{m[3]}" if m else None


def _order(act: str) -> tuple[int, int]:
    _, year, pos = act.split("/")
    return int(year), int(pos)


class _HttpsOnlyRedirects(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if not newurl.startswith("https://"):
            raise urllib.error.URLError(f"przekierowanie poza https: {newurl}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch_act(act: str) -> dict:
    """Metadane aktu z API ELI."""
    try:                                   # systemowy magazyn certyfikatów, jeśli dostępny
        import truststore
        truststore.inject_into_ssl()
    except ImportError:
        pass
    req = urllib.request.Request(API + act, headers={"User-Agent": "fikus-wykryj-zmiany/0.1",
                                                     "Accept": "application/json"})
    with urllib.request.build_opener(_HttpsOnlyRedirects).open(req, timeout=60) as r:
        body = r.read(MAX_BYTES + 1)
    if len(body) > MAX_BYTES:
        raise ValueError(f"odpowiedź dla {act} ma ponad {MAX_BYTES // 2**20} MB")
    return json.loads(body)


def load_reviewed(path: Path) -> set[str]:
    """Nowelizacje już przejrzane: identyfikatory ELI z data/zmiany_sprawdzone.yaml."""
    if not path.is_file():
        return set()
    entries = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    for e in entries:
        if not {"act", "checked_at", "note"} <= set(e):
            raise ValueError(f"{path.name}: wpis {e!r} potrzebuje pól act, checked_at i note")
    return {e["act"] for e in entries}


def cited_acts(store: Store, today: date) -> dict[str, set[str]]:
    """Akty ELI cytowane jako źródła pierwotne w wersjach obowiązujących dziś lub później."""
    acts: dict[str, set[str]] = {}
    for p in store.params.values():
        for v in p.versions:
            if v.valid_to is not None and v.valid_to < today:
                continue
            for s in v.sources:
                if s.kind == "primary" and (act := eli_id(s.url)):
                    acts.setdefault(act, set()).add(p.id)
    return acts


def check_act(act: str, params: set[str], fetch: Fetch, reviewed: set[str]) -> list[Finding]:
    ps = tuple(sorted(params))
    meta = fetch(act)
    refs = meta.get("references", {})
    out: list[Finding] = []
    if meta.get("inForce") != "IN_FORCE":
        out.append(Finding("nie_obowiazuje", act, ps, f"status w ELI: {meta.get('status')}"))

    base = [r["id"] for r in refs.get("Tekst jednolity dla aktu", [])]
    if base:                                   # cytujemy tekst jednolity: czy jest nowszy?
        texts = [r["id"] for r in fetch(base[0]).get("references", {}).get("Inf. o tekście jednolitym", [])]
        newest = max(texts, key=_order, default=act)
        if _order(newest) > _order(act):
            out.append(Finding("nowy_tekst", act, ps, f"nowszy tekst jednolity: {newest}"))
            return out                         # nowelizacje i tak trzeba czytać w nowym tekście
        changes = refs.get("Nowelizacje po tekście jednolitym", [])
    else:
        if refs.get("Inf. o tekście jednolitym"):
            newest = max((r["id"] for r in refs["Inf. o tekście jednolitym"]), key=_order)
            out.append(Finding("nowy_tekst", act, ps, f"akt ma tekst jednolity {newest}; cytuj tekst jednolity"))
            return out
        changes = refs.get("Akty zmieniające", [])

    for c in sorted(changes, key=lambda r: _order(r["id"])):
        if c["id"] not in reviewed:
            when = f", wchodzi w życie {c['date']}" if c.get("date") else ""
            out.append(Finding("nowelizacja", act, ps, f"{c['id']}{when}"))
    return out


def ending_versions(store: Store, today: date, horizon: int) -> list[Finding]:
    """Ostatnie wersje parametrów, które kończą się najpóźniej za `horizon` dni."""
    out = []
    limit = today + timedelta(days=horizon)
    for p in store.params.values():
        last = p.versions[-1]
        if last.valid_to is not None and last.valid_to <= limit:
            when = "skończyła się" if last.valid_to < today else "kończy się"
            out.append(Finding("koniec_wersji", None, (p.id,),
                               f"ostatnia wersja {when} {last.valid_to} i nie ma następczyni"))
    return out


def detect(store: Store, today: date, fetch: Fetch = fetch_act, reviewed: set[str] = frozenset(),
           horizon: int = 60) -> list[Finding]:
    findings = ending_versions(store, today, horizon)
    for act, params in sorted(cited_acts(store, today).items()):
        try:
            findings += check_act(act, params, fetch, reviewed)
        except (OSError, ValueError, KeyError) as e:      # sieć, zły JSON, nieoczekiwany kształt
            findings.append(Finding("blad", act, tuple(sorted(params)), f"nie da się sprawdzić: {e}"))
    return findings

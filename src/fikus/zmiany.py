"""Wykrywanie zmian w aktach, na których opierają się obowiązujące wersje parametrów.

Skrypt pyta API ELI Sejmu (api.sejm.gov.pl/eli) o każdy akt cytowany jako źródło pierwotne
w wersji, która obowiązuje dziś albo zacznie obowiązywać później. Wersje zamknięte pomija,
bo ich źródła mają prawo być nieaktualne. Zgłasza:

- akt, który przestał obowiązywać;
- nowszy tekst jednolity niż cytowany;
- nowelizacje opublikowane po cytowanym tekście jednolitym (z obu list ELI: nowelizacji po tym
  tekście i aktów zmieniających akt bazowy) albo zmiany aktu, który tekstu jednolitego nie ma, z pominięciem tych, które ktoś już przejrzał i zapisał w
  data/zmiany_sprawdzone.yaml;
- wersje parametrów, które kończą się w ciągu `horizon` dni i nie mają następczyni.

Niczego nie zmienia w danych. Wynik to lista rzeczy do sprawdzenia przez człowieka albo agenta.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Callable

from .cytaty import fetch_bytes
from .store import Store, load_yaml    # load_yaml odrzuca powtórzony klucz

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


def fetch_act(act: str) -> dict:
    """Metadane aktu z API ELI."""
    body, _ = fetch_bytes(API + act, {"User-Agent": "fikus-wykryj-zmiany/0.1",
                                      "Accept": "application/json"}, MAX_BYTES)
    return json.loads(body)


def load_reviewed(path: Path) -> set[str]:
    """Nowelizacje już przejrzane z data/zmiany_sprawdzone.yaml: identyfikator ELI nowelizacji
    albo, gdy wpis ma pole `for`, para „nowelizacja@akt” (przejrzana tylko dla tego aktu)."""
    if not path.is_file():
        return set()
    entries = load_yaml(path) or []
    for e in entries:
        if not {"act", "checked_at", "note"} <= set(e):
            raise ValueError(f"{path.name}: wpis {e!r} potrzebuje pól act, checked_at i note")
    return {f"{e['act']}@{e['for']}" if e.get("for") else e["act"] for e in entries}


def check_act(act: str, params: set[str], fetch: Fetch, reviewed: set[str],
              handled: dict[str, set[str]] | None = None) -> list[Finding]:
    """Zmiany jednego aktu. `handled` to nowelizacje obsłużone w danym parametrze („nowelizacja@akt”
    według identyfikatora parametru): nowelizacja trafia do wyniku tylko z parametrami, które jej nie cytują."""
    ps = tuple(sorted(params))
    handled = handled or {}
    meta = fetch(act)
    refs = meta.get("references", {})
    out: list[Finding] = []
    if meta.get("inForce") != "IN_FORCE":
        out.append(Finding("nie_obowiazuje", act, ps, f"status w ELI: {meta.get('status')}"))

    base = [r["id"] for r in refs.get("Tekst jednolity dla aktu", [])]
    if base:                                   # cytujemy tekst jednolity: czy jest nowszy?
        base_refs = fetch(base[0]).get("references", {})
        texts = [r["id"] for r in base_refs.get("Inf. o tekście jednolitym", [])]
        newest = max(texts, key=_order, default=act)
        if _order(newest) > _order(act):
            out.append(Finding("nowy_tekst", act, ps, f"nowszy tekst jednolity: {newest}"))
            return out                         # nowelizacje i tak trzeba czytać w nowym tekście
        # ELI nie zawsze dopisuje nowelizację do „Nowelizacje po tekście jednolitym” tekstu;
        # pewniejsza jest lista „Akty zmieniające” aktu bazowego. Pozycje w Dz.U. rosną z datą
        # ogłoszenia, więc nowelizacja o pozycji późniejszej niż tekst jednolity nie jest w nim ujęta.
        later = [r for r in base_refs.get("Akty zmieniające", []) if _order(r["id"]) > _order(act)]
        changes = list({r["id"]: r for r in later + refs.get("Nowelizacje po tekście jednolitym", [])}.values())
    else:
        if refs.get("Inf. o tekście jednolitym"):
            newest = max((r["id"] for r in refs["Inf. o tekście jednolitym"]), key=_order)
            out.append(Finding("nowy_tekst", act, ps, f"akt ma tekst jednolity {newest}; cytuj tekst jednolity"))
            return out
        changes = refs.get("Akty zmieniające", [])

    for c in sorted(changes, key=lambda r: _order(r["id"])):
        key = f"{c['id']}@{act}"
        if c["id"] in reviewed or key in reviewed:
            continue
        open_for = tuple(p for p in ps if key not in handled.get(p, ()))
        if open_for:
            when = f", wchodzi w życie {c['date']}" if c.get("date") else ""
            out.append(Finding("nowelizacja", act, open_for, f"{c['id']}{when}"))
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


def _base_act(act: str, fetch: Fetch) -> str:
    """Akt bazowy tekstu jednolitego (DU/2026/592 → DU/1991/350); dla innych aktów sam akt."""
    try:
        base = fetch(act).get("references", {}).get("Tekst jednolity dla aktu", [])
    except (OSError, ValueError, KeyError):   # błąd zgłosi check_act
        return act
    return base[0]["id"] if base else act


def current_acts(store: Store, today: date, fetch: Fetch,
                 handled: dict[str, set[str]] | None = None) -> dict[str, set[str]]:
    """Akty ELI cytowane jako źródła pierwotne w wersjach obowiązujących dziś lub później, z parametrami.

    Pomija starsze teksty jednolite cytowane obok nowszego tekstu tej samej ustawy w tej samej wersji.
    Takie teksty są celowo nieaktualne: dowodzą stanu prawnego z przeszłości (np. od kiedy obowiązuje
    przepis, czyli valid_from). Do `handled` dopisuje według parametru nowelizacje cytowane obok aktu."""
    acts: dict[str, set[str]] = {}
    for p in store.params.values():
        for v in p.versions:
            if v.valid_to is not None and v.valid_to < today:
                continue
            newest: dict[str, str] = {}            # akt bazowy → najnowszy cytowany tekst
            for s in v.sources:
                if s.kind == "primary" and (act := eli_id(s.url)):
                    base = _base_act(act, fetch)
                    if base not in newest or _order(act) > _order(newest[base]):
                        newest[base] = act
            for act in newest.values():
                acts.setdefault(act, set()).add(p.id)
                if handled is not None:            # nowelizacja cytowana obok aktu = obsłużona w tym parametrze
                    handled.setdefault(p.id, set()).update(f"{a}@{act}" for a in newest.values() if a != act)
    return acts


def detect(store: Store, today: date, fetch: Fetch = fetch_act, reviewed: set[str] = frozenset(),
           horizon: int = 60) -> list[Finding]:
    cache: dict[str, dict] = {}

    def cached(act: str) -> dict:                  # każdy akt pobieramy z API raz
        if act not in cache:
            cache[act] = fetch(act)
        return cache[act]

    findings = ending_versions(store, today, horizon)
    handled: dict[str, set[str]] = {}
    for act, params in sorted(current_acts(store, today, cached, handled).items()):
        try:
            findings += check_act(act, params, cached, set(reviewed), handled)
        except (OSError, ValueError, KeyError) as e:      # sieć, zły JSON, nieoczekiwany kształt
            findings.append(Finding("blad", act, tuple(sorted(params)), f"nie da się sprawdzić: {e}"))
    return findings

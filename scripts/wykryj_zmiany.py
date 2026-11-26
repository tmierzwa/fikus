"""Sprawdza w API ELI, czy akty cytowane przy obowiązujących wersjach się zmieniły.

Użycie: python scripts/wykryj_zmiany.py [--dni 60]
--dni: ile dni naprzód szukać wersji kończących się bez następczyni (domyślnie 60).

Kody wyjścia: 0, gdy nie ma nic do sprawdzenia; 1, gdy są zmiany do przejrzenia; 2, gdy któregoś
aktu nie dało się sprawdzić. Przejrzaną nowelizację, która nie zmienia wartości, zapisz
w data/zmiany_sprawdzone.yaml, żeby skrypt przestał ją zgłaszać.
Wynik jest w Markdown, więc w CI trafia wprost do podsumowania zadania.
"""
import argparse
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

from fikus.store import DATA, Store
from fikus.zmiany import detect, load_reviewed

HEADINGS = {
    "nie_obowiazuje": "Akty, które przestały obowiązywać",
    "nowy_tekst": "Nowsze teksty jednolite",
    "nowelizacja": "Nowelizacje do przejrzenia",
    "koniec_wersji": "Wersje kończące się bez następczyni",
    "blad": "Nie udało się sprawdzić",
}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dni", type=int, default=60)
    args = ap.parse_args()
    today = datetime.now(ZoneInfo("Europe/Warsaw")).date()
    findings = detect(Store(), today, reviewed=load_reviewed(DATA / "zmiany_sprawdzone.yaml"),
                      horizon=args.dni)
    print(f"# Zmiany w źródłach, stan na {today}\n")
    if not findings:
        print("Nic do sprawdzenia.")
        return 0
    for kind, heading in HEADINGS.items():
        group = [f for f in findings if f.kind == kind]
        if not group:
            continue
        print(f"## {heading}\n")
        if kind == "nowelizacja":              # jedna pozycja na akt, z listą nowelizacji
            by_act: dict[tuple, list[str]] = {}
            for f in group:
                by_act.setdefault((f.act, f.params), []).append(f.detail)
            for (act, params), details in by_act.items():
                print(f"- {act}, parametry: {', '.join(params)}")
                for d in details:
                    print(f"  - {d}")
        else:
            for f in group:
                act = f"{f.act}: " if f.act else ""
                print(f"- {act}{f.detail} (parametry: {', '.join(f.params)})")
        print()
    return 2 if any(f.kind == "blad" for f in findings) else 1


if __name__ == "__main__":
    sys.exit(main())

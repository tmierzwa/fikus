"""Sprawdza, że każdy cytat przy źródle jest dosłownie w oficjalnym tekście tego źródła.

Użycie: python scripts/sprawdz_cytaty.py [--offline]
--offline: tylko teksty już zapisane w pamięci podręcznej (bez pobierania).
Kończy się kodem 1, jeśli któryś cytat nie zgadza się z tekstem, tekstu nie da się pobrać
albo któraś wersja nie ma sprawdzonego cytatu ze źródła pierwotnego. W trybie --offline
brak tekstu w pamięci nie jest błędem, ale jest liczony osobno.
"""
import sys

from fikus.cytaty import cached_text, fetch_text, quote_in
from fikus.store import Store


def main() -> int:
    offline = "--offline" in sys.argv
    bad = missing = ok = absent = 0
    for p in Store().params.values():
        for v in p.versions:
            primary_quoted = False
            for s in v.sources:
                if not s.quote:
                    continue
                try:
                    text = cached_text(s.url) if offline else fetch_text(s.url)
                except Exception as e:      # noqa: BLE001
                    print(f"BŁĄD   {p.id} {v.valid_from}: nie da się pobrać {s.url}: {e}")
                    bad += 1
                    continue
                if text is None:
                    print(f"BRAK   {p.id} {v.valid_from}: brak tekstu w pamięci dla {s.url}")
                    absent += 1
                    primary_quoted |= s.kind == "primary"   # nie da się sprawdzić offline
                    continue
                if quote_in(s.quote, text):
                    ok += 1
                    primary_quoted |= s.kind == "primary"
                else:
                    print(f"ŹLE    {p.id} {v.valid_from}: cytatu nie ma w {s.url}")
                    bad += 1
            if not primary_quoted:
                missing += 1
                print(f"BEZ    {p.id} {v.valid_from}: brak sprawdzonego cytatu ze źródła pierwotnego")
    print(f"\nzgodne cytaty: {ok}, niezgodne: {bad}, wersje bez cytatu pierwotnego: {missing}"
          + (f", niesprawdzone offline: {absent}" if absent else ""))
    return 1 if bad or missing else 0


if __name__ == "__main__":
    sys.exit(main())

"""Narzędzie opiekuna: generuje listę dni wolnych na rok do wklejenia w data/parameters/kalendarz.yaml.

Wynik trafia do danych przez PR, z cytatem i drugim źródłem. Serwer niczego nie liczy.
Użycie: python scripts/gen_holidays.py 2028
"""
import sys
from datetime import date, timedelta


def easter(y: int) -> date:
    a, b, c = y % 19, y // 100, y % 100
    d, e = b // 4, b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = c // 4, c % 4
    l_ = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l_) // 451
    return date(y, (h + l_ - 7 * m + 114) // 31, (h + l_ - 7 * m + 114) % 31 + 1)


def holidays(y: int) -> list[date]:
    e = easter(y)
    fixed = [(1, 1), (1, 6), (5, 1), (5, 3), (8, 15), (11, 1), (11, 11), (12, 25), (12, 26)]
    hs = {date(y, mo, d) for mo, d in fixed} | {e, e + timedelta(1), e + timedelta(49), e + timedelta(60)}
    if y >= 2025:
        hs.add(date(y, 12, 24))  # Wigilia od 2025 r.
    return sorted(hs)


if __name__ == "__main__":
    print("[" + ", ".join(str(d) for d in holidays(int(sys.argv[1]))) + "]")

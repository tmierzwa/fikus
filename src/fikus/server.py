"""Serwer MCP: narzędzia tylko do odczytu."""
from __future__ import annotations

from datetime import date

try:                                   # mcp >= 2
    from mcp.server.mcpserver import MCPServer as Server
except ImportError:                    # mcp 1.x
    from mcp.server.fastmcp import FastMCP as Server

from .store import Store

mcp = Server(
    "fikus",
    instructions=(
        "Parametry przepisów dla JDG w Polsce, z datą obowiązywania, źródłem i poziomem weryfikacji. "
        "Serwer niczego nie liczy: podaje fakty i opisuje zasady obliczeń (kind=rule) z podstawą prawną; liczy klient. "
        "To nie są porady podatkowe. Sprawdzaj pole confidence.level: "
        "'niska' oznacza wartość bez pełnego kompletu dowodów (cytat ze źródła pierwotnego "
        "i co najmniej dwa inne dowody); nie opieraj na niej rozliczeń bez sprawdzenia."
    ),
)
store = Store()


class BadDate(ValueError):
    pass


def _d(s: str | None) -> date:
    if not s:
        return date.today()
    try:
        return date.fromisoformat(s)
    except ValueError:
        raise BadDate(f"niepoprawna data {s!r}; oczekiwany format RRRR-MM-DD") from None


def _bad_date(e: BadDate) -> dict:
    return {"found": False, "reason": str(e)}


@mcp.tool()
def get_parameter(id: str, as_of: str | None = None) -> dict:
    """Wartość parametru lub opis zasady (kind=rule) obowiązujące w danym dniu (YYYY-MM-DD, domyślnie dziś)."""
    if id not in store.params:
        return {"id": id, "found": False, "reason": "nieznany parametr", "known": sorted(store.params)}
    try:
        return store.get(id, _d(as_of))
    except BadDate as e:
        return _bad_date(e)


@mcp.tool()
def list_parameters(profile: str, as_of: str | None = None) -> list[dict]:
    """Wszystkie parametry obowiązujące dany profil w danym dniu. Profile: patrz list_profiles."""
    try:
        return store.for_profile(profile, _d(as_of))
    except BadDate as e:
        return [_bad_date(e)]


@mcp.tool()
def list_profiles() -> list[dict]:
    """Dostępne profile przykładowe (forma opodatkowania, VAT, rodzaj ZUS)."""
    return [{"id": pid, **p.as_dict()} for pid, p in store.profiles.items()]


@mcp.tool()
def deadlines(profile: str, year: int, month: int) -> dict:
    """Reguły terminów w miesiącu, dni wolne tego miesiąca i zasada przesunięcia. Datę liczy klient."""
    return store.deadlines(profile, year, month)


@mcp.tool()
def get_schema(form: str, as_of: str | None = None) -> dict:
    """Wersja schematu XSD deklaracji (np. JPK_V7M) obowiązująca w danym dniu."""
    pid = f"schemat.{form.lower()}"
    if pid not in store.params:
        return {"form": form, "found": False, "reason": "brak schematu w danych"}
    try:
        return store.get(pid, _d(as_of))
    except BadDate as e:
        return _bad_date(e)


@mcp.tool()
def changes(since: str) -> list[dict]:
    """Wersje parametrów sprawdzone od podanej daty (RRRR-MM-DD), najnowsze pierwsze."""
    try:
        return store.changes(_d(since))
    except BadDate as e:
        return [_bad_date(e)]


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()

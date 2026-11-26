# Zmiany

Format według [Keep a Changelog](https://keepachangelog.com/pl/1.1.0/), wersje według
[Semantic Versioning](https://semver.org/lang/pl/). Zmiany w danych (nowe wersje parametrów)
opisują PR-y i pole `verification`; tu trafiają tylko zmiany w serwerze, modelu danych i zasadach.

## [Niewydane]

## [0.1.0] - 2026-11-26

### Dodane

- Serwer MCP (stdio) z narzędziami `get_parameter`, `list_profiles`, `list_parameters`,
  `deadlines`, `get_schema` i `changes`.
- Dane: składki ZUS i zdrowotna, terminy ZUS, PIT, ryczałtu i JPK_V7, dni wolne na 2026
  i 2027 rok, zasady obliczeń opisane krokami z podstawą prawną.
- Poziom pewności liczony z dowodów oraz skrypt `scripts/sprawdz_cytaty.py`, który sprawdza
  cytaty w oficjalnych tekstach.
- Licencje: kod Apache 2.0, dane CC BY 4.0.

[Niewydane]: https://github.com/tmierzwa/fikus/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/tmierzwa/fikus/releases/tag/v0.1.0

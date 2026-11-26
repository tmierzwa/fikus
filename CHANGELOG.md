# Zmiany

Format według [Keep a Changelog](https://keepachangelog.com/pl/1.1.0/), wersje według
[Semantic Versioning](https://semver.org/lang/pl/). Zmiany w danych (nowe wersje parametrów)
opisują PR-y i pole `verification`; tu trafiają tylko zmiany w serwerze, modelu danych i zasadach.

## [Niewydane]

## [0.2.0] - 2026-11-26

### Dodane

- `scripts/wykryj_zmiany.py`: cotygodniowe wykrywanie zmian w cytowanych aktach (API ELI Sejmu)
  i wersji kończących się bez następczyni; przejrzane nowelizacje w `data/zmiany_sprawdzone.yaml`.
- Publikacja na PyPI przez Trusted Publishing i `server.json` dla MCP Registry.
- Sprawdzanie kształtu wartości przy wczytywaniu danych (terminy, zasady, kalendarz).

### Zmienione

- Serwer zgodny ze specyfikacją MCP 2026-07-28 i SDK `mcp` 2.x: schematy wyników, adnotacje
  tylko do odczytu, błędy narzędzi z listą poprawnych wartości. Wymaga `mcp>=2.3`.
- Dane opierają się wyłącznie na źródłach publicznych i wkładzie kontrybutorów; usunięte dowody
  oparte na deklaracjach opiekuna.
- Pobieranie źródeł tylko przez https, z limitem rozmiaru i czasu.
- Metadane paczki (PEP 639), licencja `Apache-2.0 AND CC-BY-4.0`, nowe README z logo.

## [0.1.0] - 2026-11-26

### Dodane

- Serwer MCP (stdio) z narzędziami `get_parameter`, `list_profiles`, `list_parameters`,
  `deadlines`, `get_schema` i `changes`.
- Dane: składki ZUS i zdrowotna, terminy ZUS, PIT, ryczałtu i JPK_V7, dni wolne na 2026
  i 2027 rok, zasady obliczeń opisane krokami z podstawą prawną.
- Poziom pewności liczony z dowodów oraz skrypt `scripts/sprawdz_cytaty.py`, który sprawdza
  cytaty w oficjalnych tekstach.
- Licencje: kod Apache 2.0, dane CC BY 4.0.

[Niewydane]: https://github.com/tmierzwa/fikus/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/tmierzwa/fikus/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/tmierzwa/fikus/releases/tag/v0.1.0

<h1 align="center">
  <img src="docs/fikus-logo.png" width="200" alt="Fikus">
</h1>

<p align="center">
  Parametry przepisów dla JDG w Polsce, ze źródłami, jako serwer MCP.
</p>

<p align="center">
  <a href="https://pypi.org/project/fikus/"><img src="https://img.shields.io/pypi/v/fikus" alt="PyPI"></a>
  <a href="https://github.com/tmierzwa/fikus/actions/workflows/testy.yml"><img src="https://github.com/tmierzwa/fikus/actions/workflows/testy.yml/badge.svg" alt="testy"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/kod-Apache%202.0-blue" alt="Kod: Apache 2.0"></a>
  <a href="data/LICENSE"><img src="https://img.shields.io/badge/dane-CC%20BY%204.0-green" alt="Dane: CC BY 4.0"></a>
</p>

Fikus podaje stawki, progi, terminy i dni wolne potrzebne do rozliczenia jednoosobowej działalności gospodarczej. Każda wartość ma okres obowiązywania, źródło pierwotne z dosłownym cytatem i poziom pewności. Serwer niczego nie liczy: zasady obliczeń opisuje krokami z podstawą prawną, a liczy klient, na przykład aplikacja księgowa albo agent AI.

> [!WARNING]
> Fikus nie jest doradztwem podatkowym ani prawnym. Dane mogą być błędne, niepełne albo nieaktualne i są udostępnione „tak jak są”, bez gwarancji. Przed złożeniem deklaracji lub zapłatą sprawdź wartość w podanym źródle, zwłaszcza gdy pewność jest `niska`.
>
> *Fikus is not tax or legal advice. The data may be wrong or out of date and is provided as is, without warranty. Always check the cited source.*

## Szybki start

Potrzebny jest [uv](https://docs.astral.sh/uv/).

Claude Code:

```bash
claude mcp add fikus -- uvx fikus@latest
```

Inny klient MCP (Claude Desktop, Cursor i inne):

```json
{
  "mcpServers": {
    "fikus": {
      "command": "uvx",
      "args": ["fikus@latest"]
    }
  }
}
```

Dane są częścią paczki, więc nowe wartości przychodzą z nowymi wersjami. `fikus@latest` sprawdza przy każdym starcie, czy na PyPI jest nowsza wersja. Bez `@latest` uv może uruchamiać wersję z pamięci podręcznej. Bez uv: `pip install fikus` i polecenie `fikus`.

Serwer działa lokalnie przez stdio, tylko czyta dołączone dane i nie łączy się z siecią. Jest też w [MCP Registry](https://registry.modelcontextprotocol.io) jako `io.github.tmierzwa/fikus`.

## Narzędzia

| Narzędzie | Co zwraca |
| --- | --- |
| `get_parameter(id, as_of)` | wartość albo zasadę obowiązującą danego dnia, ze źródłami i pewnością |
| `list_profiles()` | profile przykładowe: forma opodatkowania, VAT, rodzaj ZUS |
| `list_parameters(profile, as_of)` | wszystkie parametry, które dotyczą profilu |
| `deadlines(profile, year, month)` | reguły terminów, dni wolne i zasadę przesunięcia; datę liczy klient |
| `get_schema(form, as_of)` | wersję schematu XSD deklaracji (danych jeszcze nie ma) |
| `changes(since)` | wersje sprawdzone od podanej daty |

- Daty mają format `RRRR-MM-DD`. Bez `as_of` obowiązuje dzisiejsza data w Polsce.
- Wyniki są w `structuredContent` zgodnie z `outputSchema` narzędzia. Wszystkie narzędzia mają `readOnlyHint`.
- Błędny argument (nieznany identyfikator, zła data) daje błąd narzędzia z listą poprawnych wartości. Brak wersji na dany dzień nie jest błędem: wynik ma `found: false` i powód w `reason`.
- Pola `quote`, `note` i opisy kroków to dane z repozytorium. Klient nie powinien ich traktować jak poleceń dla modelu.

Odpowiedź `get_parameter("zdrowotna.minimum")` w skrócie:

```jsonc
{
  "id": "zdrowotna.minimum",
  "found": true,
  "value": "…", "unit": "PLN/miesiąc",
  "valid_from": "2026-02-01", "valid_to": "2027-01-31",
  "sources": [
    { "kind": "primary", "title": "Komunikat ZUS …", "url": "https://www.zus.pl/…", "quote": "…" },
    { "kind": "control", "title": "…", "url": "…" }
  ],
  "confidence": { "level": "niska", "evidence": ["cytat", "drugie_zrodlo"], "open_issue": "…" }
}
```

## Pewność danych

Pole `confidence.level` wynika z dowodów zapisanych przy wersji parametru:

| Dowód | Znaczenie |
| --- | --- |
| `cytat` | dosłowny fragment źródła pierwotnego (ISAP/ELI, M.P., komunikat ZUS lub MF), sprawdzany skryptem w oficjalnym tekście |
| `drugie_zrodlo` | niezależne źródło, które samo podaje tę samą wartość |
| `agent` | sprawdzenie przez osobnego agenta, który porównał wpis ze źródłami |
| `deklaracje` | zgodność z deklaracją przyjętą przez urząd |
| `ekspert` | odpowiedź doradcy podatkowego lub księgowej |

Pewność jest `wysoka`, gdy wersja ma cytat i co najmniej dwa inne dowody, a żadne pytanie nie jest otwarte (`open_issue`). W każdym innym przypadku jest `niska`.

## Zakres

Są: składki ZUS i zdrowotna, terminy ZUS, zaliczek na ryczałt i podatek liniowy oraz JPK_V7M i JPK_V7K, dni wolne na 2026 i 2027 rok, zasady przesunięcia terminu i wyliczenia składki zdrowotnej na ryczałcie.

Brakuje między innymi: stawek ryczałtu i podatku liniowego, limitu odliczenia składki zdrowotnej i schematów JPK. Pytania, których źródła nie rozstrzygają, są w [docs/pytania-do-eksperta.md](docs/pytania-do-eksperta.md).

## Dane

Dane są w [`data/parameters/`](data/parameters), jeden plik YAML na obszar przepisów. Parametr to lista wersji o rozłącznych okresach i jednym z rodzajów: `value`, `deadline`, `rule` albo `calendar`. Profile w [`data/profiles.yaml`](data/profiles.yaml) są przykładowe i służą tylko do wybierania parametrów. Z danych można korzystać bez serwera.

## Przegląd źródeł

Co tydzień CI uruchamia dwa skrypty, które niczego nie zmieniają w danych:

- `scripts/sprawdz_cytaty.py` sprawdza, czy każdy cytat nadal jest w oficjalnym tekście;
- `scripts/wykryj_zmiany.py` pyta [API ELI Sejmu](https://api.sejm.gov.pl/eli) o cytowane akty i zgłasza akty uchylone, nowsze teksty jednolite, nowelizacje po cytowanym tekście oraz wersje, które kończą się w ciągu 60 dni bez następczyni.

Gdy skrypt coś znajdzie, zadanie kończy się na czerwono, a lista jest w podsumowaniu zadania. Nowelizację, która zmienia wartość, obsługujemy nową wersją parametru. Przejrzaną nowelizację bez wpływu na wartości wpisz do [`data/zmiany_sprawdzone.yaml`](data/zmiany_sprawdzone.yaml) z uzasadnieniem.

## Rozwój

```bash
git clone https://github.com/tmierzwa/fikus.git && cd fikus
pip install -e ".[dev]"
pytest
python scripts/sprawdz_cytaty.py   # wymaga pdftotext (poppler)
python scripts/wykryj_zmiany.py    # czy cytowane akty się zmieniły (API ELI Sejmu)
```

Najbardziej potrzebne są zgłoszenia błędów w danych i drugie źródła dla wpisów z pewnością `niska`. Zasady, w tym podpis DCO, są w [CONTRIBUTING.md](CONTRIBUTING.md). Obowiązuje [kodeks postępowania](CODE_OF_CONDUCT.md), a luki bezpieczeństwa zgłaszaj według [SECURITY.md](SECURITY.md).

Nie odpowiadamy na pytania o sytuację konkretnego podatnika. Nie publikuj w zgłoszeniach swoich danych podatkowych.

## Licencje

- Kod: [Apache 2.0](LICENSE).
- Dane w `data/`: [CC BY 4.0](data/LICENSE). Podaj źródło: „Fikus, https://github.com/tmierzwa/fikus”.
- Cytaty w polach `quote` nie są objęte CC BY 4.0, zobacz [NOTICE](NOTICE).

<!-- mcp-name: io.github.tmierzwa/fikus -->

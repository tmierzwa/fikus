# Fikus

Fikus to serwer MCP z parametrami przepisów dla jednoosobowej działalności gospodarczej (JDG) w Polsce: stawkami, progami, terminami i dniami wolnymi. Każda wartość ma okres obowiązywania, źródło z dosłownym cytatem i poziom pewności. Serwer niczego nie liczy. Zasady obliczeń opisuje słowami, krok po kroku, z podstawą prawną, a liczy klient, na przykład aplikacja księgowa albo agent AI.

## Zastrzeżenie

Fikus nie jest doradztwem podatkowym ani prawnym i nie zastępuje doradcy podatkowego ani biura rachunkowego. Nie odpowiada na pytania o sytuację konkretnego podatnika.

Dane mogą być błędne, niepełne albo nieaktualne, mimo opisanej niżej weryfikacji. Przed złożeniem deklaracji lub zapłatą sprawdź wartość w źródle podanym przy parametrze. Na wersje z pewnością `niska` uważaj szczególnie.

Kod i dane udostępniamy „tak jak są”, bez gwarancji. Autorzy nie odpowiadają za skutki ich użycia, w tym za zaległości podatkowe, odsetki i sankcje. Szczegóły są w licencjach.

*Fikus is not tax or legal advice. The data may be wrong or out of date and is provided as is, without warranty. Always check the cited source.*

## Uruchomienie

Potrzebny jest Python 3.11 lub nowszy. Skrypt sprawdzający cytaty wymaga też `pdftotext` (pakiet poppler).

```
git clone https://github.com/tmierzwa/fikus.git
cd fikus
pip install -e ".[dev]"
pytest
python scripts/sprawdz_cytaty.py   # czy cytaty są w oficjalnych tekstach
fikus                              # serwer MCP przez stdio
```

Konfiguracja klienta MCP (na przykład Claude Code, plik `.mcp.json`):

```json
{
  "mcpServers": {
    "fikus": { "command": ".venv/bin/fikus", "args": [] }
  }
}
```

## Narzędzia MCP

| Narzędzie | Co zwraca |
| --- | --- |
| `get_parameter(id, as_of)` | wartość lub opis zasady na dany dzień, źródła i dowody weryfikacji |
| `list_profiles()` | dostępne profile przykładowe |
| `list_parameters(profile, as_of)` | wszystkie parametry danego profilu |
| `deadlines(profile, year, month)` | reguły terminów, dni wolne i zasadę przesunięcia; datę liczy klient |
| `get_schema(form, as_of)` | wersję schematu XSD deklaracji (danych jeszcze nie ma) |
| `changes(since)` | wersje sprawdzone od podanej daty |

## Dane

Dane są w `data/parameters/`, jeden plik YAML na obszar przepisów. Parametr to lista wersji, a okresy wersji nie mogą na siebie nachodzić (pilnują tego walidator i testy). Parametr ma jeden z czterech rodzajów (`kind`): `value` (wartość), `deadline` (reguła terminu), `rule` (zasada obliczeń w krokach) albo `calendar` (dni wolne). Kroki zasady wskazują parametry, których używają (`uses`), a walidator sprawdza, czy te parametry istnieją.

Profile w `data/profiles.yaml` to przykłady połączeń formy opodatkowania, VAT i rodzaju ZUS. Służą do wybierania parametrów, które dotyczą danego przypadku.

Poziom pewności (`confidence`) jest w każdej odpowiedzi serwera i wynika z dowodów zapisanych przy wersji:

- `cytat`: dosłowny fragment źródła pierwotnego; `scripts/sprawdz_cytaty.py` sprawdza, czy jest w oficjalnym tekście;
- `drugie_zrodlo`: niezależne źródło, które samo podaje tę samą wartość (`independent: true` albo `kind: control`);
- `agent`: sprawdzenie przez osobnego agenta (`weryfikator-zrodel`), który porównuje wpis ze źródłami;
- `deklaracje`: zgodność z deklaracją przyjętą przez urząd;
- `ekspert`: odpowiedź doradcy podatkowego lub księgowej.

Pewność jest `wysoka`, gdy wersja ma cytat i co najmniej dwa inne dowody, a żadne pytanie nie pozostaje otwarte (`open_issue`). W pozostałych przypadkach jest `niska`.

## Stan

Wczesna wersja. Obejmuje składki ZUS i zdrowotną, terminy ZUS, ryczałtu i JPK_V7 oraz dni wolne na 2026 i 2027 rok. Brakuje między innymi stawek ryczałtu i podatku liniowego, limitu odliczenia składki zdrowotnej i schematów JPK. Część wersji ma pewność niską. Pytania, których źródła nie rozstrzygają, są w [docs/pytania-do-eksperta.md](docs/pytania-do-eksperta.md).

## Współtworzenie

Zgłoszenia błędów w danych i nowe źródła są najbardziej potrzebne. Zasady są w [CONTRIBUTING.md](CONTRIBUTING.md), a obowiązuje [kodeks postępowania](CODE_OF_CONDUCT.md).

## Licencje

- Kod: [Apache License 2.0](LICENSE).
- Dane w `data/`: [CC BY 4.0](data/LICENSE). Korzystając z danych, podaj źródło: „Fikus, https://github.com/tmierzwa/fikus”.
- Cytaty w polach `quote` nie są objęte licencją CC BY 4.0. Wyjaśnienie jest w pliku [NOTICE](NOTICE).

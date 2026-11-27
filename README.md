<h1 align="center">
  <img src="docs/fikus-logo.png" width="200" alt="Fikus">
</h1>

<p align="center">
  Serwer MCP dla przepisów dotyczących JDG w Polsce, ze źródłami.
</p>

<p align="center">
  <a href="https://pypi.org/project/fikus/"><img src="https://img.shields.io/pypi/v/fikus" alt="PyPI"></a>
  <a href="https://github.com/tmierzwa/fikus/actions/workflows/testy.yml"><img src="https://github.com/tmierzwa/fikus/actions/workflows/testy.yml/badge.svg" alt="testy"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/kod-Apache%202.0-blue" alt="Kod: Apache 2.0"></a>
  <a href="data/LICENSE"><img src="https://img.shields.io/badge/dane-CC%20BY%204.0-green" alt="Dane: CC BY 4.0"></a>
</p>

Fikus podaje stawki, progi, terminy i dni wolne potrzebne do rozliczenia jednoosobowej działalności gospodarczej. Każda wartość ma okres obowiązywania, źródło pierwotne z dosłownym cytatem i poziom pewności. 

Serwer niczego nie liczy: zasady obliczeń opisuje krokami z podstawą prawną, a liczy klient, na przykład aplikacja księgowa albo agent AI.

> [!WARNING]
> Fikus nie jest doradztwem podatkowym ani prawnym. Dane mogą być błędne, niepełne albo nieaktualne i są udostępnione „tak jak są”, bez gwarancji. Przed złożeniem deklaracji lub zapłatą sprawdź wartość w podanym źródle, zwłaszcza gdy pewność jest `niska` albo `średnia`.
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
| `get_schema(form, as_of)` | wersję schematu XSD deklaracji (JPK_V7M, JPK_V7K, JPK_PKPIR, JPK_EWP, PIT-36, PIT-36L, PIT-28) z adresem pliku XSD (`xsd_url`) albo wzór formularza (ZUS_DRA) |
| `changes(since)` | wersje sprawdzone od podanej daty |

- Daty mają format `RRRR-MM-DD`. Bez `as_of` obowiązuje dzisiejsza data w Polsce.
- Wyniki są w `structuredContent` zgodnie z `outputSchema` narzędzia. Wszystkie narzędzia mają `readOnlyHint`.
- Błędny argument (nieznany identyfikator, zła data) daje błąd narzędzia z listą poprawnych wartości. Brak wersji na dany dzień nie jest błędem: wynik ma `found: false` i powód w `reason`.
- Pola `quote`, `note` i opisy kroków to dane z repozytorium. Klient nie powinien ich traktować jak poleceń dla modelu.
- `get_schema` przyjmuje symbol z łącznikiem albo podkreśleniem, wielkimi albo małymi literami (PIT-36L, pit_36l). Dla JPK_V7M i JPK_V7K dniem jest pierwszy dzień okresu rozliczeniowego, dla zeznań PIT pierwszy dzień roku podatkowego, a dla ZUS_DRA dzień złożenia dokumentu.
- `xsd_url` w `get_schema` to adres, pod którym urząd udostępnia plik XSD. Dla JPK_V7M, JPK_V7K i zeznań PIT to adres schematu w Centralnym Repozytorium Wzorów Dokumentów Elektronicznych, a dla JPK_PKPIR i JPK_EWP adres pliku na gov.pl. Nie jest to przestrzeń nazw schematu i może się zmienić bez nowej wersji struktury.

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
  "confidence": { "level": "niska", "evidence": ["cytat", "drugie_zrodlo"], "open_issue": "…", "open_issue_scope": "value" }
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

| Poziom | Kiedy |
| --- | --- |
| `wysoka` | cytat i co najmniej dwa inne dowody, bez otwartego pytania |
| `średnia` | ten sam komplet dowodów, ale otwarte pytanie dotyczy tylko przypadku brzegowego (`open_issue_scope: edge_case`) |
| `niska` | mniej dowodów albo otwarte pytanie o samą wartość lub rdzeń zasady (`open_issue_scope: value`) |

- Przy pewności `średnia` przeczytaj `confidence.open_issue`. Opisuje przypadek, którego zasada nie rozstrzyga; jeśli Cię nie dotyczy, wartość ma pełny komplet dowodów.
- Pytanie bez zakresu w danych traktujemy jak pytanie o wartość.
- Przy zasadzie obliczeń (kroki słowne) dowód `drugie_zrodlo` daje tylko dokument, który sam podaje wszystkie kroki zasady. Strony urzędów potwierdzające część kroków są w danych zwykłymi źródłami z cytatem i nie podnoszą pewności. Dlatego wszystkie zasady mają dziś pewność `niska`, dopóki nie dostaną innych dowodów (deklaracje, ekspert).
- Wartość złożona z kilku pól (na przykład schemat JPK) może mieć drugie źródło potwierdzone pole po polu. Źródło wymienia w `confirms` pola, które samo podaje (klucze wartości i `period` dla okresu obowiązywania). Dowód `drugie_zrodlo` jest spełniony, gdy każde pole i okres podają co najmniej dwa różne dokumenty z cytatem, w tym źródło pierwotne. Jeden dokument liczy się raz. Gdy wersja używa `confirms`, liczy się tylko ta ścieżka: źródło kontrolne bez `confirms` nie zastępuje potwierdzenia pól. `confirms` wymaga cytatu. Pola, którym brakuje drugiego dokumentu, są w `confidence.unconfirmed_fields`.

## Zakres

Dane obejmują trzy formy opodatkowania: ryczałt od przychodów ewidencjonowanych, podatek liniowy i skalę podatkową.

Są:

- forma opodatkowania:
  - limit przychodów uprawniający do ryczałtu, wyłączenia z ryczałtu i z podatku liniowego;
  - wybór formy opodatkowania: termin i sposób złożenia oświadczenia, kontynuacja i rezygnacja;
- podatek dochodowy:
  - stawki ryczałtu i dosłowny zakres usług informatycznych i inżynierskich według PKWiU (bez przypisania stawki do przychodu);
  - stawka podatku liniowego i limit odliczenia składki zdrowotnej;
  - progi i stawki skali podatkowej;
  - zasady ustalenia podatku i zaliczek miesięcznych dla każdej z trzech form;
  - zaliczki kwartalne i uproszczone, kwartalne opłacanie ryczałtu i limity w euro, od których zależą;
  - zaliczki i ryczałt w okresie zawieszenia działalności;
  - data uzyskania przychodu i przeliczenie przychodu w walucie obcej;
  - ulgi i odliczenia dla każdej z trzech form, z limitami (internet, dzieci, termomodernizacja, darowizny,
    ulga rehabilitacyjna, IKZE);
  - IP Box (stawka i zasada) i ulga badawczo-rozwojowa (procent odliczenia i zasada);
  - wspólne opodatkowanie małżonków i opodatkowanie osoby samotnie wychowującej dzieci, z wyłączeniami;
- koszty na skali i podatku liniowym:
  - limity wydatków na samochody osobowe;
  - próg środka niskocennego, jednorazowa amortyzacja i zasady amortyzacji (bez tabeli stawek);
  - wyłączenie z kosztów płatności poza rachunkiem płatniczym;
- ewidencja i zeznania:
  - zasady ewidencji przychodów na ryczałcie i termin wpisu;
  - schematy zeznań PIT-36, PIT-36L i PIT-28;
  - dane autoryzujące do podpisu deklaracji, zeznań i plików JPK;
- VAT:
  - stawka podstawowa i obniżone, limit zwolnienia podmiotowego, zasada odliczenia;
  - obowiązek wystawiania faktur w KSeF;
  - limit zwolnienia z kasy rejestrującej;
- terminy:
  - zaliczek miesięcznych i kwartalnych oraz zeznań rocznych;
  - JPK_V7M i JPK_V7K;
  - wpisu do ewidencji przychodów;
  - składek ZUS i rocznego rozliczenia składki zdrowotnej;
  - zasada przesunięcia terminu;
  - dni wolne na 2026 i 2027 rok;
- JPK:
  - schematy JPK_V7M, JPK_V7K, JPK_PKPIR i JPK_EWP (narzędzie `get_schema`);
  - zasady przesyłania księgi i ewidencji na ryczałcie w formie JPK;
- składki społeczne:
  - stopy składek, Fundusz Pracy i Fundusz Solidarnościowy;
  - podstawa pełna i preferencyjna, limit rocznej podstawy;
  - ulga na start i Mały ZUS Plus;
  - minimalne i prognozowane przeciętne wynagrodzenie;
  - obowiązek składania deklaracji ZUS DRA i wzór formularza DRA;
- składka zdrowotna:
  - progi i kwoty na ryczałcie;
  - stopy i zasady obliczenia na podatku liniowym i skali, z rozliczeniem rocznym;
  - minimalna składka.

Wartości na 2027 rok są tam, gdzie urząd już je ogłosił. Pozostałe wersje kończą się z końcem okresu, na który je
ogłoszono, a zapytanie o późniejszy dzień daje `found: false`.

Brakuje między innymi:

- karty podatkowej (poza wyłączeniami, w których jest wymieniona);
- tabeli stawek amortyzacyjnych i amortyzacji poza zasadami ogólnymi;
- kwot ulg na robotyzację, ekspansję i innych ulg innowacyjnych (zasady ulg tylko je wymieniają);
- specyfikacji technicznych (EWD i KEDU w ZUS, interfejsy JPK i e-Deklaracji).

Każda zasada wymienia przepisy, których nie opisuje. Pytania, których źródła nie rozstrzygają, są w [docs/pytania-do-eksperta.md](docs/pytania-do-eksperta.md).

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

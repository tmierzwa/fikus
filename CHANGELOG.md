# Zmiany

Format według [Keep a Changelog](https://keepachangelog.com/pl/1.1.0/), wersje według
[Semantic Versioning](https://semver.org/lang/pl/). Zmiany w danych (nowe wersje parametrów)
opisują PR-y i pole `verification`; tu trafiają tylko zmiany w serwerze, modelu danych i zasadach.

## [Niewydane]

### Dodane

- Zasady obliczeń można potwierdzać krok po kroku: źródło wymienia w `confirms` kroki, które samo podaje
  (`step_1`, `step_2`, …), tak jak pola wartości złożonej. Dowód `drugie_zrodlo` jest spełniony, gdy każdy
  krok podają co najmniej dwa różne dokumenty z cytatem, w tym źródło pierwotne. Okresu zasady nie
  potwierdza się osobno. Brakujące kroki
  są w `confidence.unconfirmed_fields` (decyzja z 27 listopada 2026 r.).
- Pytania do eksperta mają dyskusje w GitHub Discussions, w kategorii „Pytania do eksperta”, z formularzem
  dla nowych pytań. Odpowiedź z dyskusji trafia do `verification.expert` dopiero po potwierdzeniu przez
  opiekuna (decyzja z 27 listopada 2026 r.).

### Zmienione

- Zasada obliczeń może mieć `not_covered` bez `see_also`. Wylicza wtedy sprawy, których zasada nie opisuje
  (dawne zdania „Ta zasada nie opisuje…” w krokach), a `see_also` opcjonalnie wskazuje parametry, które
  te sprawy opisują (dawne odesłania „…opisuje zasada …”). Tego opisu nie potwierdza się dokumentami, więc nie
  blokuje pewności zasady. Przy wartości `not_covered` nadal wymaga `see_also` (decyzja z 27 listopada 2026 r.).

## [0.5.0] - 2026-11-27

### Dodane

- Pola `not_covered` i `see_also` w wersji parametru i w wyniku `get_parameter`. Wartość, która ma pełny
  komplet dowodów, a nie rozstrzyga sposobu stosowania (na przykład podstawy limitu), mówi, czego nie
  rozstrzyga, i wskazuje parametry, które to opisują. Pytanie o sposób stosowania ma tamten parametr, więc
  nie obniża pewności samej wartości. Klienci (Staffkey) powinni sprawdzać `see_also` przy takiej wartości.

### Zmienione

- Skrypt cytatów czyta w plikach XML i XSD wartości atrybutów, a na stronach adresy linków, i dopisuje je
  na końcu tekstu źródła. Można więc zacytować kod systemowy i wersję schematu z pliku XSD oraz adres pliku
  z linku na stronie urzędu. Zmienił się format pamięci podręcznej `.cache/zrodla/`, więc teksty źródeł
  pobierają się od nowa.
- Adres pliku schematu (`xsd_url`) potwierdza też sam plik spod tego adresu, gdy cytat z niego podaje kod
  systemowy formularza. Model odrzuca taki cytat bez kodu systemowego.
- Pobieranie źródeł (`sprawdz_cytaty.py`, `wykryj_zmiany.py`) ma łączny limit czasu 120 s na jeden adres
  i jedną ponowną próbę po błędzie sieci lub serwera. Wcześniej limit 60 s dotyczył tylko jednej operacji
  na gnieździe i powolny serwer mógł zablokować sprawdzanie na godziny.
- CI: w PR teksty źródeł są przywracane z pamięci podręcznej i pobierane są tylko brakujące; na main,
  w cotygodniowym przebiegu i na żądanie wszystko od nowa. Zadania mają limity czasu, a instalacja
  pakietów korzysta z pamięci pip.
- `sprawdz_cytaty.py` pobiera brakujące teksty źródeł równolegle: najwyżej 6 naraz i 2 z jednego serwera.
  Cytaty sprawdza dalej po kolei, więc komunikaty, podsumowanie i kod wyjścia się nie zmieniają.
  Zapis tekstu do pamięci podręcznej idzie przez plik tymczasowy, a dopisanie do `indeks.tsv` pod blokadą.
- Notatki wersji opisują tylko obecny stan. Historię edycji danych w 23 notatkach (zdania „Poprawka…”,
  opis poprzednich błędów, wzmianki o weryfikatorze) zastąpiło krótkie zdanie „Korekta z …: zmienione …”
  albo usunięto ją, gdy poprawka dotyczyła samej notatki. Wartości, okresy, źródła i kroki się nie zmieniają.
  Test odrzuca historię edycji w notatkach.
- Zasady źródeł: poradnik ZUS opublikowany na zus.pl jest komunikatem ZUS, czyli źródłem pierwotnym (CLAUDE.md).

## [0.4.5] - 2026-11-27

### Dodane

- Deklaracja ZUS DRA za siebie: schemat elektroniczny `schemat.kedu` (KEDU 5.7, specyfikacja EWD 2.27;
  `get_schema` zwraca go dla symbolu KEDU), kody `zus.kod.termin_przesylania` i `zus.kod.tytul_ubezpieczenia`
  (załącznik nr 24 do Dz.U. 2026 poz. 518), zasady `zasada.dra_finansowanie_skladek` (bloki IV i VI)
  i `zasada.dra_bloki_zdrowotne` (bloki XI i XII) w pliku `data/parameters/zus_dra.yaml` oraz podstawa
  `zdrowotna.ryczalt.podstawa` (podstawa składki zdrowotnej na ryczałcie dla każdego progu).

### Zmienione

- Przy zasadach obliczeń drugim źródłem jest tylko dokument, który sam podaje wszystkie kroki zasady.
  Strony MF i ZUS potwierdzające część kroków są teraz zwykłymi źródłami, a częściowe strony portali
  usunięto ze źródeł. Pewność 15 wersji zasad spadła do `niska` (decyzja z 27 listopada 2026 r.).

## [0.4.0] - 2026-11-27

### Dodane

- Parametr `ryczalt.stawki`: stawki ryczałtu od przychodów ewidencjonowanych według punktów
  art. 12 ust. 1 ustawy o zryczałtowanym podatku dochodowym (nowy plik `data/parameters/podatek.yaml`).
- Parametr `ryczalt.zakres_uslug`: dosłowne brzmienie liter art. 12 ust. 1 ustawy o zryczałtowanym podatku
  dochodowym, które wymieniają usługi informatyczne i inżynierskie, z symbolami PKWiU 2015 i wyłączeniami
  (pkt 2 lit. a, e, i; pkt 2a lit. b, c; pkt 2b lit. a, b; pkt 4 lit. e). Nie przypisuje stawki do przychodu.
- Schematy `schemat.jpk_v7m`, `schemat.jpk_v7k` i `schemat.jpk_pkpir` oraz zasady przesyłania ksiąg
  w formie JPK (`zasada.jpk_pd_pkpir`, `zasada.jpk_pd_ryczalt`) w nowym pliku `data/parameters/jpk.yaml`.
  `get_schema` zwraca teraz dane dla tych symboli.
- Schemat `schemat.jpk_ewp` (JPK_EWP, wariant 4 od 2026 r.); `get_schema` zwraca go dla symbolu JPK_EWP.
- Nowy plik `data/parameters/ewidencja.yaml`: termin `termin.ewidencja_przychodow_wpis` (wpis przychodów
  za miesiąc na ryczałcie; `deadlines` zwraca go dla profili na ryczałcie) oraz zasady `zasada.ewidencja_przychodow`,
  `zasada.przychod_data_uzyskania` i `zasada.przychod_w_walucie`.
- Parametry VAT w nowym pliku `data/parameters/vat.yaml`: `vat.stawki` (stawka podstawowa i obniżone
  w okresie z art. 146ef ustawy o VAT), `vat.limit_zwolnienia` (limit zwolnienia podmiotowego z art. 113
  ust. 1) i zasada `zasada.vat_odliczenie` (prawo do odliczenia, moment i korekta, samochody, wyłączenia).
- Nowy plik `data/parameters/forma_opodatkowania.yaml`: limit przychodów uprawniający do ryczałtu
  (`ryczalt.limit_przychodow_euro`, art. 6 ust. 4 ustawy o zryczałtowanym podatku dochodowym) oraz zasady
  `zasada.ryczalt_wylaczenia` (art. 8), `zasada.liniowy_wylaczenia` (art. 9a ust. 3 i 5 ustawy o PIT)
  i `zasada.wybor_formy_opodatkowania` (termin i sposób wyboru ryczałtu i podatku liniowego, kontynuacja, rezygnacja).
- Schematy e-Deklaracji zeznań rocznych `schemat.pit_36`, `schemat.pit_36l` i `schemat.pit_28` (za 2025 r.
  i od 2026 r., według wyróżników wzorów w CRWDE) oraz zasada `zasada.dane_autoryzujace` (podpis danymi
  autoryzującymi zeznań PIT i plików JPK_V7M, JPK_EWP i JPK_PKPIR) w nowym pliku `data/parameters/pit_zeznania.yaml`.
- Zasady `zasada.dra_obowiazek` (deklaracja ZUS DRA za siebie) i `zasada.roczne_rozliczenie_zdrowotnej`
  oraz wzór formularza `schemat.zus_dra` (od 1 maja 2026 r., według dnia złożenia) w nowym pliku
  `data/parameters/zus_dra.yaml`. `get_schema("ZUS_DRA")` zwraca wzór DRA.
- Koszty uzyskania przychodów na skali i podatku liniowym w nowym pliku `data/parameters/koszty.yaml`:
  `koszty.samochod.limity` (limity wartości samochodu osobowego z art. 23 ust. 1 pkt 4, 47 i 47a ustawy o PIT
  według emisji CO2 od 2026 r. oraz udziały wydatków z pkt 46 i 46a), `amortyzacja.srodek_niskocenny.limit`
  (art. 22d ust. 1 i art. 22f ust. 3), `amortyzacja.jednorazowa.limit_euro` (art. 22k ust. 7),
  `amortyzacja.jednorazowa.limit_nowe_srodki` (art. 22k ust. 14) oraz zasady `zasada.amortyzacja`
  (metody, początek odpisów, odpisy jednorazowe, odesłanie do Wykazu stawek) i `zasada.platnosci_gotowkowe_koszty`
  (art. 22p, z nową wersją od 2027 r.).
- Nowy plik `data/parameters/ksef_kasy.yaml`: zasada `zasada.ksef_obowiazek` (obowiązek wystawiania faktur
  w KSeF, przepisy przejściowe na 2026 r., wyłączenia, kary od 2027 r.) i wartość `vat.kasa_fiskalna.limit_zwolnienia`
  (limit sprzedaży na rzecz osób fizycznych zwalniający z kasy rejestrującej, do końca 2027 r.).
- Zasada `zasada.zaliczki_zawieszenie` w `data/parameters/zaliczki.yaml`: zaliczki na PIT i ryczałt w okresie
  zawieszenia działalności i po jej wznowieniu.
- IP Box i ulga badawczo-rozwojowa w nowym pliku `data/parameters/ip_box_br.yaml` (skala i podatek liniowy):
  stawka `ip_box.stawka` (art. 30ca ust. 1), najwyższe procenty kosztów kwalifikowanych `ulga.br.odliczenie` (art. 26e ust. 7 pkt 3)
  oraz zasady `zasada.ip_box` i `zasada.ulga_br`.

### Zmienione

- `get_schema` przyjmuje symbol z łącznikiem albo podkreśleniem, wielkimi albo małymi literami
  (PIT-36L, pit_36l). Opis narzędzia wymienia wszystkie symbole, które mają dane, i dzień, według którego
  wybiera się wersję.
- Trzy poziomy pewności zamiast dwóch: `wysoka`, `średnia` i `niska`. `średnia` oznacza pełny komplet
  dowodów i otwarte pytanie tylko o przypadek brzegowy (`verification.open_issue_scope: edge_case`).
  Klient, który porównuje poziom z `niska`, musi obsłużyć nową wartość. Odpowiedź podaje też
  `confidence.open_issue_scope`.
- Drugie źródło wartości złożonej można potwierdzić pole po polu (`confirms` przy źródle).
  `confidence.unconfirmed_fields` wymienia pola, którym brakuje drugiego dokumentu.
- Sprawdzanie cytatów pomija znaki zerowej szerokości, którymi strony gov.pl dzielą nazwy plików.
- Kroki zasad, które przesądzały otwarte pytania P1, P8, P14 i P19, opisują je teraz jako niewyjaśnione;
  zasady o wspólnym opodatkowaniu wymieniają rezygnację korektą (P16) i kartę podatkową (P15).

## [0.3.0] - 2026-11-26

### Dodane

- Wersje na 2027 r.: prognozowane przeciętne wynagrodzenie i limit rocznej podstawy składek
  emerytalnej i rentowych (M.P. 2026 poz. 1098).
- Nowa wersja `zasada.przesuniecie_terminu` od 1 października 2026 r. (art. 12 § 5 Ordynacji
  podatkowej w brzmieniu z Dz.U. 2026 poz. 846), z otwartym pytaniem P5 o terminy zapłaty.

### Zmienione

- `wykryj_zmiany.py` pomija starsze teksty jednolite cytowane obok nowszego tekstu tej samej
  ustawy, pobiera metadane każdego aktu raz, a przejrzaną nowelizację można przypisać do jednego
  aktu (pole `for` w `data/zmiany_sprawdzone.yaml`); 18 przejrzanych nowelizacji.
- Treść danych po polsku, bez nazw pól w zdaniach; notatki tylko o zmianach widocznych dla klienta.
- README: instalacja z PyPI przez `uvx fikus@latest`, jaśniejsze logo.

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

[Niewydane]: https://github.com/tmierzwa/fikus/compare/v0.5.0...HEAD
[0.5.0]: https://github.com/tmierzwa/fikus/compare/v0.4.5...v0.5.0
[0.4.5]: https://github.com/tmierzwa/fikus/compare/v0.4.0...v0.4.5
[0.4.0]: https://github.com/tmierzwa/fikus/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/tmierzwa/fikus/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/tmierzwa/fikus/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/tmierzwa/fikus/releases/tag/v0.1.0

# Specyfikacja: parametry do ewidencji przychodów i deklaracji JDG

Stan: propozycja z 2026-11-26. Zgłasza ją pierwszy klient, Staffkey. Decyzję o zakresie podejmuje
opiekun w dokumencie projektowym.

Decyzje opiekuna (decyzja 25 w dokumencie projektowym, 2026-11-26):

- A6 (zakres usług według stawek ryczałtu) jest w zakresie.
- C3 obejmuje wzór formularza DRA (`schemat.zus_dra`). Schemat KEDU (`schemat.kedu`, z wersją specyfikacji
  EWD) doszedł później, w wersji 0.4.5, razem z deklaracją ZUS DRA za siebie.
- Obszar D (kanały wysyłki) jest poza zakresem.

## Cel

Staffkey prowadzi dla użytkownika ewidencję przychodów i przygotowuje deklaracje:

- ewidencję przychodów i plik JPK_EWP (ryczałt),
- zeznanie roczne PIT-36, PIT-36L i PIT-28,
- plik JPK_V7M,
- dokument ZUS DRA, także z rocznym rozliczeniem składki zdrowotnej.

Staffkey liczy sam. Od Fikusa potrzebuje wartości, terminów, wersji schematów i zasad opisanych
krokami z podstawą prawną. Ta specyfikacja wymienia, czego dziś w danych brakuje.

## Granice

- Specyfikacja nie zmienia zasad nadrzędnych z `CLAUDE.md`. Serwer nadal niczego nie liczy.
- Każdy nowy wpis powstaje według skilla `dodaj-parametr`. Wpis bez źródła pierwotnego nie trafia
  do danych.
- Wartości podane w tej specyfikacji pochodzą z wyszukiwania z 2026-11-26. Są tylko wskazówką,
  gdzie szukać. Wartość do danych bierzesz ze źródła pierwotnego.
- Kursy walut, numeracja wierszy, sumy kontrolne i treść plików XML to praca klienta. Fikus podaje
  tylko zasadę i wersję schematu.
- Jeden obszar to jeden PR. Kolejność PR-ów jest w części „Kolejność”.

## Obszar A: ewidencja przychodów (ryczałt)

### A1. `schemat.jpk_ewp`

- Rodzaj: `value`, tak jak `schemat.jpk_pkpir`.
- Dotyczy: `{tax_form: [ryczalt]}`.
- Wartość: `form`, `variant`, `system_code`, `schema_version`.
- Wskazówka: broszura MF o strukturze JPK_EWP(4) podaje wariant 4 od 1 stycznia 2026 r.
  Specyfikacja interfejsów usług JPK 5.6.0 wymienia JPK_EWP(3) i JPK_EWP(4).
- Źródła do sprawdzenia:
  - broszura MF o JPK_EWP(4) na podatki.gov.pl (pierwotne, tak jak przy JPK_PKPIR),
  - specyfikacja interfejsów usług JPK 5.6.0 z 10 września 2026 r. (wariant, bez wersji schematu).
- Kryterium odbioru: `get_schema("JPK_EWP", "2026-01-01")` zwraca wariant 4. Opis narzędzia i test
  w `tests/test_server.py` wymieniają JPK_EWP.

### A2. `termin.ewidencja_przychodow_wpis`

- Rodzaj: `deadline`.
- Dotyczy: `{tax_form: [ryczalt]}`.
- Treść: do którego dnia trzeba wpisać przychody za miesiąc do ewidencji.
- Wskazówka: portale podają 20. dzień następnego miesiąca i § 6 rozporządzenia o ewidencji
  przychodów. Za grudzień termin może być inny.
- Źródło do ustalenia: rozporządzenie ministra o prowadzeniu ewidencji przychodów i wykazu środków
  trwałych, obowiązujące od 1 stycznia 2026 r. Portale podają Dz.U. 2025 poz. 1294, ale numer
  i datę aktu trzeba potwierdzić w ELI.
- Kryterium odbioru: `deadlines(przyklad_ryczalt, 2026, 11)` zwraca ten termin obok
  `termin.zaliczka_ryczalt`.

### A3. `zasada.ewidencja_przychodow`

- Rodzaj: `rule`.
- Dotyczy: `{tax_form: [ryczalt]}`.
- Kroki, każdy z podstawą prawną:
  1. kto prowadzi ewidencję i za jaki okres (odrębnie za każdy rok podatkowy),
  2. jakie dane zawiera wpis według rozporządzenia,
  3. jakie dowody są podstawą wpisu, także faktura z KSeF i jej numer,
  4. jak wpisuje się korektę przychodu,
  5. kiedy ewidencja jest rzetelna i niewadliwa.
- Kroki 2 i 3 wymieniają dane słownie. Nie odwzorowują pól pliku XML. Pola opisuje broszura
  ze schematu A1.
- Wskazówka: portale podają, że od 2026 r. wpis może zawierać numer KSeF faktury. Trzeba to
  sprawdzić w rozporządzeniu.

### A4. `zasada.przychod_data_uzyskania`

- Rodzaj: `rule`.
- Dotyczy: wszystkich profili. Data przychodu jest potrzebna w ewidencji, w PKPiR i w zaliczkach.
- Treść: który dzień jest dniem uzyskania przychodu z działalności. Kroki mówią o dniu wydania
  rzeczy albo wykonania usługi, o dniu wystawienia faktury, o dniu zapłaty i o usługach
  rozliczanych w okresach.
- Źródło do sprawdzenia: art. 14 ust. 1c i 1e ustawy o PIT. Ustawa o ryczałcie odsyła do tych
  przepisów, a odesłanie trzeba wskazać w osobnym kroku.

### A5. `zasada.przychod_w_walucie`

- Rodzaj: `rule`.
- Dotyczy: wszystkich profili.
- Treść: który kurs NBP i z którego dnia stosuje się do przychodu w walucie obcej. Kroki opisują
  też różnice kursowe, jeśli dotyczą ryczałtu.
- Źródło do sprawdzenia: art. 11a ustawy o PIT.
- Fikus nie podaje kursów. Kurs pobiera klient z NBP.

### A6. Zakres usług według stawek ryczałtu

W zakresie (decyzja 25). W danych jest jako `ryczalt.zakres_uslug`.


- Staffkey musi przypisać stawkę do każdego przychodu. Dziś `ryczalt.stawki` podaje stawki według
  punktów art. 12 ust. 1, a zakres usług odsyła do przepisu.
- Propozycja: osobny parametr z dosłownym zakresem usług (symbole PKWiU) dla stawek, które
  dotyczą usług IT i inżynierskich.
- Ryzyko: wybór stawki dla konkretnego przychodu zbliża się do doradztwa (pytanie P0). Dlatego
  parametr podaje tylko brzmienie przepisu, a stawkę dla przychodu wybiera podatnik.

## Obszar B: zeznanie roczne PIT

### B1. `schemat.pit_36`, `schemat.pit_36l`, `schemat.pit_28`

- Rodzaj: `value`.
- Dotyczy: odpowiednio `skala`, `liniowy`, `ryczalt`.
- Wartość: `form`, `variant`, `schema_version` i adres schematu z wyróżnika wzoru, tak jak przy
  JPK_V7M.
- Dniem dla `get_schema` jest pierwszy dzień roku podatkowego, za który składa się zeznanie.
  To trzeba opisać w narzędziu tak jak dla JPK_V7M.
- Źródło do sprawdzenia: wyróżniki wzorów w CRWDE (ePUAP) i strona MF ze strukturami e-Deklaracji.
- Zmiana w serwerze: `get_schema` musi przyjąć symbol z łącznikiem. „PIT-36L” daje identyfikator
  `schemat.pit_36l`. Test sprawdza obie postacie.

### B2. `zasada.dane_autoryzujace`

- Rodzaj: `rule`.
- Dotyczy: wszystkich profili.
- Treść:
  1. jakie dane tworzą dane autoryzujące,
  2. z którego zeznania i za który rok bierze się kwotę przychodu,
  3. co robi podatnik, który takiego zeznania nie składał,
  4. których dokumentów nie można tak podpisać, także dokumentów pełnomocnika.
- Źródło do sprawdzenia: rozporządzenie ministra o sposobie przesyłania deklaracji i podań oraz
  o rodzajach podpisu elektronicznego, w tekście aktualnym.
- Ten sam sposób podpisu dotyczy JPK_V7M i JPK_EWP. Krok o zakresie dokumentów musi to objąć.

## Obszar C: ZUS DRA

### C1. `zasada.dra_obowiazek`

- Rodzaj: `rule`.
- Dotyczy: wszystkich profili.
- Treść: kto składa DRA za siebie, za który miesiąc i kiedy DRA nie trzeba składać. Osobny krok
  mówi o DRA za kwiecień z rocznym rozliczeniem składki zdrowotnej.
- Wskazówka: od 2022 r. osoby, które płacą składki tylko za siebie, nie mają już zwolnienia
  z comiesięcznego DRA. Tego nie potwierdziło źródło pierwotne.
- Źródło do sprawdzenia: art. 47 ustawy o systemie ubezpieczeń społecznych, w tekście jednolitym.
- Połączenie: `termin.zus` i `termin.roczne_rozliczenie_zdrowotnej` w polu `uses`.

### C2. `zasada.roczne_rozliczenie_zdrowotnej`

- Rodzaj: `rule`.
- Dotyczy: wszystkich profili z formami `skala`, `liniowy` i `ryczalt`.
- Treść: jaki dokument zawiera roczne rozliczenie, za który okres, jak rozlicza się nadpłatę
  i niedopłatę i kiedy rozliczenia nie ma.
- Uwaga: rok składkowy dla skali i liniowego trwa od 1 lutego do 31 stycznia (`HANDOFF.md`).
  Kroki muszą to uwzględnić.
- Źródło do sprawdzenia: art. 81 ustawy o świadczeniach opieki zdrowotnej (Dz.U. 2025 poz. 1461)
  i komunikaty ZUS o rocznym rozliczeniu.

### C3. `schemat.zus_dra` i `schemat.kedu`

- Rodzaj: `value`.
- Dotyczy: wszystkich profili.
- Wartość dla `schemat.zus_dra`: wersja wzoru formularza i data, od której obowiązuje.
- Wartość dla `schemat.kedu`: wersja specyfikacji wejścia-wyjścia EWD i wersja schematu KEDU.
- Wskazówka: ZUS podaje nowy wzór DRA od 1 maja 2026 r. (rozliczenia od kwietnia 2026 r.)
  i specyfikację EWD 2.27 ze schematem KEDU od 25 kwietnia 2026 r.
- Źródła do sprawdzenia:
  - komunikat ZUS o nowych wzorach DRA i RCA od 1 maja 2026 r.,
  - strona ZUS „Wymagania dla oprogramowania interfejsowego – dokumenty ubezpieczeniowe”,
  - rozporządzenie o wzorach dokumentów ubezpieczeniowych, jeśli wzór DRA ustala akt.
- Oba parametry są w danych: `schemat.zus_dra` i `schemat.kedu` (od wersji 0.4.5).

## Obszar D: kanały wysyłki (poza zakresem, decyzja 25)

- Propozycja: `schemat.jpk_api` (wersja specyfikacji interfejsów usług JPK) i
  `schemat.e_deklaracje_api` (wersja specyfikacji wejścia-wyjścia e-Deklaracji).
- Wskazówka: specyfikacja JPK 5.6.0 z 10 września 2026 r. i specyfikacja e-Deklaracji 2.4.
- Za: klient wie, kiedy MF zmienia interfejs, a `changes` to pokaże.
- Przeciw: to nie są przepisy, a Fikus zbiera przepisy. Adresów usług Fikus nie podaje.
- Obszar jest poza zakresem (decyzja 25).

## Zmiany w serwerze

1. `get_schema` przyjmuje symbole z łącznikiem i małe litery. Opis narzędzia wymienia wszystkie
   symbole, które mają dane.
2. `deadlines` zwraca `termin.ewidencja_przychodow_wpis` dla profili na ryczałcie.
3. Testy w `tests/test_server.py` obejmują nowe symbole i nowy termin.
4. `CHANGELOG.md` w sekcji „Niewydane” wymienia nowe parametry i zmianę w `get_schema`.

## Otwarte pytania do `docs/pytania-do-eksperta.md`

Pytania dopisujesz przy wpisie, którego dotyczą, z kolejnym numerem po P30.

- A2: czy termin wpisu za grudzień jest inny niż za pozostałe miesiące.
- A3: czy przychód na fakturze korygującej wpisuje się w dniu korekty czy w okresie pierwotnym.
- A4 i A5: którą datę stosuje ryczałtowiec, gdy faktura jest wystawiona przed wykonaniem usługi.
- C1: czy przy zawieszeniu działalności przez część miesiąca DRA składa się za ten miesiąc.
- P19 (już otwarte) dotyczy też A1. Pierwszy rok przesyłania JPK_EWP zależy od rozliczania VAT.

## Kolejność

1. Obszar A bez A6: ewidencja jest potrzebna jako pierwsza. Wpisy za 2026 r. trzeba robić już teraz.
2. Obszar C: DRA za każdy miesiąc i roczne rozliczenie do 20 maja 2027 r.
3. Obszar B: zeznania za 2026 r. od 15 lutego 2027 r.
4. A6 (w zakresie po decyzji 25). Obszar D jest poza zakresem.

## Kryteria odbioru całości

- Każdy nowy wpis przechodzi `python scripts/sprawdz_cytaty.py` i `python -m pytest -q`.
- Każdy nowy wpis ma raport `weryfikator-zrodel` bez niezgodności, zanim dostanie `agent_check`.
- Wpis bez drugiego niezależnego źródła ma `open_issue` i pewność niską. Staffkey pokazuje wtedy
  ostrzeżenie i nie wysyła deklaracji automatycznie.

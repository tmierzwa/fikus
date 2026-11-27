# Pytania do eksperta

Pytania, na które źródła nie dają jednoznacznej odpowiedzi. Opiekun przekazuje je doradcy podatkowemu
albo biuru rachunkowemu, a odpowiedź (imię, data, podstawa) trafia do pola `verification.expert`
wpisu. Do czasu odpowiedzi wpis ma `open_issue` i pewność niską albo, gdy pytanie dotyczy tylko
przypadku brzegowego, średnią.

## P0. Granica doradztwa podatkowego przed publicznym udostępnieniem

- Dotyczy: całego projektu (README, zasady w `data/parameters/zasady.yaml`, odpowiedzi serwera).
- Zgłoszone: 2026-11-26.
- Ustawa o doradztwie podatkowym (Dz.U. 2026 poz. 1274): czynności doradztwa obejmują udzielanie
  podatnikom „na ich zlecenie lub na ich rzecz, porad, opinii i wyjaśnień z zakresu ich obowiązków”
  (art. 2 ust. 1 pkt 1). Ich zawodowe wykonywanie jest zastrzeżone dla doradców podatkowych,
  adwokatów, radców prawnych i biegłych rewidentów (art. 2 ust. 2, art. 3 ust. 1), a naruszenie
  grozi grzywną (art. 81).
- Fikus publikuje dla wszystkich te same dane: wartości, terminy i zasady obliczeń opisane krokami
  z podstawą prawną. Nie odpowiada na pytania o sytuację konkretnego podatnika. Klienci (na przykład
  aplikacja, która liczy podatek dla użytkownika) mogą jednak używać tych danych do obliczeń dla
  konkretnej osoby.
- Pytania: czy publikowanie zasad obliczeń w tej formie może być uznane za czynność doradztwa
  podatkowego? Czy zastrzeżenie w README wystarcza? Czy coś trzeba zmienić w sposobie opisu zasad
  albo w odpowiedziach serwera?

## P1. Składka zdrowotna na ryczałcie według przychodu z poprzedniego roku: wyjątek przy ponownym podjęciu działalności

- Wpis: `zasada.ryczalt_zdrowotna_prog_poprzedni_rok` (od 2025-01-01), krok 4.
- Zgłoszone: 2026-11-26.
- Ustawa o świadczeniach opieki zdrowotnej, art. 81 ust. 2h: podstawę ustaloną według przychodu
  z poprzedniego roku stosuje się „przez cały rok kalendarzowy”.
- Poradnik ZUS „Polski Ład” (stan prawny na 1 stycznia 2025 r.): tak ustaloną podstawę stosuje się
  przez cały rok, „za wyjątkiem przypadków, w których zakończysz działalność gospodarczą, a następnie
  podejmiesz nową” (przykład 17).
- Pytanie: czy wyjątek z poradnika ZUS wynika z przepisu (którego?) i czy należy go dopisać do zasady?
- Przeszukane źródła publiczne (2026-11-26), bez rozstrzygnięcia:
  - Druk sejmowy nr 838 (10. kadencja), który uchylał art. 81 ust. 2b–2h: weto Prezydenta z 7 maja 2025 r.,
    bez ponownego uchwalenia. Ust. 2h obowiązuje (tekst jednolity Dz.U. 2025 poz. 1461).
  - Interpretacje indywidualne ZUS w BIP (https://bip.zus.pl/inne/interpretacje), kategorie „Podstawa
    wymiaru składek na ubezpieczenie zdrowotne” i „Składka na ubezpieczenie zdrowotne”, 358 decyzji
    z lat 2022–2026. Art. 81 ust. 2h omawia tylko DI/200000/43/1233/2023 (zmiana formy opodatkowania
    na ryczałt; podstawę stosuje się „przez cały rok”). Żadna decyzja nie dotyczy zakończenia
    i ponownego podjęcia działalności w ciągu roku.
  - FAQ ZUS („Zmiany od 2022 r.”): przy zawieszeniu działalności w poprzednim roku ust. 2h nie ma
    zastosowania. To przypadek pokrewny, nie ten z pytania.
  - Poradnik ZUS stawia przypis 21 („Art. 81 ust. 2h ustawy zdrowotnej”) po regule, że podstawę stosuje się „przez
    cały rok”, a przed wyjątkiem o zakończeniu działalności. Dla samego wyjątku nie podaje żadnej podstawy.
- Dalsze źródła przeszukane 2026-11-26, bez rozstrzygnięcia:
  - Prezes NFZ nie wydaje rozstrzygnięć w tej sprawie (wniosek z przepisów, nie cytat): w ustawie o świadczeniach
    (Dz.U. 2025 poz. 1461) art. 109 ust. 2 wyłącza z decyzji w indywidualnych sprawach sprawy z zakresu wymierzania
    i pobierania składek, a art. 109a ust. 2 wyłącza z interpretacji indywidualnych Prezesa NFZ sprawy składek należące
    do ZUS i KRUS (art. 83d ustawy o systemie ubezpieczeń społecznych, art. 62a ustawy o ubezpieczeniu społecznym rolników).
  - ZUS, ulotka „Ryczałt od przychodów ewidencjonowanych” (2022,
    https://www.zus.pl/documents/10182/4446388/Rycza%C5%82t.pdf/35fc43d1-637f-6933-9619-0833b896b0f5): podaje tylko
    warunek prowadzenia działalności „przez cały poprzedni rok kalendarzowy”, bez wyjątku z poradnika.
  - ZUS, bieżące wyjaśnienie komórek merytorycznych „Roczna podstawa wymiaru składki na ubezpieczenie zdrowotne osób
    prowadzących działalność gospodarczą” (17 lutego 2023 r.): nie omawia art. 81 ust. 2h.
  - Orzeczenia sądów powszechnych (baza SAOS, wyszukiwanie frazy „81 ust. 2h”): 8 wyroków z lat 2024–2026, wszystkie
    w sprawach podstawy składki komorników sądowych; przepis jest w nich tylko wymieniony. Żaden nie dotyczy
    zakończenia i ponownego podjęcia działalności. Sprawy składek rozpatrują sądy powszechne, nie administracyjne,
    więc CBOSA nie jest właściwą bazą.
  - Interpelacje poselskie (wyszukiwanie w sejm.gov.pl): brak odpowiedzi na to pytanie.

## P2. Minimalna składka zdrowotna na skali i liniowym w roku składkowym 2025/2026 (rozstrzygnięte 2026-11-26, bez eksperta)

- Rozstrzygnięcie: informacja ZUS na samorzad.gov.pl (18 lutego 2025 r.) sama podaje, że od lutego 2025 r. do stycznia 2026 r. składka nie może być niższa niż 314,96 zł; dodana jako źródło kontrolne, `open_issue` usunięty. Styczeń 2026 potwierdza też komunikat ZUS z 2026 r.

- Wpis: `zdrowotna.minimum` (2025-02-01 – 2026-01-31, 314,96 zł).
- Zgłoszone: 2026-11-26.
- Komunikat ZUS z 30 stycznia 2025 r. podaje 314,96 zł „za miesiące od lutego 2025 r. do stycznia 2026 r.”
  (9% z 3499,50 zł, czyli 75% minimalnego wynagrodzenia 4666 zł, art. 4 ustawy z 6 grudnia 2024 r.).
- Żadne niezależne źródło nie podaje tej kwoty za cały ten okres: komunikat ZUS z 2026 r. i ifirma
  podają ją tylko za styczeń 2026, a PITax podaje okres do grudnia 2026.
- Pytanie: czy minimalna miesięczna składka zdrowotna przedsiębiorcy na skali i na podatku liniowym
  wynosiła 314,96 zł za każdy miesiąc od lutego 2025 r. do stycznia 2026 r.?

## P3. Minimalna składka zdrowotna na skali i liniowym za styczeń 2027 (rozstrzygnięte 2026-11-26, bez eksperta)

- Rozstrzygnięcie: biznes.gov.pl sam podaje 432,54 zł za okres od 1 lutego 2026 r. do 31 stycznia 2027 r., tak jak komunikat ZUS z 2 lutego 2026 r.; dodany jako źródło kontrolne, `open_issue` usunięty.

- Wpis: `zdrowotna.minimum` (2026-02-01 – 2027-01-31, 432,54 zł).
- Zgłoszone: 2026-11-26.
- Komunikat ZUS z 2 lutego 2026 r. podaje 432,54 zł „za miesiące od lutego 2026 r. do stycznia 2027 r.”
  (9% z 4806 zł, art. 81 ust. 2d). Źródło kontrolne (ifirma) potwierdza kwotę tylko za luty–grudzień 2026.
- Pytanie: czy minimalna składka za styczeń 2027 r. (ostatni miesiąc roku składkowego) wynosi 432,54 zł,
  mimo że od 1 stycznia 2027 r. obowiązuje nowe minimalne wynagrodzenie?

## P4. Zryczałtowana stopa składki wypadkowej dla płatnika do 9 ubezpieczonych

- Wpis: `zus.stawka.wypadkowa_do_9` (2025-04-01 – 2026-03-31 i 2026-04-01 – 2027-03-31, 1,67%).
- Zgłoszone: 2026-11-26.
- Ustawa wypadkowa, art. 28 ust. 1: stopa wynosi 50% najwyższej stopy ustalonej na dany rok składkowy
  dla grup działalności. Najwyższa stopa w tabeli z załącznika nr 2 rozporządzenia (Dz.U. 2025
  poz. 1874) to 3,33, a § 6 ust. 2 każe zaokrąglać według zasady matematycznej. Kwotę 1,67% podają
  wprost materiały ZUS (poradnik i strona o informacji ZUS IWA), a za rok 2025/2026 także biznes.gov.pl, choć bez wskazania roku składkowego (niżej).
- Pytanie: czy dla płatnika zgłaszającego nie więcej niż 9 ubezpieczonych stopa w latach składkowych
  2025/2026 i 2026/2027 wynosi 1,67%, i czy istnieje urzędowe źródło poza materiałami ZUS, które
  podaje tę stopę wprost?

- Materiały znalezione 2026-11-26 (nie rozstrzygają pytania):
  - Za rok 2026/2027: przedruk wypowiedzi regionalnej rzeczniczki prasowej ZUS z 1 kwietnia 2026 r. na stronie Starostwa
    Powiatowego w Hajnówce (https://samorzad.gov.pl/web/powiat-hajnowski/stopy-procentowe) podaje 1,67% i najwyższą stopę
    3,33% od 1 kwietnia 2026 r. To nadal materiał ZUS, nie źródło spoza ZUS.
  - Za rok 2025/2026: biznes.gov.pl (https://www.biznes.gov.pl/pl/portal/00274, aktualizacja 11 lutego 2026 r.) podaje
    „Składka wypadkowa od 1.04.2024 (1,67%)”, ale nie wskazuje roku składkowego, a na tej samej stronie podaje też stopę
    „od 1.04.2021”.

## P5. Przesunięcie terminu z art. 12 § 5 Ordynacji podatkowej od 1 października 2026 r. a termin zapłaty

- Wpis: `zasada.przesuniecie_terminu` (od 2026-10-01).
- Zgłoszone: 2026-11-26.
- Ustawa z 29 maja 2026 r. (Dz.U. 2026 poz. 846, art. 1 pkt 1) zmienia art. 12 § 5: przesunięcie dotyczy „ostatniego
  dnia terminu do wykonania czynności”. Wchodzi w życie 1 października 2026 r. (art. 35).
- Uzasadnienie projektu (druk sejmowy nr 2287, https://api.sejm.gov.pl/sejm/term10/prints/2287/2287-uzasadnienie.docx, str. 7–8): przepis ma nie przesuwać końca terminu przedawnienia i „powinien mieć
  zastosowanie tylko do terminów dotyczących wykonania czynności np. złożenia deklaracji czy wniesienia odwołania”.
- Pytanie: czy termin zapłaty podatku (np. zaliczki, VAT) jest „terminem do wykonania czynności” w rozumieniu nowego
  art. 12 § 5? Czy tak samo jest z terminem opłacenia składek ZUS, do których art. 12 stosuje się odpowiednio
  (art. 31 ustawy o systemie ubezpieczeń społecznych)?
- Przeszukane źródła urzędowe (2026-11-26), bez rozstrzygnięcia:
  - Zestawienie uwag z konsultacji dołączone do druku nr 2287 (stanowisko MF): przepis ma odnosić się „tylko do terminów
    do wykonania czynności np. złożenie deklaracji czy wniesienie odwołania”; o terminie zapłaty nie ma mowy. Uzasadnienie
    dodaje tylko, że nowe brzmienie nadal obejmuje termin z art. 150 (fikcja doręczenia).
  - Sprawozdanie Komisji Finansów Publicznych (druk nr 2480), stenogram posiedzenia Sejmu z 12 maja 2026 r., zapis posiedzenia
    Komisji Finansów Publicznych nr 270, uchwała Senatu (druk nr 2587), opinia Biura Legislacyjnego Senatu do druku senackiego nr 721 (20 maja
    2026 r., https://www.senat.gov.pl/download/gfx/senat/pl/senatekspertyzy/7945/plik/721o.pdf) i sprawozdanie komisji
    senackiej (druk nr 721 A): żaden z nich nie omawia terminu zapłaty w art. 12 § 5.
  - Informacja prawna KIS za 22–26 czerwca 2026 r. (https://www.gov.pl/attachment/42efbcdb-a097-46be-9b93-f93c0faa3238)
    powtarza tylko opis zmiany z uzasadnienia.
  - Nie znaleziono objaśnień podatkowych, interpretacji ogólnej ani komunikatu MF, KAS lub ZUS o terminach zapłaty po
    1 października 2026 r. Strona ZUS „Termin składania dokumentów i opłacania składek” przesuwa termin opłacenia składek
    na następny dzień roboczy, ale powołuje ustawę w brzmieniu z Dz.U. 2021 poz. 423, więc nie dotyczy nowego brzmienia.
  - Materiał dla eksperta (nie rozstrzyga): kalendarz przedsiębiorcy na biznes.gov.pl (https://www.biznes.gov.pl/pl/portal/005105,
    aktualizacja 16.11.2026) podaje terminy zapłaty przesunięte z dni wolnych w listopadzie 2026 r.: kartę podatkową za
    październik do 9 listopada, podatek od nieruchomości i składki ZUS płatników z osobowością prawną do 16 listopada.
    Kalendarz Rzecznika MŚP (https://rzecznikmsp.gov.pl/kalendarz-przedsiebiorcy/) przesuwa składki ZUS płatników
    z osobowością prawną na 16 listopada 2026 r., bo „15. dzień miesiąca przypada na niedzielę”. Żadna z tych stron nie
    podaje przepisu, na podstawie którego przesuwa termin zapłaty.

## P6. Stawka ryczałtu bez ewidencji pozwalającej ustalić przychody z każdego rodzaju działalności

- Wpis: `zasada.ryczalt_podstawa` (od 2024-01-01), krok o stawce bez takiej ewidencji.
- Zgłoszone: 2026-11-26.
- Ustawa o zryczałtowanym podatku dochodowym (Dz.U. 2025 poz. 843), art. 12 ust. 3 zdanie drugie: gdy
  ewidencja nie pozwala ustalić przychodów z każdego rodzaju działalności, „ryczałt od przychodów
  ewidencjonowanych wynosi 8,5 % przychodów, z tym że w przypadku osiągania również przychodów”
  z ust. 1 pkt 1, 2, 2a, 2b, 3 albo 4 wynosi odpowiednio 17, 15, 14, 12, 10 albo 12,5%.
- Pytania: czy stawkę podwyższoną stosuje się do wszystkich przychodów, czy tylko do przychodów z danego
  punktu? Którą stawkę stosuje się, gdy podatnik ma przychody z kilku z tych punktów?
- Przeszukane źródła urzędowe (2026-11-26), bez rozstrzygnięcia: wyszukiwarka MF Eureka (eureka.mf.gov.pl) nie ma
  objaśnień podatkowych ani interpretacji ogólnej o art. 12 ust. 3; strona MF „Opodatkowanie ryczałtem od przychodów
  ewidencjonowanych” (podatki.gov.pl, aktualizacja 26.11.2026) tego nie omawia.
- Materiał dla eksperta: biznes.gov.pl, „Ryczałt od przychodów ewidencjonowanych” (https://www.biznes.gov.pl/pl/portal/00263,
  aktualizacja 07.01.2026) podaje, że bez takiej ewidencji „Organ podatkowy przypisze te przychody do stawki 8,5% zamiast
  do stawek niższych” oraz: „Zasady tej sankcji nie stosuje się do przychodów, dla których stawka ryczałtu jest wyższa niż
  8,5%”. Według tej strony stawkę podwyższoną stosuje się więc tylko do przychodów z danego punktu. Portal nie jest
  objaśnieniem podatkowym MF, więc nie rozstrzyga pytania.

## P7. Minimum rocznej składki zdrowotnej przy podatku liniowym: liczba miesięcy

- Wpis: `zasada.liniowy_zdrowotna` (wersje od 2025-02-01, od 2026-02-01 i od 2027-02-01), krok o rocznej składce.
- Zgłoszone: 2026-11-26.
- Ustawa o świadczeniach opieki zdrowotnej (Dz.U. 2025 poz. 1461), art. 79a ust. 1 pkt 2: roczna składka nie mniej niż 9%
  „iloczynu liczby miesięcy w roku składkowym, o którym mowa w art. 81 ust. 2, i minimalnego wynagrodzenia”. Art. 81 ust. 2b
  dla minimalnej rocznej podstawy liczy natomiast miesiące podlegania ubezpieczeniu w roku kalendarzowym.
- Poradnik ZUS „Polski Ład” (stan prawny na 1 stycznia 2025 r.) w przykładzie rocznej składki przy podatku liniowym liczy
  minimum od liczby miesięcy podlegania ubezpieczeniu.
- Pytanie: czy minimum rocznej składki z art. 79a ust. 1 pkt 2 liczy się od wszystkich miesięcy roku składkowego, czy tylko
  od miesięcy podlegania ubezpieczeniu zdrowotnemu?
- Materiały zebrane 2026-11-26 (urzędowe źródła się różnią, więc pytanie zostaje otwarte):
  - ZUS, bieżące wyjaśnienie komórek merytorycznych „Roczna podstawa wymiaru składki na ubezpieczenie zdrowotne osób
    prowadzących działalność gospodarczą” (17 lutego 2023 r.,
    https://www.zus.pl/-/roczna-podstawa-wymiaru-sk%C5%82adki-na-ubezpieczenie-zdrowotne-os%C3%B3b-prowadz%C4%85cych-dzia%C5%82alno%C5%9B%C4%87-gospodarcz%C4%85):
    „Składka ustalana od podstawy rocznej nie może być niższa niż kwota równa 9% iloczynu liczby miesięcy podlegania
    ubezpieczeniu zdrowotnemu i minimalnego wynagrodzenia obowiązującego w pierwszym dniu roku składkowego.”
  - ZUS, „Zmiany w składce zdrowotnej opłacanej przez przedsiębiorców od 1 stycznia 2025 r.” (2 stycznia 2025 r.,
    https://www.zus.pl/-/zmiany-w-sk%C5%82adce-zdrowotnej-op%C5%82acanej-przez-przedsi%C4%99biorc%C3%B3w-od-1-stycznia-2025-r.):
    minimalna roczna podstawa to iloczyn „liczby miesięcy podlegania ubezpieczeniu zdrowotnemu w roku 2025” i 75%
    minimalnego wynagrodzenia, a przy podatku liniowym minimalna składka miesięczna i roczna to 9% minimalnej podstawy
    wymiaru. Dotyczy tylko roku składkowego 2025/2026.
  - ZUS, prezentacja z webinaru „Roczne rozliczenie składki na ubezpieczenie zdrowotne” (17 kwietnia 2023 r.,
    https://www.zus.pl/documents/10182/24154/Webinar_prezentacja+17.04.2023+r.pdf/f8f3baa7-94bf-3c98-a085-84ce230e75b9,
    str. 27–28): przy zmianie formy opodatkowania z ryczałtu na zasady ogólne od 1 stycznia 2023 r. (i przy rozpoczęciu
    działalności 1 stycznia 2023 r.) styczeń 2023 r. zalicza się do „jednomiesięcznego roku składkowego”, a dla skali albo
    podatku liniowego składka roczna za ten okres „będzie obliczona w wysokości 0 zł”.
  - biznes.gov.pl, „Ile wynosi składka zdrowotna” (https://www.biznes.gov.pl/pl/portal/001052): powtarza brzmienie ustawy:
    „Minimalna roczna składka zdrowotna to 9% iloczynu liczby miesięcy w roku składkowym i kwoty minimalnego wynagrodzenia
    obowiązującego w pierwszym dniu roku składkowego”, z przykładem tylko dla pełnego roku składkowego.
  - Historia przepisów: art. 79a ust. 1 pkt 2 w obecnym brzmieniu („liczby miesięcy w roku składkowym”) pochodzi z ustawy
    z 29 października 2021 r. (Dz.U. 2021 poz. 2105, art. 15). Ta sama ustawa nadała art. 81 ust. 2b brzmienie „liczby miesięcy
    w roku składkowym podlegania ubezpieczeniu”. Ustawa z 9 czerwca 2022 r. (Dz.U. 2022 poz. 1265, art. 10 pkt 6) zmieniła je na „liczby
    miesięcy podlegania ubezpieczeniu zdrowotnemu w roku kalendarzowym”, a art. 79a ust. 1 pkt 2 zostawiła bez zmian.
    Uzasadnienie projektu (druk sejmowy nr 2186, IX kadencja,
    https://api.sejm.gov.pl/sejm/term9/prints/2186/2186-uzas.docx) mówi o zmianie art. 81 ust. 2b: ma ona „usunięcie
    wątpliwości w zakresie ustalania liczby miesięcy podlegania dla celów określenia minimalnej rocznej podstawy wymiaru
    składki”. O art. 79a uzasadnienie nie mówi.
  - Orzeczenia sądów powszechnych (baza SAOS, fraza „liczby miesięcy w roku składkowym”): 31 wyroków z lat 2023–2025,
    głównie w sprawach komorników sądowych. Przytaczają art. 79a ust. 1, ale żaden nie rozstrzyga, którą liczbę miesięcy
    przyjąć.

## P8. Od kiedy stosować art. 81 ust. 2zd pkt 2 bez art. 21 ust. 1 pkt 63a ustawy o PIT

- Wpisy, których dotyczy wątpliwość:
  - `zasada.ryczalt_zdrowotna_prog`, wersja od 2025-01-01 (roczne rozliczenie za 2026 r.);
  - `zasada.ryczalt_zdrowotna_prog_poprzedni_rok`, wersja od 2027-01-01 (przychód z 2026 r. przyjmowany w 2027 r.);
  - `zasada.liniowy_zdrowotna` i `zasada.skala_zdrowotna`, wersje od 2026-02-01 (składka za styczeń 2027 r. i roczne
    rozliczenie roku składkowego 2026/2027); te zasady są w osobnych PR.
- Nowe brzmienie jest w wersjach od 2027-01-01 (ryczałt) i od 2027-02-01 (liniowy, skala). Kroki tych wersji przepisują
  ustawę dosłownie; odpowiedź na dodatkowe pytanie niżej może jednak wymagać w nich zastrzeżenia.
- Zgłoszone: 2026-11-26.
- Ustawa z 22 października 2026 r. (Dz.U. 2026 poz. 1542) w art. 12 skreśla w art. 81 ust. 2zd pkt 2 ustawy
  o świadczeniach wyrazy „63a,”, a w art. 4 pkt 1 uchyla art. 21 ust. 1 pkt 63a ustawy o PIT. Wchodzi w życie
  1 stycznia 2027 r. (art. 30). Nie ma przepisu przejściowego dla art. 81 ust. 2zd. Art. 26 i 27 tej ustawy dotyczą
  decyzji o wsparciu i pomocy publicznej ze stref ekonomicznych. Art. 27 ust. 1 („Do spraw związanych z przyznaną pomocą
  publiczną wynikających z ustawy uchylanej w art. 29 stosuje się przepisy dotychczasowe”) wchodzi w życie dopiero
  31 grudnia 2027 r., a pkt 63a znika 1 stycznia 2027 r.
- Dodatkowe pytanie: czy przychody objęte dotychczasowymi zezwoleniami strefowymi mogą po 1 stycznia 2027 r. nadal być
  zwolnione, a więc po skreśleniu „63a,” w art. 81 ust. 2zd pkt 2 przestają się liczyć do podstawy składki?
- Pytania: czy nowe brzmienie art. 81 ust. 2zd pkt 2 stosuje się do przychodów i dochodów osiągniętych od 1 stycznia
  2027 r., czy do każdej podstawy ustalanej po tym dniu? Dotyczy to na przykład:
  - składki za styczeń 2027 r. liczonej od dochodu z grudnia 2026 r. (skala, liniowy);
  - rocznego rozliczenia za 2026 r. składanego w 2027 r.;
  - przychodu z 2026 r. przyjmowanego na ryczałcie według art. 81 ust. 2h.
- Materiały zebrane 2026-11-26 (żadne urzędowe źródło nie podaje odpowiedzi):
  - Uzasadnienie projektu (druk sejmowy nr 3160, X kadencja,
    https://api.sejm.gov.pl/sejm/term10/prints/3160/3160-uzasadnienie.docx) omawia art. 12 projektu (ten sam numer w ustawie)
    razem z innymi artykułami jednym zdaniem: „Zaproponowane zmiany związane są z wygaszeniem z dniem 1 stycznia 2027 r.
    funkcjonowania SSE, co powoduje konieczność aktualizacji przepisów wymienionych ustaw.” O uchyleniu art. 21 ust. 1 pkt 63a
    ustawy o PIT pisze, że po wygaszeniu SSE „brak będzie możliwości korzystania ze zwolnienia w ramach tego przepisu”.
    O tym, od kiedy stosować nowe brzmienie art. 81 ust. 2zd, uzasadnienie nie mówi. Ocena skutków regulacji (druk 3160,
    pkt 6) podaje w tabeli dochody NFZ od roku 1 po wejściu w życie, ale nie omawia art. 81 ust. 2zd ani okresu, od którego
    zmiana ma wpływać na składkę.
  - Senat przyjął ustawę bez poprawek 27 października 2026 r. (druk senacki nr 892). Na stronie posiedzenia z materiałów Biura
    Legislacyjnego jest tylko materiał porównawczy (892m); opinii Biura Legislacyjnego do tej ustawy nie znaleziono.
  - Komunikatów ZUS, MZ i MF o stosowaniu nowego brzmienia nie znaleziono (ustawa ogłoszona 23 listopada 2026 r.).
  - Dla porównania: przy poprzedniej zmianie art. 81 ust. 2zd ustawa z 6 grudnia 2024 r. (Dz.U. 2024 poz. 1915) miała przepisy
    przejściowe. Art. 2: nowe brzmienie art. 81 ust. 2zd pkt 3 (i inne wymienione przepisy) przy skali, liniowym i IP Box
    „stosuje się do rozliczenia składek na ubezpieczenie zdrowotne należnych za okres od dnia 1 lutego 2025 r.”; art. 3:
    do składek na ryczałcie należnych za okres do 31 grudnia 2024 r. stosuje się przepisy dotychczasowe. Ustawa Dz.U. 2026
    poz. 1542 takich przepisów nie ma.

## P9. Ulga na start: jak liczyć 6 miesięcy ulgi i następne 24 miesiące podstawy preferencyjnej

- Wpis: `zasada.ulga_na_start` (od 2026-01-01), kroki 3, 5 i 6; `zus.ulga_na_start.okres`.
- Zgłoszone: 2026-11-26.
- Prawo przedsiębiorców (Dz.U. 2026 poz. 1484), art. 18 ust. 1: przedsiębiorca „nie podlega obowiązkowym
  ubezpieczeniom społecznym przez okres 6 miesięcy od dnia podjęcia działalności gospodarczej”.
- ZUS (wyjaśnienie „Ulga na start, preferencyjna podstawa, działalność nieewidencjonowana”) i biznes.gov.pl
  (https://www.biznes.gov.pl/pl/portal/00285): jeżeli działalność zaczyna się w trakcie miesiąca, tego miesiąca
  nie wlicza się do 6 miesięcy, więc ulga trwa do końca szóstego pełnego miesiąca kalendarzowego.
- Pytanie: czy okres z art. 18 ust. 1 kończy się z upływem 6 miesięcy od dnia podjęcia działalności, czy z końcem
  szóstego pełnego miesiąca kalendarzowego, jak podaje ZUS? Na jakiej podstawie?
- Ustawa o systemie ubezpieczeń społecznych (Dz.U. 2026 poz. 1474), art. 18aa ust. 1 i 3: po rezygnacji z ulgi albo
  po jej upływie okres 24 miesięcy kalendarzowych podstawy preferencyjnej liczy się „od dnia objęcia ubezpieczeniami”.
- biznes.gov.pl (portal/00285): po rezygnacji z ulgi w połowie miesiąca okres obniżonych składek zaczyna się „dopiero od
  kolejnego miesiąca”. ZUS liczy tak samo (zobacz materiały niżej). Przepis wprost nie mówi, jak liczyć
  miesiąc, w którym objęcie ubezpieczeniami następuje w trakcie miesiąca.
- Pytanie: jak liczyć 24 miesiące z art. 18aa ust. 1 i 3, gdy objęcie ubezpieczeniami następuje w trakcie miesiąca?
- Materiały znalezione 2026-11-26 (nie rozstrzygają pytania, bo przepisy nie mówią wprost, jak liczyć niepełny miesiąc):
  - ZUS, bieżące wyjaśnienie komórek merytorycznych „Zmiany w ubezpieczeniach wprowadzone przez »Konstytucję biznesu«”
    (12 kwietnia 2018 r.,
    https://www.zus.pl/baza-wiedzy/biezace-wyjasnienia-komorek-merytorycznych/-/asset_publisher/biezacewyjasnieniakomorekmerytorycznych/content/id/1540038):
    ulga trwa „maksymalnie 6 miesięcy kalendarzowych”, miesiąca rozpoczęcia działalności w trakcie miesiąca nie wlicza się;
    tak samo dla 24 miesięcy: „Jeśli przypada w trakcie miesiąca kalendarzowego, miesiąca tego nie wliczaj.” Przykład
    w obecnej informacji ZUS o uldze na start (rezygnacja i objęcie ubezpieczeniami w trakcie miesiąca) daje ten sam wynik.
    ZUS i biznes.gov.pl liczą więc oba okresy tak samo.
  - Uzasadnienie projektu Prawa przedsiębiorców (druk sejmowy VIII kadencji nr 2051, https://api.sejm.gov.pl/sejm/term8/prints/2051/2051-uzas.docx):
    okres 6 miesięcy „powinien być liczony od momentu podjęcia” działalności, czyli od pierwszej czynności w obrocie
    gospodarczym. O pełnych miesiącach uzasadnienie nie mówi. Uzasadnienie przepisów wprowadzających (druk nr 2055)
    nie mówi, jak liczyć 24 miesiące z art. 18aa.
  - Wyrok SN z 27 kwietnia 2023 r., III USKP 34/22 (znany z omówienia w „Rachunkowości”,
    https://rachunkowosc.com.pl/jak-zus-liczy-miesiace-przy-uldze-na-start; pełnego tekstu nie udało się pobrać ze strony SN):
    60 miesięcy przerwy z art. 18 ust. 1 Prawa przedsiębiorców to nie miesiące kalendarzowe, bo przepis, inaczej niż art. 18a
    ustawy o systemie ubezpieczeń społecznych, nie dodaje słowa „kalendarzowych”; okres liczy się według art. 57 Kpa.
    Wyrok dotyczy okresu przerwy, nie 6 miesięcy ulgi, ale ten sam przepis mówi o „okresie 6 miesięcy” bez słowa
    „kalendarzowych”.
  - Niesprawdzone: interpretacje indywidualne ZUS w BIP (wyszukiwarka https://bip.zus.pl/inne/interpretacje nie daje
    wyników bez formularza, a archiwa są w plikach RAR), pismo Centrali ZUS DI/100000/43/164/2022 (dostępne tylko w LEX),
    artykuł „Ulga na start – krytyczna analiza instytucji z art. 18 ustawy Prawo przedsiębiorców” (Palestra 4/2020).

## P10. Mały ZUS Plus: skutek zgłoszenia po terminie i liczenie okresów od 2026 r.

- Wpis: `zasada.maly_zus_plus` (od 2026-01-01), kroki 3, 4 i ostatni.
- Zgłoszone: 2026-11-26.
- Ustawa o systemie ubezpieczeń społecznych (Dz.U. 2026 poz. 1474), art. 36 ust. 4b i 14a: zgłoszenie do ubezpieczeń
  (albo wyrejestrowanie i ponowne zgłoszenie przy zmianie tytułu ubezpieczenia) do końca stycznia, a w innych
  przypadkach w ciągu 7 dni. Przepisy nie mówią, co oznacza zgłoszenie po terminie.
- ZUS („Mały ZUS plus” – nowe zasady od 2026 r., 22 grudnia 2025 r.): bez zgłoszenia w terminie ZUS uznaje, że
  przedsiębiorca zrezygnował z ulgi. biznes.gov.pl (https://www.biznes.gov.pl/pl/portal/00284): bez dokumentów
  w terminie z ulgi nie można skorzystać przez cały rok.
- Pytanie: czy zgłoszenie po terminie z art. 36 ust. 4b lub 14a wyłącza prawo do Małego ZUS Plus do końca roku
  kalendarzowego? Z jakiego przepisu to wynika?
- Ustawa z 21 maja 2025 r. (Dz.U. 2025 poz. 769) od 1 stycznia 2026 r. zastąpiła art. 18c ust. 11 pkt 6 przepisami
  ust. 11a–11c (36 miesięcy w każdym okresie 60 miesięcy; pierwszy okres zaczyna się od pierwszego miesiąca, w którym
  podstawę ustalono według art. 18c). Przepisu przejściowego o miesiącach sprzed 2026 r. nie ma; art. 38 tej ustawy
  dotyczy tylko dodatkowych 12 miesięcy z art. 112a.
- ZUS (ta sama informacja z 22 grudnia 2025 r.) i biznes.gov.pl: od stycznia 2026 r. przysługuje 36 miesięcy ulgi
  „niezależnie od tego, czy wykorzystałeś ją przed 2026 rokiem”. Sam ZUS dodaje, że niewykorzystane dodatkowe
  miesiące z art. 112a można wykorzystać dopiero po upływie 36 miesięcy; biznes.gov.pl podaje tylko, że można je
  wykorzystać po 2025 r.
- Pytania: czy miesiące korzystania z ulgi i prowadzenia działalności sprzed 1 stycznia 2026 r. wlicza się do okresów
  36 i 60 miesięcy z art. 18c ust. 11a–11c? Jak dodatkowe 12 miesięcy z art. 112a mają się do limitu 36 miesięcy?
- Materiały znalezione 2026-11-26 (nie rozstrzygają pytań, bo źródła się różnią):
  - Uzasadnienie rządowego projektu (druk sejmowy X kadencji nr 1108, https://api.sejm.gov.pl/sejm/term10/prints/1108/1108-uzasadnienie.docx,
    część o ustawie o systemie ubezpieczeń społecznych): po 36 miesiącach ulgi następuje „karencja” 24 miesięcy, a nowe
    ust. 11a–11c, przy planowanym w projekcie wejściu w życie 1 stycznia 2025 r., „znajdą zastosowanie zarówno do osób,
    które już w przeszłości skorzystały z Małego ZUS Plus (i znajdują się obecnie w okresie »karencji«), jak i tych, które
    są w trakcie korzystania z niego”. To sugeruje, że okresy liczy się także z miesięcy sprzed wejścia w życie, inaczej niż
    podają ZUS i biznes.gov.pl („niezależnie od tego, czy wykorzystałeś ją przed 2026 rokiem”). Uchwalona ustawa wchodzi
    w tej części w życie 1 stycznia 2026 r. (art. 48 pkt 1). Uzasadnienie art. 38 mówi tylko, że do praw z art. 112a stosuje
    się dotychczasowy art. 18c ust. 11 pkt 6.
  - Zgłoszenie po terminie: wyrok SN z 24 kwietnia 2024 r., III USKP 47/23 (znany z tezy w INFORLEX; pełnego tekstu nie udało
    się pobrać): złożenie po terminie deklaracji rozliczeniowej uprawniającej do ulgi uniemożliwia skorzystanie z niej.
    Sprawa dotyczyła deklaracji za luty 2020 r., czyli przepisów sprzed 2026 r. i terminu deklaracji, a nie zgłoszenia
    z art. 36 ust. 4b lub 14a. Niesprawdzone: wyroki sądów okręgowych i apelacyjnych w Portalu Orzeczeń Sądów Powszechnych.

## P11. Jak długo podatnik jest „rozpoczynającym działalność” przy zaliczkach kwartalnych PIT i kwartalnym ryczałcie

- Wpisy: `zasada.zaliczki_kwartalne_pit` (od 2026-01-01), krok 2; `zasada.ryczalt_kwartalnie` (od 2026-01-01), krok 2.
- Zgłoszone: 2026-11-26.
- Ustawa o PIT (Dz.U. 2026 poz. 592), art. 44 ust. 3g: zaliczki kwartalne mogą wpłacać mali podatnicy oraz
  „podatnicy rozpoczynający prowadzenie działalności gospodarczej, o których mowa w art. 22k ust. 11”; ust. 3h (podatek
  liniowy) mówi o „podatnicy rozpoczynający prowadzenie działalności gospodarczej” i każe stosować art. 22k ust. 11
  odpowiednio. Art. 22k ust. 11 wyłącza z ulgi z ust. 7 podatnika, który prowadził działalność w roku rozpoczęcia albo
  w dwóch latach przed nim; nie określa, kto jest rozpoczynającym. Art. 22k ust. 7 mówi o roku podatkowym, w którym
  podatnik rozpoczął działalność.
- Ustawa o ryczałcie (Dz.U. 2025 poz. 843), art. 21 ust. 1b: kwartalnie mogą płacić „podatnicy rozpoczynający
  prowadzenie działalności, o których mowa w art. 7”; art. 7 ust. 1 dotyczy podatników rozpoczynających działalność
  w roku podatkowym, którzy w poprzednim roku jej nie prowadzili.
- Strony MF (podatki.gov.pl) i biznes.gov.pl piszą tylko „rozpoczynasz prowadzenie działalności”.
- Pytanie: czy prawo rozpoczynającego działalność do zaliczek kwartalnych (PIT) i do kwartalnego ryczałtu dotyczy tylko
  roku podatkowego, w którym rozpoczął działalność?
- Przeszukane źródła urzędowe (2026-11-26), bez rozstrzygnięcia:
  - Objaśnienia podatkowe MF z 27 września 2019 r. o wyborze formy opodatkowania i sposobu wpłacania zaliczek
    (https://www.gov.pl/attachment/92eafef0-5159-42a7-be45-95a802efbd05), część V: zaliczki kwartalne może wybrać
    podatnik „spełniający definicję małego podatnika albo rozpoczynający działalność”, a od 1 stycznia 2019 r.
    „z kwartalnego sposobu wpłacania ryczałtu mogą korzystać podatnicy rozpoczynający prowadzenie działalności”.
    Objaśnienia nie mówią, jak długo trwa ten status.
  - Strona MF o ryczałcie (podatki.gov.pl, aktualizacja 26.11.2026) nadal podaje tylko warunek „rozpoczynasz
    prowadzenie działalności gospodarczej”.
  - Eureka: brak interpretacji ogólnej w tej sprawie.

## P12. Zaliczki uproszczone, gdy w roku poprzedzającym nie złożono zeznania PIT z działalności

- Wpis: `zasada.zaliczki_uproszczone` (od 2026-01-01), krok 2.
- Zgłoszone: 2026-11-26.
- Ustawa o PIT (Dz.U. 2026 poz. 592), art. 44 ust. 6b: podstawą zaliczek uproszczonych jest dochód z działalności
  wykazany w zeznaniu z art. 45 ust. 1 albo ust. 1a pkt 2 złożonym w roku poprzedzającym (pkt 1), a zeznanie sprzed
  dwóch lat (pkt 2) – „jeżeli w zeznaniu, o którym mowa w pkt 1, podatnicy nie wykazali dochodu” z działalności albo
  wykazali dochód nie wyższy od ilorazu kwoty zmniejszającej podatek i najniższej stawki skali.
- Przepis nie mówi, co gdy w roku poprzedzającym podatnik w ogóle nie złożył takiego zeznania (na przykład rozliczał
  się ryczałtem i składał inne zeznanie), ani gdy nie złożył go dwa lata wcześniej.
- Pytanie: czy w takim przypadku podatnik może wpłacać zaliczki uproszczone na podstawie zeznania sprzed dwóch lat,
  czy zaliczki uproszczone nie są dla niego dostępne?
- Przeszukane źródła urzędowe (2026-11-26), bez rozstrzygnięcia: Eureka nie ma objaśnień podatkowych ani
  interpretacji ogólnej o art. 44 ust. 6b; objaśnienia MF z 27 września 2019 r. (część V) dotyczą tylko informowania
  o wyborze zaliczek uproszczonych w zeznaniu. Sam art. 44 ust. 6b rozstrzyga tylko przypadek, w którym w obu
  zeznaniach nie wykazano dochodu albo wykazano dochód nieprzekraczający ilorazu („nie są możliwe wpłaty zaliczek
  w uproszczonej formie”), a nie przypadek braku zeznania.

## P13. Limit odliczenia darowizn na ryczałcie: od jakiej kwoty przychodu

- Wpis: `ulga.darowizny.limit_ryczalt` (od 2026-01-01).
- Zgłoszone: 2026-11-26.
- Ustawa o zryczałtowanym podatku dochodowym (Dz.U. 2025 poz. 843), art. 11 ust. 1: darowizny z art. 26 ust. 1
  pkt 9 ustawy o PIT odlicza się od przychodów; art. 11 ust. 2: art. 26 ust. 5 ustawy o PIT stosuje się odpowiednio.
- Ustawa o PIT (Dz.U. 2026 poz. 592), art. 26 ust. 5: łączna kwota odliczeń darowizn nie może przekroczyć
  „kwoty stanowiącej 6 % dochodu”.
- Strona MF „Darowizny na cele pożytku publicznego PIT” (aktualizacja 6.10.2026): „nie więcej jednak niż 6% Twojego
  dochodu (przychodu)”, bez wskazania, o jaki przychód chodzi.
- Pytanie: czy na ryczałcie limit 6% liczy się od przychodu przed odliczeniami z art. 11 ust. 1 i 1a (składki,
  inne ulgi), czy od przychodu po tych odliczeniach? Czy przy przychodach opodatkowanych różnymi stawkami limit
  liczy się od łącznego przychodu?
- Przeszukane źródła urzędowe (2026-11-26), bez rozstrzygnięcia:
  - Broszura informacyjna MF do PIT/O za 2025 r. (https://www.podatki.gov.pl/media/z5abnlba/pit-o-broszura-za-2025-r.pdf):
    limit to „6% Twojego dochodu (odpowiednio przychodu w zeznaniu PIT–28)”, bez wskazania, o jaki przychód chodzi.
  - Formularz PIT-28(25) (https://www.gov.pl/attachment/4702beb3-9a78-4c10-a023-c9bdd2a037f6), część E.1: darowizny
    z PIT/O odlicza się razem ze stratami i składkami społecznymi, a składki zdrowotne dopiero w części E.4; formularz
    nie określa podstawy limitu 6%.
  - Uzasadnienie projektu ustawy Dz.U. 2026 poz. 1541 (druk sejmowy nr 3149,
    https://api.sejm.gov.pl/sejm/term10/prints/3149/3149-uzasadnienie.docx), część o krwiodawstwie: odliczenie „nie
    może przekroczyć odpowiednio 6 % rocznego dochodu (przychodu)”.
  - Eureka: brak objaśnień podatkowych i interpretacji ogólnej o art. 26 ust. 5 na ryczałcie.

## P14. Limit ulgi internetowej w zeznaniu za 2027 r. po jej uchyleniu

- Wpisy: `ulga.internet.limit` (2027-01-01 – 2027-12-31, 760 zł) oraz kroki o Internecie w `zasada.ulgi_ryczalt`
  i `zasada.ulgi_skala` (od 2027-01-01).
- Zgłoszone: 2026-11-26.
- Ustawa z 22 października 2026 r. (Dz.U. 2026 poz. 1541) uchyla art. 26 ust. 1 pkt 6a i ust. 6h ustawy o PIT
  dla dochodów (przychodów) od 1 stycznia 2027 r. (art. 1 pkt 1, art. 4 ust. 1). Podatnik, który po raz pierwszy
  skorzysta z odliczenia w zeznaniu za 2026 r., „zachowuje prawo do tego odliczenia w zeznaniu podatkowym składanym
  za 2027 r. na zasadach określonych w art. 26 ust. 1 pkt 6a i ust. 6h” (art. 5 ust. 1); do podatników, którzy odliczali wydatki
  na ryczałcie, ust. 1 stosuje się odpowiednio (art. 5 ust. 2).
- Brak drugiego źródła, które samo podaje limit na 2027 r.: strona MF „Ulga na Internet PIT” (aktualizacja 9.10.2026)
  powstała przed ogłoszeniem ustawy, a ifirma.pl podaje przepis przejściowy bez kwoty.
- Art. 5 ust. 2 stosuje ust. 1 do podatników, którzy skorzystali z odliczenia na ryczałcie, tylko „odpowiednio”.
  Przepis nie mówi, co się dzieje, gdy podatnik zmienił formę opodatkowania między 2026 a 2027 r.
- Pytania:
  1. Czy w zeznaniu za 2027 r. taki podatnik odlicza wydatki na Internet poniesione w 2027 r. do 760 zł?
  2. Jak „odpowiednio” stosuje się art. 5 ust. 1 na ryczałcie: czy prawo do odliczenia od przychodu w zeznaniu
     za 2027 r. ma podatnik, który po raz pierwszy odliczył wydatki od przychodu w zeznaniu za 2026 r.?
  3. Czy prawo zachowuje podatnik, który w 2026 r. odliczył wydatki na ryczałcie, a w 2027 r. rozlicza się według
     skali (albo odwrotnie)? Czy traci je podatnik, który w 2027 r. przeszedł na podatek liniowy?
- Przeszukane źródła urzędowe (2026-11-26), bez rozstrzygnięcia:
  - Uzasadnienie projektu (druk sejmowy nr 3149, https://api.sejm.gov.pl/sejm/term10/prints/3149/3149-uzasadnienie.docx),
    część o art. 5: przepis „zachowuje zatem roczne prawa nabyte dla osób, które po raz pierwszy skorzystają z tego
    odliczenia w rozliczeniu podatku PIT (zarówno na podstawie ustawy o PIT, jak i ustawy o ryczałcie), w rozliczeniu
    podatku za rok poprzedzający rok wejścia w życie projektowanej ustawy”. We wstępie podaje obecny limit: „do wysokości
    limitu 760 zł rocznie”. Uzasadnienie nie mówi o zmianie formy opodatkowania między 2026 a 2027 r. i nie podaje
    wprost limitu dla zeznania za 2027 r. Uzasadnienie nie jest objaśnieniem podatkowym, więc nie rozstrzyga pytań 1 i 2.
  - Strona MF „Ulga na Internet PIT” nadal ma aktualizację z 9.10.2026 (sprawdzone 2026-11-26), sprzed ogłoszenia ustawy.
  - Eureka: brak objaśnień podatkowych i interpretacji ogólnej o uldze internetowej po 2026 r.

## P15. Wyłączenie łącznego opodatkowania przy podatku liniowym albo ryczałcie: rok bez przychodów i zmiana formy w trakcie roku

- Wpis: `zasada.opodatkowanie_laczne_wylaczenia` (od 2025-01-01), ostatni krok.
- Zgłoszone: 2026-11-26.
- Ustawa o PIT (Dz.U. 2026 poz. 592), art. 6 ust. 8 pkt 1: wspólnego opodatkowania małżonków i sposobu
  opodatkowania osoby samotnie wychowującej dzieci nie stosuje się, gdy choćby jeden z małżonków (osoba
  samotnie wychowująca dziecko lub jej dziecko) stosuje art. 30c albo ustawę o zryczałtowanym podatku
  dochodowym (z wyjątkiem jej art. 6 ust. 1a) „w zakresie osiągniętych w roku podatkowym przychodów,
  poniesionych kosztów uzyskania przychodów, zobowiązania lub uprawnienia do zwiększania lub pomniejszenia
  podstawy opodatkowania” albo innych doliczeń lub odliczeń.
- podatki.gov.pl (Wspólne rozliczenie małżonków, aktualizacja 24.06.2026) i biznes.gov.pl (strona 00264):
  rok, w którym przy działalności na podatku liniowym nie było przychodów, kosztów ani odliczeń („zerowy”
  PIT-36L), nie wyklucza wspólnego rozliczenia. biznes.gov.pl: zmiana w trakcie roku z podatku liniowego albo
  ryczałtu na zasady ogólne wyklucza wspólne rozliczenie za ten rok.
- Pytania: czy oba te wyjaśnienia wynikają z art. 6 ust. 8 i czy można je dopisać do zasady jako kroki?
  Czy tak samo jest przy ryczałcie od przychodów ewidencjonowanych (rok bez przychodów i kosztów) i przy
  karcie podatkowej?
- Przeszukane źródła urzędowe (2026-11-26), bez rozstrzygnięcia:
  - Objaśnienia podatkowe MF z 18 stycznia 2019 r. (Eureka, ID 482279,
    https://eureka.mf.gov.pl/informacje/podglad/482279) powtarzają wyłączenia z art. 6 ust. 8 ogólnie, bez roku bez
    przychodów i bez zmiany formy w trakcie roku.
  - Materiał dla eksperta: „Pigułka wiedzy” KIS „Rozliczenie wspólne małżonków” (Eureka, ID 525130,
    https://eureka.mf.gov.pl/informacje/podglad/525130), pytanie 5: „Wspólne rozliczenie z małżonkiem jest możliwe,
    jeśli do któregoś z małżonków mają zastosowanie przepisy dot. działalności gospodarczej opodatkowanej podatkiem
    liniowym, ale ma on „zerowy” PIT-36L”. Nie dotyczy ryczałtu, karty podatkowej ani zmiany formy w trakcie roku.
    „Pigułka wiedzy” nie jest objaśnieniem podatkowym ani interpretacją ogólną.

## P16. Wniosek o łączne opodatkowanie w zeznaniu złożonym po terminie albo w korekcie; okres samotnego wychowywania dzieci

- Materiał urzędowy znaleziony 2026-11-26 (pytanie zostaje otwarte): objaśnienia podatkowe MF z 18 stycznia 2019 r.
  (Eureka, ID 482279, https://eureka.mf.gov.pl/informacje/podglad/482279) podają, że po uchyleniu art. 6 ust. 10 ustawy
  o PIT możliwość „opodatkowania dochodów małżonków, wdów i wdowców albo osób samotnie wychowujących dzieci nie jest już
  uzależniona od terminu złożenia wniosku o wyborze preferencyjnego sposobu opodatkowania zawartego w zeznaniu
  podatkowym”, a małżonkowie, którzy złożyli zeznanie po terminie, „nie tracą uprawnienia do wspólnego opodatkowania
  dochodów mimo upływu terminu na złożenie zeznania” (Przykład 2). Objaśnienia mówią też o podatnikach, którzy złożyli
  zeznanie w terminie, ale nie skorzystali z preferencyjnego opodatkowania i „nie mogąc tego dokonać po terminie” czuli
  się pokrzywdzeni („Wprowadzona zmiana eliminuje tę niedogodność”), a Przykład 1 (stan sprzed zmiany) opisuje korektę
  wspólnego zeznania na odrębne zeznania. Objaśnienia opisują stan prawny z 2019 r.; w innych punktach (zawarcie
  małżeństwa w trakcie roku, śmierć małżonka, dochody uczącego się dziecka) są nieaktualne. Kroków zasad nie zmieniono:
  zmiana kroku wymaga nowej wersji po ocenie, czy objaśnienia obejmują też korektę zeznania.

- Wpisy: `zasada.malzonkowie_wspolne_opodatkowanie` i `zasada.samotny_rodzic_opodatkowanie` (od 2025-01-01),
  krok o wniosku; przy osobie samotnie wychowującej dzieci także ostatni krok.
- Zgłoszone: 2026-11-26.
- Ustawa o PIT (Dz.U. 2026 poz. 592), art. 6 ust. 2 i ust. 4c: wniosek wyraża się w zeznaniu podatkowym
  (przy osobie samotnie wychowującej dzieci: w rocznym zeznaniu). Przepis nie mówi o terminie wniosku ani
  o korekcie. Zeznanie składa się w terminie z art. 45 ust. 1.
- podatki.gov.pl (Wspólne rozliczenie małżonków; Osoba samotnie wychowująca dziecko; aktualizacja
  24.06.2026): wniosek można wyrazić w korekcie zeznania, można też zmienić wspólne rozliczenie na
  indywidualne korektą, a złożenie zeznania po terminie nie pozbawia prawa do wspólnego rozliczenia.
- Pytania: czy wniosek o łączne opodatkowanie (i o sposób opodatkowania dla osoby samotnie wychowującej
  dzieci) można skutecznie wyrazić w korekcie zeznania i na jakiej podstawie (art. 81 Ordynacji podatkowej?),
  oraz czy korektą można z niego zrezygnować? Czy objaśnienia z 18 stycznia 2019 r. (wyżej) pozwalają opisać w zasadzie
  wniosek w zeznaniu złożonym po terminie?
- Art. 6 ust. 4c: sposób opodatkowania dotyczy rodzica, który „w roku podatkowym samotnie wychowuje dzieci”.
  Przepis nie mówi, czy przez cały rok. podatki.gov.pl (Osoba samotnie wychowująca dziecko) podaje, że nie
  trzeba samotnie wychowywać dziecka przez cały rok (przykład rozwodu w trakcie roku).
- Pytanie: czy warunek samotnego wychowywania dzieci jest spełniony, gdy trwał tylko przez część roku
  podatkowego, i czy można to dopisać do zasady?
- Przeszukane źródła urzędowe (2026-11-26), bez rozstrzygnięcia pozostałych pytań: objaśnienia z 18 stycznia 2019 r. nie
  mówią o okresie samotnego wychowywania; Eureka nie ma w tych sprawach innych objaśnień ani
  interpretacji ogólnej. Odpowiedzi MF dla mediów z 9 lutego 2024 r. (Eureka, ID 578092 i 578172) dotyczą opieki
  naprzemiennej, nie okresu w roku.

## P17. Wariant JPK_V7K dla deklaracji za I kwartał 2026 r.

- Wpisy: `schemat.jpk_v7k` (od 2026-02-01, wariant 3, i do 2026-01-31, wariant 2: od odpowiedzi zależy data końca).
- Zgłoszone: 2026-11-26.
- MF (podatki.gov.pl, gov.pl/web/kas/struktury-jpk, broszura z 1 lutego 2026 r.): wariant 2 stosuje się „za okresy
  rozliczeniowe od stycznia 2022 roku do stycznia 2026 roku”, a wariant 3 „za okresy rozliczeniowe od lutego 2026 roku”.
- Plik JPK_V7K składa się za miesiąc; plik za trzeci miesiąc kwartału zawiera też deklarację za cały kwartał.
  I kwartał 2026 r. obejmuje styczeń, za który obowiązuje wariant 2.
- Rozporządzenie Dz.U. 2025 poz. 1800 (§ 2a pkt 2 dodany do rozporządzenia Dz.U. 2024 poz. 13) każe wykazać dane
  o kaucji „w deklaracji za I kwartał 2026 r.”, co sugeruje wariant 3, ale nie mówi tego wprost.
- Pytanie: czy plik JPK_V7K za marzec 2026 r. z deklaracją za I kwartał 2026 r. (i jego korekty) składa się
  w wariancie 3? Którego wariantu używa się do korekty deklaracji za I kwartał 2026 r.?
- Dodatkowe materiały (2026-11-26), bez rozstrzygnięcia:
  - Rozporządzenie Dz.U. 2024 poz. 13, § 5: do rozliczeń „za okresy rozliczeniowe przypadające przed dniem wejścia w życie”
    (1 lutego 2026 r.) stosuje się przepisy dotychczasowe. I kwartał 2026 r. zaczął się przed 1 lutego 2026 r.; czy dla
    deklaracji kwartalnej okresem rozliczeniowym w rozumieniu § 5 jest kwartał, jest częścią pytania. Jednocześnie § 2a pkt 2 (Dz.U. 2025 poz. 1800) każe wykazać kaucję
    w deklaracji za I kwartał 2026 r., czego dotychczasowe przepisy nie przewidują.
  - Broszura MF z 2026 r. (pole Miesiac): w pliku JPK_V7K z deklaracją podaje się ostatni miesiąc kwartału, ale broszura nie
    mówi, który wariant stosuje się do kwartału obejmującego styczeń 2026 r. Komunikat MF z 19 grudnia 2025 r. (podatki.gov.pl
    i gov.pl/web/finanse) mówi tylko o stosowaniu nowych wzorów „do rozliczeń od 1 lutego 2026 r.”.
  - Schematy XSD obu wariantów (CRWDE 2021/12/27/11149 i 2025/12/19/14089) technicznie dopuszczają rok 2026 i każdy kwartał,
    więc nie rozstrzygają pytania.
  - Specyfikacja interfejsów usług JPK 5.6.0 i strona KAS „Struktury JPK” nie wyjaśniają tego przypadku.

## P18. Czy na ryczałcie przesyła się ewidencję przychodów (JPK_EWP) (rozstrzygnięte 2026-11-26, bez eksperta)

- Rozstrzygnięcie: broszura MF o strukturze JPK_EWP(4) sama podaje wprost, że osoby fizyczne i spółki opodatkowane
  ryczałtem od przychodów ewidencjonowanych, prowadzące ewidencję przychodów, „będą zobowiązane przesyłać plik XML zgodny
  ze strukturą JPK_EWP”, i wskazuje art. 15 ust. 12 jako podstawę. Zgadza się to z ustawą: art. 15 ust. 1 nazywa ewidencję
  przychodów „ewidencją”, a ust. 12 obejmuje podmioty „prowadzące ewidencję lub wykaz środków trwałych”. Strona KAS
  „Struktury JPK w podatkach dochodowych” podaje dla ryczałtowców daty struktur JPK_EWP i JPK_ST z podstawą art. 15 ust. 12
  i 13. Krok zasady poprawiony, P18 usunięty z `open_issue`. Ryczałtowiec prowadzący ewidencję przychodów przesyła ją
  także wtedy, gdy nie ma środków trwałych.

- Wpis: `zasada.jpk_pd_ryczalt` (od 2026-01-01).
- Zgłoszone: 2026-11-26.
- Ustawa o zryczałtowanym podatku dochodowym (Dz.U. 2025 poz. 843), art. 15 ust. 12: podmioty z ust. 1
  „prowadzące ewidencję lub wykaz środków trwałych oraz wartości niematerialnych i prawnych są obowiązane prowadzić
  tę ewidencję i wykaz przy użyciu programów komputerowych” i przesyłać je po zakończeniu roku do upływu terminu
  zeznania. Art. 66 ust. 1 ustawy z 29 października 2021 r. (Dz.U. 2021 poz. 2105) wymienia „księgi, ewidencje
  i wykazy” z art. 15 ust. 12.
- Broszura MF o strukturze JPK_EWP(4) (podatki.gov.pl) podaje, że podmioty prowadzące ewidencję przychodów „będą
  zobowiązane przesyłać plik XML zgodny ze strukturą JPK_EWP”, i wskazuje art. 15 ust. 12 jako podstawę.
- Strona MF o JPK_PD (podatki.gov.pl) podaje, że ustawa z 29 października 2021 r. nałożyła obowiązek prowadzenia
  „ewidencji i wykazów prowadzonych dla celów podatków dochodowych” przy użyciu programów komputerowych
  i ich przekazywania, wymienia JPK_EWP wśród pięciu struktur, które „JPK_PD obejmie”, i mówi o przesyłaniu danych
  w postaci „obligatoryjnych plików JPK_PD”. Tekst art. 15 ust. 12 wymienia jednak tylko „ewidencję lub wykaz środków trwałych oraz
  wartości niematerialnych i prawnych”.
- Pytanie: czy art. 15 ust. 12 obejmuje ewidencję przychodów (czyli czy ryczałtowiec przesyła JPK_EWP), czy tylko
  ewidencję lub wykaz środków trwałych oraz wartości niematerialnych i prawnych (JPK_ST)? Czy ryczałtowiec bez
  środków trwałych przesyła cokolwiek?

## P19. Na który dzień ocenia się rozliczanie VAT miesięcznie przy pierwszym przesłaniu ksiąg w formie JPK

- Wpisy: `zasada.jpk_pd_pkpir` (od 2026-07-01) i `zasada.jpk_pd_ryczalt` (od 2026-01-01).
- Dotyczy też `schemat.jpk_ewp` (od 2026-01-01), ale tylko pośrednio: od odpowiedzi zależy, za który rok po raz
  pierwszy przesyła się plik JPK_EWP, a nie wariant schematu. Dlatego ten wpis nie ma otwartego pytania.
- Zgłoszone: 2026-11-26.
- Art. 66 ust. 1 ustawy z 29 października 2021 r. (Dz.U. 2021 poz. 2105, w brzmieniu z Dz.U. 2022 poz. 1265
  i Dz.U. 2023 poz. 1059): księgi i ewidencje przesyła się po raz pierwszy za rok podatkowy rozpoczynający się po
  31 grudnia 2025 r. „w przypadku podmiotów, które są obowiązane przesyłać ewidencję”, o której mowa w art. 109
  ust. 3 ustawy o VAT, zgodnie z art. 109 ust. 3b (rozliczenie miesięczne), a pozostali za rok rozpoczynający się
  po 31 grudnia 2026 r. Przepis nie mówi, na który dzień albo za który okres ocenia się ten obowiązek.
- Pytania: czy obowiązek przesłania księgi lub ewidencji za 2026 r. ma podatnik, który w 2026 r. zmienił rozliczenie
  VAT z kwartalnego na miesięczne (albo odwrotnie)? Czy ma go podatnik, który w trakcie 2026 r. zarejestrował się
  jako czynny podatnik VAT rozliczający się miesięcznie? Czy liczy się stan na początek roku, na koniec roku, czy
  którykolwiek miesiąc roku?
- Przeszukane źródła (2026-11-26), bez rozstrzygnięcia: broszury MF o JPK_PKPIR(3) i JPK_EWP(4), strony MF o JPK_PD
  i KAS „Struktury JPK w podatkach dochodowych”, uzasadnienie projektu ustawy z 9 czerwca 2022 r. (druk sejmowy nr 2186,
  IX kadencja). Żadne z nich nie mówi, na który dzień ocenia się obowiązek. Pierwotne brzmienie art. 66 ust. 1 (Dz.U. 2022
  poz. 1265) mówiło o „okresach rozliczeniowych rozpoczynających się” po danym dniu; ustawa Dz.U. 2023 poz. 1059 zastąpiła je
  „rokiem podatkowym rozpoczynającym się”. Strona KAS mówi o podatnikach „obowiązanych przesyłać pliki JPK_V7M”,
  a strona MF o JPK_PD o podatnikach „zobowiązani do składania JPK_VAT za okresy miesięczne”, obie bez wskazania dnia.

## P20. Ulga na robotyzację i ulga na ekspansję od 2027 r.: odpisy od aktywów sprzed 2027 r. i kolejność wobec art. 26i

- Wpisy: `zasada.ulgi_liniowy` i `zasada.ulgi_skala` (od 2027-01-01), krok o odliczeniach od podstawy obliczenia podatku.
- Zgłoszone: 2026-11-26.
- Ustawa z 22 października 2026 r. (Dz.U. 2026 poz. 1541), art. 1 pkt 4 lit. a, dodaje w art. 52jb ustawy o PIT
  ust. 2a: „W przypadku środków trwałych i wartości niematerialnych i prawnych podlegających amortyzacji za koszty
  uzyskania przychodów poniesione na robotyzację uznaje się dokonywane w danym roku podatkowym, zaliczane do kosztów
  uzyskania przychodów, odpisy amortyzacyjne od tych środków trwałych oraz wartości niematerialnych i prawnych”. Nowe brzmienie stosuje się do dochodów od 1 stycznia 2027 r.
  (art. 4 ust. 1). Art. 7 ust. 1 każe stosować uchylany ust. 5a do kosztów „poniesionych przed dniem 1 stycznia 2027 r.”.
- Pytania: czy od 2027 r. kosztem poniesionym na robotyzację są także odpisy amortyzacyjne od robotów i innych aktywów
  z art. 52jb ust. 2 nabytych przed 2027 r.? Jeżeli tak, czy do takich odpisów stosuje się wyłączenia z ust. 5a
  (art. 7 ust. 1), skoro odpis dokonany w 2027 r. nie jest kosztem „poniesionym przed dniem 1 stycznia 2027 r.”?
  Czy koszt nabycia odliczony przed 2027 r. można odliczyć ponownie przez odpisy?
- Ulga na ekspansję: ta sama ustawa uchyla art. 26gb od 1 stycznia 2027 r., ale do kosztów poniesionych przed tym dniem
  „stosuje się przepisy dotychczasowe” (art. 6 ust. 1), a art. 26gb ust. 9 pozwala odliczać nieodliczoną część
  w zeznaniach za sześć kolejnych lat, a ust. 6 przewiduje doliczenie odliczonej kwoty. Jednocześnie art. 26i ust. 1 od 1 stycznia 2027 r. nie wymienia art. 26gb
  wśród odliczeń, po których koryguje się podstawę (art. 1 pkt 3).
- Pytanie dodatkowe: w jakiej kolejności po 2026 r. stosuje się odliczenie i doliczenie z art. 26gb (ust. 9 i 6) za koszty
  sprzed 2027 r. i korektę podstawy z art. 26i: czy art. 26i stosuje się do podstawy przed nimi, czy po nich?
- Przeszukane źródła urzędowe (2026-11-26), bez rozstrzygnięcia:
  - Uzasadnienie projektu (druk sejmowy nr 3149, https://api.sejm.gov.pl/sejm/term10/prints/3149/3149-uzasadnienie.docx):
    stanowisko MF „jest w tej sprawie niezmienne od początku obowiązywania przepisów regulujących ulgę na robotyzację”
    i „W ocenie MF prawidłowym jest uznanie za koszt kwalifikowany kwoty dokonywanych odpisów amortyzacyjnych”; o art. 7:
    przy rozliczaniu ulgi w latach po zmianie „nadal należy stosować ograniczenie, o którym mowa w uchylanym ust. 5a,
    dotyczącym zasady DNSH (do kosztów sprzed nowelizacji)”; o art. 6: podatnicy będą „uprawnieni kontynuować
    odliczenie nieodliczonej w poprzednich latach ulgi ze względu na brak dochodu”. Uzasadnienie nie mówi o odpisach
    od aktywów nabytych przed 2027 r. ani o kolejności wobec art. 26i.
  - Eureka: brak objaśnień podatkowych i interpretacji ogólnej o uldze na robotyzację i uldze na ekspansję. W odpowiedzi
    dla mediów z 10 maja 2023 r. (Eureka, ID 543390) MF zapowiedziało objaśnienia o uldze na ekspansję; w Eurece ich nie ma.

## P30. Limit odliczenia składki zdrowotnej przy podatku liniowym na 2027 r.

- Wpis: `podatek.liniowy.limit_skladki_zdrowotnej` (2027-01-01 – 2027-12-31, 15 100 zł).
- Zgłoszone: 2026-11-26.
- Obwieszczenie Ministra Finansów i Gospodarki z 16 listopada 2026 r. (M.P. 2026 poz. 1163), wydane na podstawie
  art. 30c ust. 2c ustawy o PIT: łączna kwota „w roku 2027 nie może przekroczyć 15 100 zł”.
- Na 26 listopada 2026 r. żadna strona urzędu (podatki.gov.pl, biznes.gov.pl) nie podaje jeszcze kwoty na 2027 r.,
  więc wartość nie ma drugiego dowodu.
- Pytanie: czy limit z art. 30c ust. 2 pkt 2 ustawy o PIT na rok podatkowy 2027 wynosi 15 100 zł?

## P31. Termin wpisu przychodów do ewidencji za grudzień (rozstrzygnięte 2026-11-26, bez eksperta)

- Rozstrzygnięcie: rozporządzenie w sprawie prowadzenia ewidencji przychodów (Dz.U. 2025 poz. 1294), § 6, samo podaje
  wprost, że zapisy dokonuje się „najpóźniej do 20. dnia każdego miesiąca za miesiąc poprzedni”. Przepis obejmuje każdy
  miesiąc i nie ma wyjątku dla grudnia, więc wpisy za grudzień dokonuje się do 20 stycznia. Rozporządzenie nie ma przepisów
  przejściowych dla ewidencji (§ 10 dotyczy tylko wykazu środków trwałych). Termin nie zależy od kwartalnego wpłacania
  ryczałtu. Wpis `termin.ewidencja_przychodow_wpis` nie ma otwartego pytania.

- Wpis: `termin.ewidencja_przychodow_wpis` (od 2026-01-01).
- Zgłoszone: 2026-11-26 (specyfikacja Staffkey, obszar A2).
- Pytanie: czy termin wpisu przychodów za grudzień jest inny niż za pozostałe miesiące?

## P32. Korekta przychodu w ewidencji przychodów przy błędzie rachunkowym lub oczywistej omyłce

- Wpis: `zasada.ewidencja_przychodow` (od 2026-01-01), krok o korekcie przychodu.
- Zgłoszone: 2026-11-26.
- Ustawa o PIT (Dz.U. 2026 poz. 592), art. 14 ust. 1m: jeżeli korekta przychodu „nie jest spowodowana błędem rachunkowym
  lub inną oczywistą omyłką”, ujmuje się ją w okresie rozliczeniowym, w którym wystawiono fakturę korygującą. Ustawa
  o ryczałcie (Dz.U. 2025 poz. 843) odwołuje się do tej korekty w art. 6 ust. 1e i 1f, więc dla korekt bez błędu ustawa
  sama wskazuje okres i to opisuje krok zasady, razem z art. 6 ust. 1f (korekta po zmianie formy opodatkowania).
  Wyłączeń z art. 14 ust. 1o krok nie opisuje.
- Ani ustawa, ani rozporządzenie Dz.U. 2025 poz. 1294 nie mówią, w którym okresie ujmuje się korektę wynikającą z błędu
  rachunkowego lub oczywistej omyłki. Rozporządzenie przewiduje zapis „ze znakiem (-)” tylko dla korekty danych
  z raportów fiskalnych (§ 4 ust. 5); wzór ewidencji nie ma osobnej kolumny na korektę.
- Pytania: czy korektę wynikającą z błędu rachunkowego lub oczywistej omyłki ujmuje się w okresie, w którym ujęto
  pierwotny przychód (z korektą wpłaconego ryczałtu za ten okres)? Jak wpisuje się taką korektę i korektę z art. 14 ust. 1m
  do ewidencji: nowym zapisem ze znakiem minus z datą wpisu w dniu korekty, czy poprawieniem pierwotnego zapisu?

## P33. Data uzyskania przychodu, gdy faktura jest wystawiona przed wykonaniem usługi

- Wpisy: `zasada.przychod_data_uzyskania` (od 2026-01-01), krok o dniu wykonania usługi, oraz `zasada.przychod_w_walucie`
  (od 2026-01-01), krok o kursie.
- Zgłoszone: 2026-11-26.
- Ustawa o PIT (Dz.U. 2026 poz. 592), art. 14 ust. 1c: datą powstania przychodu jest dzień wydania rzeczy lub wykonania
  usługi, „niepóźniej niż dzień: 1) wystawienia faktury albo 2) uregulowania należności”. Art. 14 ust. 3 pkt 1: do
  przychodów nie zalicza się „pobranych wpłat lub zarachowanych należności na poczet dostaw towarów i usług, które zostaną
  wykonane w następnych okresach sprawozdawczych”.
- Art. 11a ust. 1: przychód w walucie przelicza się po kursie z ostatniego dnia roboczego przed „dniem uzyskania
  przychodu”, więc od odpowiedzi zależy też dzień kursu.
- Pytania: czy przy fakturze wystawionej przed wykonaniem usługi (albo wydaniem rzeczy), bez zapłaty, dniem uzyskania
  przychodu jest dzień wystawienia faktury? Czy inaczej jest, gdy faktura dokumentuje usługę wykonywaną w następnym okresie
  (zarachowana należność z art. 14 ust. 3 pkt 1)? Czy na ryczałcie odpowiedź jest taka sama?

## P34. Przeliczenie przychodu w walucie obcej na ryczałcie

- Wpis: `zasada.przychod_w_walucie` (od 2026-01-01), krok o ryczałcie.
- Zgłoszone: 2026-11-26.
- Ustawa o PIT (Dz.U. 2026 poz. 592), art. 11a ust. 1: przychody w walutach obcych przelicza się „według kursu średniego
  walut obcych ogłaszanego przez Narodowy Bank Polski z ostatniego dnia roboczego poprzedzającego dzień uzyskania
  przychodu”.
- Ustawa o ryczałcie (Dz.U. 2025 poz. 843) nie odsyła do art. 11a. Art. 6 ust. 1 obejmuje ryczałtem przychody,
  „o których mowa w art. 7a ust. 4 lub art. 14 ustawy o podatku dochodowym”, a art. 6 ust. 1c każe stosować odpowiednio
  art. 24c (różnice kursowe), który sam posługuje się kursem średnim NBP. Przepisy ustawy o ryczałcie o przeliczaniu
  (na przykład art. 4 ust. 2) dotyczą kwot wyrażonych w euro.
- Przeszukane źródła urzędowe (2026-11-26), bez rozstrzygnięcia: strony podatki.gov.pl i biznes.gov.pl o ryczałcie od
  przychodów ewidencjonowanych, broszura MF o JPK_EWP(4) (pole kwoty przychodu w PLN, bez zasady przeliczenia).
- Pytanie: czy podatnik na ryczałcie przelicza przychód w walucie obcej według art. 11a ust. 1 ustawy o PIT? Jeżeli tak,
  na jakiej podstawie (art. 6 ust. 1 ustawy o ryczałcie)?

## P46. Wybór ryczałtu albo podatku liniowego w roku po utracie prawa do tej formy

- Wpis: `zasada.wybor_formy_opodatkowania` (od 2026-01-01), krok o roku po utracie prawa.
- Zgłoszone: 2026-11-26.
- Ustawa o ryczałcie (Dz.U. 2025 poz. 843), art. 9 ust. 1b: wybór ryczałtu „dotyczy również lat następnych”, chyba że
  podatnik w terminie złoży oświadczenie o rezygnacji albo o wyborze podatku liniowego. Art. 8 ust. 2: podatnik, który
  uzyska przychód od byłego lub obecnego pracodawcy, „traci w roku podatkowym prawo” do ryczałtu i do końca roku
  podatkowego opłaca podatek na ogólnych zasadach. Art. 8 ust. 3 mówi tak samo o utracie prawa w roku podatkowym.
- Ustawa o PIT (Dz.U. 2026 poz. 592), art. 9a ust. 2b: wybór podatku liniowego „dotyczy również lat następnych”;
  art. 9a ust. 3: podatnik „traci w roku podatkowym prawo” do podatku liniowego.
- Przepisy nie mówią wprost, czy wybór sprzed utraty prawa obowiązuje w następnym roku bez nowego oświadczenia.
  Przeszukane źródła urzędowe (2026-11-26), bez rozstrzygnięcia: strony podatki.gov.pl i biznes.gov.pl o ryczałcie
  i o podatku liniowym.
- Materiał (bez rozstrzygnięcia): biznes.gov.pl, Podatek liniowy (portal 00253) podaje, że wybór podatku liniowego
  „jest możliwy dopiero od roku następującego po roku podatkowym”, w którym podatnik pracował na rzecz byłego pracodawcy.
  Strona nie mówi, czy w tym następnym roku trzeba złożyć nowe oświadczenie.
- Pytanie: czy podatnik, który stracił w roku podatkowym prawo do ryczałtu (art. 8 ust. 2 lub 3 ustawy o ryczałcie) albo
  do podatku liniowego (art. 9a ust. 3 ustawy o PIT), jest w następnym roku opodatkowany tą formą bez nowego oświadczenia,
  jeżeli spełnia jej warunki? Czy musi złożyć oświadczenie o wyborze ponownie w terminie z art. 9 ust. 1 ustawy
  o ryczałcie albo art. 9a ust. 2 ustawy o PIT?

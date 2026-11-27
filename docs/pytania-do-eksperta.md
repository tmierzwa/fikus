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

- Wpis: `zasada.ryczalt_zdrowotna_prog_poprzedni_rok` (od 2025-01-01 i od 2027-01-01), krok 4.
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
- Dalsze źródła sprawdzone 2026-11-27, bez rozstrzygnięcia:
  - Poradnik ZUS „Polski Ład” (stan prawny na 1 stycznia 2025 r.), przykład 17: „Od lipca Dariusz nie jest związany swoją
    deklaracją” i „może zatem ustalić swoją podstawę wymiaru składki zdrowotnej na podstawie przychodów z działalności
    osiągniętych od początku 2023 r.”. Przykład dotyczy zakończenia działalności i rozpoczęcia nowej, nie zawieszenia,
    i nie wskazuje przepisu, z którego wynika wyjątek.
  - Ten sam poradnik, przykład 15 (ryczałt, likwidacja i nowa działalność w lipcu): „W lipcu 2023 r. suma przychodów
    liczonych od początku 2023 r. przekroczyła 60 000 zł”. Przykład nie dotyczy art. 81 ust. 2h.

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

## P4. Zryczałtowana stopa składki wypadkowej dla płatnika do 9 ubezpieczonych (rok 2025/2026 rozstrzygnięty 2026-11-27, bez eksperta; rok 2026/2027 otwarty)

- Rozstrzygnięcie częściowe, tylko za rok 2025/2026: poradnik ZUS „Ustalanie stopy procentowej składki na ubezpieczenie
  wypadkowe” (stan prawny na 1 stycznia 2026 r.) sam podaje stopę zryczałtowaną 1,67% dla płatnika zgłaszającego nie więcej
  niż 9 ubezpieczonych. Spoza ZUS podaje ją biznes.gov.pl (aktualizacja 11 lutego 2026 r.: składkę 1,67% opłacają firmy, które
  zgłosiły przeciętnie nie więcej niż 9 osób). Podaje ją też materiał ZUS województwa opolskiego przedrukowany przez Zieloną Linię
  (stan prawny na 26 listopada 2025 r.). Zastrzeżenie wobec biznes.gov.pl opisane niżej nie przeszkadza: obie daty początku
  stopy na tej stronie (1 kwietnia 2021 r. i 1 kwietnia 2024 r.) są wcześniejsze niż 1 kwietnia 2025 r., a cytowany przypis
  podaje stopę i grupę płatników w stanie na 11 lutego 2026 r., czyli w trakcie roku 2025/2026; stopę ustala się na cały rok
  składkowy (art. 27 ust. 1 ustawy wypadkowej). `open_issue` usunięty z wersji 2025/2026.
- Za rok 2026/2027 pytanie pozostaje otwarte: stopę na ten rok podają tylko komunikat ZUS z 12 stycznia 2026 r. (w części o tym roku)
  i przedruk wypowiedzi rzeczniczki ZUS z 1 kwietnia 2026 r. Załącznik nr 2 rozporządzenia nie nazywa najwyższej stopy,
  podaje tylko tabelę.

- Wpis: `zus.stawka.wypadkowa_do_9` (2025-04-01 – 2026-03-31 i 2026-04-01 – 2027-03-31, 1,67%).
- Zgłoszone: 2026-11-26.
- Ustawa wypadkowa, art. 28 ust. 1: stopa wynosi 50% najwyższej stopy ustalonej na dany rok składkowy
  dla grup działalności. Najwyższa stopa w tabeli z załącznika nr 2 rozporządzenia (Dz.U. 2025
  poz. 1874) to 3,33, a § 6 ust. 2 każe zaokrąglać według zasady matematycznej. Kwotę 1,67% podają
  wprost materiały ZUS (poradnik i strona o informacji ZUS IWA), a za rok 2025/2026 także biznes.gov.pl, choć bez wskazania roku składkowego (niżej).
- Pytanie (po rozstrzygnięciu za 2025/2026 dotyczy już tylko roku 2026/2027): czy dla płatnika zgłaszającego nie więcej
  niż 9 ubezpieczonych stopa w roku składkowym 2026/2027 wynosi 1,67%, i czy istnieje urzędowe źródło poza materiałami ZUS, które
  podaje tę stopę wprost?

- Materiały znalezione 2026-11-26 (historia; rok 2025/2026 rozstrzyga przypis z tej samej strony biznes.gov.pl, opisany wyżej):
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
- Dalsze źródła sprawdzone 2026-11-27, bez rozstrzygnięcia:
  - Interpretacja indywidualna KIS z 25 lipca 2025 r., sygn. 0115-KDST2-1.4011.286.2025.3.JPO
    (https://eureka.mf.gov.pl/informacje/podglad/650518), wiąże tylko wnioskodawcę. Przy jednej ewidencji bez wyodrębnienia
    przychodów z usług objętych stawkami 8,5%, 12% i 15% organ uznał, że „dla wszystkich opisanych usług, będących przedmiotem
    Pana wniosku, znajdzie zastosowanie – zgodnie z art. 12 ust. 3 pkt 2 (…) – stawka ryczałtu w wysokości 15%”. Nie omawia
    wprost, którą stawkę stosuje się przy przychodach z kilku punktów art. 12 ust. 1, i stoi w opozycji do opisu
    z biznes.gov.pl.

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
- Dalsze źródła sprawdzone 2026-11-27, bez rozstrzygnięcia:
  - Kalkulator rocznej składki zdrowotnej ZUS (https://www.zus.pl/firmy/przedsiebiorco-przeczytaj-wazne/kalkulator-rocznej-skladki-zdrowotnej),
    tylko źródło kontrolne: „Podaj liczbę miesięcy podlegania ubezpieczeniu zdrowotnemu dla formy opodatkowania „podatek
    liniowy” w roku kalendarzowym, którego dotyczy roczne rozliczenie (w liczbie miesięcy nie uwzględnia się miesięcy zwolnienia
    z opłacania składki).” Strona nie mówi, że ta liczba służy do minimum z art. 79a ust. 1 pkt 2, i obejmuje lata 2022–2025.
  - Poradnik ZUS „ZUS DRA” (maj 2026), przykład 15: roczna podstawa „nie może być niższa niż kwota wyliczona jako iloczyn
    liczby miesięcy, w których korzystała z tej formy opodatkowania i 75% minimalnego wynagrodzenia w 2025 r.”. Przykład dotyczy
    tylko roku 2025, który ma osobny przepis.

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
- Dalsze źródła sprawdzone 2026-11-27, bez rozstrzygnięcia:
  - Uzasadnienie projektu ustawy Dz.U. 2026 poz. 1542 (druk sejmowy nr 3160): „z uwagi na dalej obowiązujące zezwolenia na
    działanie na terenie SSE wydane na podstawie ustawy o SSE, konieczne było utrzymanie tego instrumentu do końca 2026 r.”;
    wygaszenie SSE od 1 stycznia 2027 r. „skutkuje brakiem możliwości rozliczania pomocy publicznej wynikającej z posiadanych
    zezwoleń”. Uzasadnienie nie jest źródłem prawa i nie mówi, do których dochodów stosuje się nowe brzmienie art. 81 ust. 2zd.
  - Ustawa Dz.U. 2026 poz. 1542, art. 26 ust. 1: nowe brzmienie art. 21 ust. 1 pkt 63b ustawy o PIT stosuje się „do dochodów
    uzyskanych z działalności gospodarczej określonej w decyzji o wsparciu wydanej po dniu 31 grudnia 2026 r.”; art. 24 ust. 2:
    „Decyzje o wsparciu wydane przed dniem wejścia w życie niniejszej ustawy obowiązują przez oznaczony czas, na który zostały
    wydane.” Żaden przepis przejściowy nie wymienia pkt 63a ani art. 81 ust. 2zd.

## P9. Ulga na start: jak liczyć 6 miesięcy ulgi i następne 24 miesiące podstawy preferencyjnej

- Wpis: `zasada.ulga_na_start` (od 2026-01-01), kroki 3, 5 i 6. Wartość `zus.ulga_na_start.okres` (6 miesięcy) od 2026-11-27
  nie ma tego pytania: podaje tylko liczbę miesięcy i odsyła do zasady (rozdzielenie wartości i sposobu stosowania).
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

- Wpis: `zasada.ulgi_ryczalt` (od 2026-01-01 i od 2027-01-01), krok o darowiznach. Wartość `ulga.darowizny.limit_ryczalt`
  (6%) od 2026-11-27 nie ma tego pytania: podaje tylko procent i odsyła do zasady (rozdzielenie wartości i sposobu stosowania).
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
- podatki.gov.pl (Wspólne rozliczenie małżonków, aktualizacja 24.06.2026): rok, w którym przy działalności
  na podatku liniowym nie było przychodów, kosztów ani odliczeń („zerowy” PIT-36L), nie wyklucza wspólnego
  rozliczenia. biznes.gov.pl (strona 00264) pisze tylko ogólnie, że wspólnego rozliczenia „nie wyłącza złożenie
  PIT zero”, i że zmiana w trakcie roku z podatku liniowego albo ryczałtu od przychodów ewidencjonowanych na zasady ogólne wyklucza wspólne
  rozliczenie za ten rok. W ogólnym warunku biznes.gov.pl wymienia też kartę podatkową (wspólne rozliczenie nie jest
  możliwe, gdy przy liniowym, ryczałcie lub karcie podatkowej osiąga się jakiekolwiek przychody, ponosi koszty albo
  korzysta z odliczeń lub ulg); o zmianie karty podatkowej na skalę w trakcie roku nie pisze.
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
- Ustalone 2026-11-26 (bez eksperta, z brzmienia przepisu): art. 6 ust. 8 pkt 1 lit. b odsyła do całej ustawy
  o zryczałtowanym podatku dochodowym (art. 5a pkt 15 ustawy o PIT) z wyjątkiem tylko jej art. 6 ust. 1a, więc obejmuje
  też kartę podatkową (art. 2 ust. 1 pkt 2 i rozdział 3 tej ustawy). Zasada to opisuje. Otwarte zostaje, jak przy ryczałcie
  od przychodów ewidencjonowanych i karcie podatkowej ocenia się rok bez przychodów i zmianę formy w trakcie roku.
- Dalsze źródła sprawdzone 2026-11-27, bez rozstrzygnięcia:
  - Interpretacja indywidualna KIS z 24 lutego 2026 r., sygn. 0115-KDIT2.4011.734.2025.3.ŁS
    (https://eureka.mf.gov.pl/informacje/podglad/680608), wiąże tylko wnioskodawcę. Dotyczy działalności opodatkowanej kartą
    podatkową, zawieszonej przez cały rok, bez przychodów, kosztów, doliczeń i odliczeń; taki stan „nie powoduje utraty prawa
    do wspólnego opodatkowania dochodów małżonków”, a „Istotą nie jest zatem kwestia braku ewidencjonowania przychodu czy też
    kosztów uzyskania przychodów lecz rzeczywisty ich brak.” Nie dotyczy ryczałtu od przychodów ewidencjonowanych ani zmiany
    formy w trakcie roku.
  - Interpretacja indywidualna Dyrektora Izby Skarbowej w Warszawie z 16 listopada 2010 r., sygn. IPPB1/415-854/10-2/JB
    (https://eureka.mf.gov.pl/informacje/podglad/94867), wiąże tylko wnioskodawcę: podatnik, który stracił w trakcie roku prawo
    do podatku liniowego (art. 9a ust. 3), „poprzez utratę prawa do opodatkowania tzw. podatkiem liniowym uzyska prawo do
    preferencyjnego opodatkowania”. Wydana według art. 6 ust. 8 w brzmieniu z 2010 r. i dotyczy przymusowej utraty prawa,
    nie dobrowolnej zmiany formy; różni się od opisu z biznes.gov.pl.

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
  małżeństwa w trakcie roku, śmierć małżonka, dochody uczącego się dziecka) są nieaktualne. Objaśnienia nie mówią,
  czy w obecnym stanie prawnym można dobrowolnie zrezygnować korektą z łącznego opodatkowania (sprawdzone 2026-11-26);
  Przykład 1 opisuje korektę wspólnego zeznania na odrębne zeznania w stanie prawnym sprzed 2019 r. Kroki o wniosku
  w obu zasadach opisują to (2026-11-26) jako niewyjaśnione, z odesłaniem do tego pytania.

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
- Dalsze źródła sprawdzone 2026-11-27, bez rozstrzygnięcia:
  - Przykładowe pliki XML JPK_V7K(3) na stronie MF „pliki do pobrania”
    (https://podatki.gov.pl/media/rhvjhlbm/jpk_v7k-3-przyk%C5%82adowy-plik-w-formacie-xml.xml i
    https://podatki.gov.pl/media/hivhu0oh/jpk_v7k-3-przyk%C5%82adowy-plik-w-formacie-xml.xml) mają wariant 3, rok 2026,
    miesiąc 3 i kwartał 1; drugi z nich to korekta. Są wypełnione danymi zastępczymi i pokazują strukturę, a nie wyjaśniają,
    w którym wariancie składa się deklarację za I kwartał 2026 r.
  - Broszura MF o JPK_VAT od 1 lutego 2026 r., opis pola Miesiac: „W przypadku złożenia pierwotnego JPK_V7K, jak i korekty
    części deklaracyjnej należy wskazać ostatni miesiąc kwartału, tj. odpowiednio: 3, 6, 9, 12.” Zdanie dotyczy pola, nie wyboru
    wariantu. Strona MF „Pytania i odpowiedzi” o JPK_VAT z deklaracją nie ma pytania o wariant 3 ani o I kwartał 2026 r.

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

## P19. Na który dzień ocenia się rozliczanie VAT miesięcznie przy pierwszym przesłaniu ksiąg w formie JPK (częściowo rozstrzygnięte 2026-11-27, bez eksperta)

- Rozstrzygnięcie: MF na stronie „Pytania i odpowiedzi JPK_PD” (podatki.gov.pl, pytanie 134, dodane 12.11.2025)
  odpowiada na pytanie, na jaki moment ustala się, czy podatnik przesyła JPK_V7M czy JPK_V7K (dla ustalenia obowiązku
  przesyłania ksiąg w formie JPK). Odpowiedź nie wymienia tych plików, ale mówi, który dzień się liczy: „W dacie zaprowadzenia
  ksiąg należy zatem sprawdzić, czy księgi te muszą być prowadzone w formie elektronicznej. Jeżeli w dacie zaprowadzenia
  ksiąg wystąpi obowiązek ich prowadzenia w formie elektronicznej, to po zakończeniu roku podatkowego wystąpi również
  obowiązek ich przesyłania w formie plików JPK.” Odpowiedź mówi też, że gdy w tym dniu obowiązku nie ma, nie ma go po
  zakończeniu roku.
  Kroki obu zasad poprawione.
- Dzień zaprowadzenia: podatkową księgę przychodów i rozchodów zakłada się „na dzień 1 stycznia roku podatkowego lub na
  dzień rozpoczęcia działalności w trakcie roku podatkowego” (§ 19 rozporządzenia w sprawie prowadzenia podatkowej księgi
  przychodów i rozchodów, Dz.U. 2025 poz. 1299). Ewidencję przychodów na ryczałcie prowadzi się „odrębnie za każdy rok
  podatkowy” (art. 15 ust. 1 ustawy o ryczałcie); rozporządzenie w sprawie prowadzenia ewidencji przychodów (Dz.U. 2025
  poz. 1294) nie podaje dnia jej zaprowadzenia. Art. 15 ust. 2 ustawy o ryczałcie mówi, że „obowiązek prowadzenia
  ewidencji powstaje od dnia, od którego ma zastosowanie opodatkowanie w formie ryczałtu od przychodów ewidencjonowanych”.
  Żadne źródło nie mówi wprost, że dzień założenia księgi z § 19 ani dzień z art. 15 ust. 2 to dzień zaprowadzenia ksiąg,
  o którym mówi MF. Rozstrzygnięta jest więc zasada (liczy się dzień zaprowadzenia ksiąg),
  a nie to, który to dzień.
- Otwarte zostaje: czy dzień zaprowadzenia ksiąg w rozumieniu MF to dzień założenia księgi z § 19 rozporządzenia
  (1 stycznia albo dzień rozpoczęcia działalności)? Kiedy za zaprowadzoną uważa się ewidencję lub wykaz środków trwałych
  oraz wartości niematerialnych i prawnych? Pytanie 134 wymienia w tytule JPK_ST i JPK_ST_KR,
  ale odpowiedź tego nie mówi. Czy dniem zaprowadzenia ewidencji przychodów na ryczałcie jest dzień z art. 15 ust. 2, zarówno przy działalności
  prowadzonej od lat, jak i przy rozpoczęciu działalności w trakcie roku? Który sposób rozliczania VAT liczy się przy rozpoczęciu działalności w trakcie roku, gdy rejestracja jako czynny
  podatnik VAT zaczyna działać w innym dniu niż założenie księgi lub ewidencji? Odpowiedź MF tych
  przypadków nie omawia.

- Wpisy: `zasada.jpk_pd_pkpir` (od 2026-07-01) i `zasada.jpk_pd_ryczalt` (od 2026-01-01).
- Dotyczy też `schemat.jpk_ewp` (od 2026-01-01), ale tylko pośrednio: od odpowiedzi zależy, za który rok po raz
  pierwszy przesyła się plik JPK_EWP, a nie wariant schematu. Dlatego ten wpis nie ma otwartego pytania.
- Zgłoszone: 2026-11-26.
- Art. 66 ust. 1 ustawy z 29 października 2021 r. (Dz.U. 2021 poz. 2105, w brzmieniu z Dz.U. 2022 poz. 1265
  i Dz.U. 2023 poz. 1059): księgi i ewidencje przesyła się po raz pierwszy za rok podatkowy rozpoczynający się po
  31 grudnia 2025 r. „w przypadku podmiotów, które są obowiązane przesyłać ewidencję”, o której mowa w art. 109
  ust. 3 ustawy o VAT, zgodnie z art. 109 ust. 3b (rozliczenie miesięczne), a pozostali za rok rozpoczynający się
  po 31 grudnia 2026 r. Przepis nie mówi, na który dzień albo za który okres ocenia się ten obowiązek.
- Pytania pierwotne (stan sprzed rozstrzygnięcia; otwarte zostają tylko pytania z punktu „Otwarte zostaje”): czy obowiązek
  przesłania księgi lub ewidencji za 2026 r. ma podatnik, który w 2026 r. zmienił rozliczenie
  VAT z kwartalnego na miesięczne (albo odwrotnie)? Czy ma go podatnik, który w trakcie 2026 r. zarejestrował się
  jako czynny podatnik VAT rozliczający się miesięcznie? Czy liczy się stan na początek roku, na koniec roku, czy
  którykolwiek miesiąc roku?
- Przeszukane źródła (2026-11-26), bez rozstrzygnięcia: broszury MF o JPK_PKPIR(3) i JPK_EWP(4), strona MF o JPK_PD (kto przekazuje; bez strony pytań i odpowiedzi)
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
- Dalsze źródła sprawdzone 2026-11-27, bez rozstrzygnięcia:
  - Interpretacja indywidualna z 6 listopada 2026 r., sygn. 0114-KDIP2-2.4010.422.2026.1.RK
    (https://eureka.mf.gov.pl/informacje/podglad/718200), wiąże tylko wnioskodawcę: „korekta „wstecz” może być dokonana jedynie
    wtedy, gdy przyczyną korekty jest błąd rachunkowy lub inna oczywista omyłka”. Dotyczy podatku CIT (art. 12 ust. 3j ustawy
    o CIT) i korekty niewynikającej z błędu, nie ewidencji przychodów ani sposobu zapisu.

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
- Dalsze źródła sprawdzone 2026-11-27, bez rozstrzygnięcia:
  - Interpretacja indywidualna Dyrektora Izby Skarbowej w Warszawie z 10 stycznia 2012 r., sygn. IPPB1/415-971/11-4/JB
    (https://eureka.mf.gov.pl/informacje/podglad/318624), wiąże tylko wnioskodawcę: „wystawienie faktury przed datą wydania
    towaru, zbycia prawa lub wykonania usługi (…) – datą powstania przychodu będzie w tym przypadku dzień wystawienia faktury”.
    Stan prawny z 2012 r., faktura była zapłacona z góry, sprawa dotyczy PIT, nie ryczałtu.

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
- Dalsze źródła sprawdzone 2026-11-27, bez rozstrzygnięcia:
  - Interpretacja indywidualna KIS z 27 kwietnia 2026 r., sygn. 0115-KDIT1.4011.230.2026.2.MN
    (https://eureka.mf.gov.pl/informacje/podglad/688926), wiąże tylko wnioskodawcę na ryczałcie (przychód z programu
    motywacyjnego): „przeliczenia tej wartości na złote należy zatem dokonać według kursu średniego NBP z ostatniego dnia
    roboczego poprzedzającego dzień uzyskania przychodu”. Organ nie podaje przepisu ustawy o ryczałcie, który odsyła
    do art. 11a ustawy o PIT.

## P39. Deklaracja ZUS DRA za miesiąc, w którym działalność zawieszono w trakcie miesiąca

- Wpis: `zasada.dra_obowiazek` (od 2024-11-01), krok o zawieszeniu działalności.
- Zgłoszone: 2026-11-26.
- Ustawa o systemie ubezpieczeń społecznych (Dz.U. 2026 poz. 1474), art. 36a ust. 3: „Za okres zawieszenia wykonywania
  działalności gospodarczej przedsiębiorca będący płatnikiem składek wyłącznie za siebie nie ma obowiązku składania
  deklaracji rozliczeniowej”. Art. 36a ust. 2: obowiązek ubezpieczeń społecznych ustaje od dnia rozpoczęcia zawieszenia
  do dnia poprzedzającego wznowienie. Art. 46 ust. 1 i art. 47 ust. 1 każą rozliczać składki i przesyłać deklarację
  za każdy miesiąc kalendarzowy.
- Materiał (portal, nie rozstrzyga): biznes.gov.pl, „Jak składać deklaracje i raporty ZUS”
  (https://www.biznes.gov.pl/pl/portal/00287): „Co do zasady deklaracje ZUS DRA i raporty imienne: ZUS RCA i ZUS RSA
  składasz co miesiąc. Dotyczy to cię, jeżeli: […] zawieszasz lub wznawiasz działalność gospodarczą.” Ta sama strona:
  „Jeśli wznawiasz działalność w trakcie miesiąca, deklarację ZUS DRA
  składasz za niepełny okres rozliczeniowy i drugą - za kolejny pełny miesiąc.” Strona nie opisuje zawieszenia
  od połowy miesiąca ani składki zdrowotnej za taki miesiąc.
- Pytanie: czy płatnik składek wyłącznie za siebie, który zawiesza działalność od dnia innego niż pierwszy dzień miesiąca,
  składa deklarację rozliczeniową za ten miesiąc za dni przed zawieszeniem? Jak wykazuje w niej składkę zdrowotną
  za ten miesiąc?
- Dalsze źródła sprawdzone 2026-11-27, bez rozstrzygnięcia:
  - Poradnik ZUS „ABC płatnika składek – jednoosobowa działalność gospodarcza” (kwiecień 2026,
    https://www.zus.pl/documents/10182/167561/ABC_platnika_skladek_skladki_na_ubezpieczenia_wlasne.pdf/cd145d00-c406-48b9-991a-4a427769282a):
    „Składki rozliczaj i opłacaj za każdy miesiąc, w którym jako płatnik byłeś zgłoszony do ubezpieczeń przez przynajmniej
    jeden dzień.” O składce zdrowotnej: „Nawet jeśli wykonywałeś działalność gospodarczą przez część miesiąca (…) składka
    na to ubezpieczenie nie zmniejsza się proporcjonalnie.” Rozdział o zawieszeniu mówi tylko o wyrejestrowaniu i nie omawia
    deklaracji za miesiąc rozpoczęcia zawieszenia.
  - Ustawa o świadczeniach opieki zdrowotnej, art. 79 ust. 2: „Składka jest miesięczna i niepodzielna, z zastrzeżeniem
    art. 79a oraz art. 81 ust. 2 i 2e.” Przepis nie wymienia zawieszenia.

## P40. Wzór ZUS DRA dla deklaracji za kwiecień 2026 r. złożonej przed 1 maja 2026 r.

- Wpis: `schemat.zus_dra` (od 2026-05-01), notatka.
- Zgłoszone: 2026-11-26.
- Rozporządzenie Ministra Rodziny, Pracy i Polityki Społecznej z 9 kwietnia 2026 r. (Dz.U. 2026 poz. 518): weszło w życie
  30 kwietnia 2026 r. (§ 8, 14 dni od ogłoszenia 15 kwietnia), a § 4 ust. 2 stanowi: „W okresie od dnia wejścia w życie
  rozporządzenia do dnia 30 kwietnia 2026 r. w przypadku przekazywania deklaracji rozliczeniowej – o symbolu ZUS DRA,
  stosuje się dokument, którego wzór stanowi załącznik nr 26 do rozporządzenia.” Wzór z załącznika nr 16 obowiązuje
  od 1 maja 2026 r. (§ 8), także dla dokumentów za wcześniejsze okresy (§ 6). Do 29 kwietnia 2026 r. obowiązywało
  rozporządzenie z 20 grudnia 2020 r. (Dz.U. 2025 poz. 1036 i 1781), które § 7 uchyla.
- Komunikat ZUS „Od 1 maja 2026 r. obowiązują nowe wzory formularzy ZUS DRA i ZUS RCA”
  (https://www.zus.pl/-/od-1-maja-2026-r.-obowi%C4%85zuj%C4%85-nowe-wzory-formularzy-zus-dra-i-zus-rca): nową metrykę
  programu Płatnik z nowymi wzorami ZUS udostępnił 24 kwietnia 2026 r.; „Możliwe jest sporządzanie i przekazanie rozliczeń
  na nowych wzorach formularzy przed ich oficjalnym terminem obowiązywania tj. 1 maja 2026 r.”, a „Rozliczenie składek za kwiecień 2026 r. przekazane na „starych”
  formularzach będą wymagały skorygowania.”
- Pytanie: który wzór stosuje się do deklaracji rozliczeniowej za kwiecień 2026 r. złożonej przed 1 maja 2026 r.:
  do 29 kwietnia wzór z rozporządzenia z 2020 r., a 30 kwietnia wzór z załącznika nr 26 (brzmienie rozporządzenia), czy
  wzór z załącznika nr 16 (stanowisko ZUS)?

## P41. Który wzór elektroniczny zeznania PIT stosuje się, gdy MF opublikowało kilka wersji schematu za ten sam rok

- Wpisy: `schemat.pit_36` (za 2025 i za 2026 r.), `schemat.pit_28` (za 2025 i za 2026 r.).
- Zgłoszone: 2026-11-26.
- W Centralnym Repozytorium Wzorów Dokumentów Elektronicznych (CRWDE, ePUAP) Ministerstwo Finansów opublikowało
  dla tego samego wariantu i roku podatkowego po dwa wzory z różnymi wersjami schematu:
  - PIT-36(32) za 2025 r.: wzór 2025/09/24/13871 (wersja schematu 1-0E) i 2026/09/11/14368 (2-0E); oba wyróżniki
    podają, że wzór „stosuje się do uzyskanych dochodów lub poniesionych strat od dnia 1 stycznia 2025 r.”;
  - PIT-36(32) za 2026 r.: wzór 2026/09/16/14376 (3-0E) i 2026/10/13/14405 (3-1E);
  - PIT-28(27): wzór 2025/09/11/13849 (1-0E) i 2025/10/10/13916 (1-1E);
  - PIT-28(28): wzór 2026/09/10/14364 (1-0E) i 2026/09/14/14369 (1-1E).
- Porównanie plików XSD (diff), poza przestrzenią nazw wzoru: 14368 różni się od 13871 wersją schematu i opisem
  jednego pola (numery pozycji 293 i 294 zamiast 283 i 284); 14405 od 14376 wersją schematu i jednym warunkiem
  unikalności identyfikatora; 13916 od 13849 wersją schematu, usunięciem dwóch warunków „większe od zera”
  i najwcześniejszym dopuszczalnym rokiem w jednym polu; 14369 od 14364 tylko wersją schematu.
  Wpisy podają wzór opublikowany najpóźniej.
- Wyróżniki PIT-36(32) za 2025 r.: wzór 13871 podpisano 24 września 2025 r., a wzór 14368 11 września 2026 r.;
  oba mają ważność od 24 lipca 2025 r. Nie wiadomo, czy wzór 14368 dotyczy też zeznań i korekt złożonych przed
  jego publikacją ani według którego wzoru składa się teraz korektę zeznania za 2025 r.
- Strona MF „Struktury dokumentów XML” (podatki.gov.pl, e-Deklaracje, Dokumentacja IT) odsyła do CRWDE, a wzory
  zeznań PIT-28, PIT-36 i PIT-36L na jej liście kończą się na latach 2021–2023. Żadne źródło urzędowe nie mówi, który z tych wzorów system e-Deklaracji przyjmuje
  i czy wcześniejszy przestaje być przyjmowany po publikacji nowszego.
- Pytanie: który wzór (wersję schematu) stosuje się przy składaniu zeznania i korekty za dany rok, gdy w CRWDE są
  dwa wzory tego samego wariantu? Czy MF publikuje gdzieś aktualną listę wzorów przyjmowanych przez e-Deklaracje?

## P42. Kwota przychodu w danych autoryzujących przy kilku zeznaniach za rok sprzed dwóch lat

- Wpis: `zasada.dane_autoryzujace` (wersje od 2026-04-01 i od 2026-06-16), kroki 2 i 3.
- Zgłoszone: 2026-11-26.
- Rozporządzenie w sprawie sposobu przesyłania deklaracji i podań (Dz.U. 2025 poz. 327, § 12 ust. 2 pkt 5)
  i rozporządzenie w sprawie sposobu przesyłania ksiąg podatkowych (Dz.U. 2025 poz. 461, § 2 ust. 2a pkt 5):
  dane autoryzujące obejmują „wysokość przychodu wykazanego odpowiednio w” zeznaniu PIT-28, PIT-36, PIT-36L,
  PIT-37, PIT-38, PIT-39 albo w rocznym obliczeniu PIT-40A za rok podatkowy o dwa lata wcześniejszy niż rok
  przesyłania, albo zero, gdy nie złożono żadnego z nich.
- Odpowiedzi MF o e-Deklaracjach (podatki.gov.pl): gdy za tamten rok nie złożono zeznania „na analogicznym
  formularzu”, ale rozliczano się na innym z wymienionych, podaje się kwotę z tamtego zeznania, a nie zero. MF podaje też
  pozycje zeznań, z których bierze się kwotę, dla kolejnych wzorów.
- Żadne z tych źródeł nie mówi, którą kwotę podać, gdy za tamten rok podatnik złożył kilka z wymienionych zeznań
  (na przykład PIT-36L i PIT-38 albo PIT-28 i PIT-38). Przy plikach JPK (JPK_V7M, JPK_EWP, JPK_PKPIR) nie ma
  „analogicznego formularza”.
- Pytanie: którą kwotę przychodu podaje się w takim przypadku przy zeznaniu PIT i przy plikach JPK? Czy można podać
  kwotę z dowolnego ze złożonych zeznań?
- Dalsze źródła sprawdzone 2026-11-27, bez rozstrzygnięcia:
  - Instrukcja MF do interaktywnych formularzy PDF, wersja 1.19 ze stycznia 2024 r.
    (https://www.podatki.gov.pl/media/xsndcdg0/instrukcja-korzystania-z-formularzy-interaktywnych-pdf-wersja-1-19_tk-1.pdf):
    w polu „Kwota przychodu” podatnik wykazuje „kwotę (sumę) przychodów wynikających z dowolnego zeznania lub rozliczenia
    rocznego za rok 2022”. Instrukcja dotyczy deklaracji składanych w 2024 r. i nie mówi o plikach JPK.

## P43. Przychód na ryczałcie w polach ZUS DRA XI 13 i XII 22: pomniejszony o składki czy bez pomniejszenia

- Wpis: `zasada.dra_bloki_zdrowotne` (od 2026-05-01), kroki 3 i 6.
- Zgłoszone: 2026-11-27.
- Ustawa o świadczeniach opieki zdrowotnej (Dz.U. 2025 poz. 1461), art. 81 ust. 2g: „Przychody, o których mowa
  w ust. 2e i 2f, są pomniejszane o kwoty opłaconych składek na ubezpieczenia emerytalne, rentowe, chorobowe
  i wypadkowe”, jeżeli nie zostały zaliczone do kosztów ani odliczone od dochodu. Od tak pomniejszonego przychodu
  zależy próg, a więc podstawa i składka.
- Wzór ZUS DRA (załącznik nr 16 do rozporządzenia Dz.U. 2026 poz. 518) w poradniku ZUS „ZUS DRA. Deklaracja
  rozliczeniowa. Jak wypełnić i skorygować” (maj 2026): pole XI 13 „Suma przychodów w bieżącym roku kalendarzowym”,
  przypis 9: „Kwota przychodów osiągniętych od początku roku kalendarzowego do końca miesiąca, za który dokonywane
  jest rozliczenie”; pole XII 22 „Kwota przychodów osiągniętych z działalności gospodarczej w roku, którego dotyczy
  roczne rozliczenie”. Przy polu XI 15 (przychód z poprzedniego roku) przypis 10 odsyła do art. 81 ust. 2h, który
  wprost mówi o przychodzie pomniejszonym o składki.
- Poradnik przy polach XI 13 i XII 22 nie wspomina o pomniejszeniu. W przykładach na ryczałcie pole XI 13
  (wspólnik spółki cywilnej) i pole XII 22 (przedsiębiorca korzystający ze zwolnienia ze składki) zawierają sumę
  przychodów podaną w opisie przykładu, a opisy nie mówią o składkach. Ten sam poradnik w opisie rocznej podstawy
  na ryczałcie podaje: „Roczną podstawę ustalasz w oparciu o łączną kwotę przychodów z działalności gospodarczej.
  Odejmujesz od tego opłacone składki na ubezpieczenia emerytalne, rentowe, chorobowe i wypadkowe.”
- Pytanie: czy w polach XI 13 i XII 22 wpisuje się przychód pomniejszony o składki z art. 81 ust. 2g, czy przychód
  bez pomniejszenia (a pomniejszenie uwzględnia się tylko przy ustalaniu progu)?
- Dalsze źródła sprawdzone 2026-11-27, bez rozstrzygnięcia:
  - FAQ ZUS „Zmiany od 2022 r.” (https://www.zus.pl/o-zus/o-nas/programy-transformacji-cyfrowej-zus/zmiany-od-2022-r./faq):
    „Dla osób opodatkowanych ryczałtem przy wyliczeniu składki zdrowotnej ustala się wysokość przychodów z uwzględnieniem
    pomniejszenia o opłacone składki na ubezpieczenia społeczne.” oraz „Progi kwotowe odnoszą się do przychodów pomniejszonych
    o kwoty opłaconych składek”. Oba zdania dotyczą wyliczenia i progów, nie tego, co wpisać w pola XI 13 i XII 22.
  - Dokumentacja programu Płatnik (wersja 8.6) opisuje pole „Suma przychodów w bieżącym roku kalendarzowym” bez wzmianki
    o pomniejszeniu. Wprost o pomniejszeniu w polu XI 13 pisze tylko portal poradnikprzedsiebiorcy.pl (źródło kontrolne).

## P44. Które składki pomniejszają przychód na ryczałcie: zapłacone w okresie czy należne za jego miesiące

- Wpisy: `zasada.dra_bloki_zdrowotne` (od 2026-05-01), kroki 3 i 6; `zasada.ryczalt_zdrowotna_prog` (wersje
  od 2025-01-01 i od 2027-01-01), kroki 1 i 5.
- Zgłoszone: 2026-11-27.
- Ustawa o świadczeniach opieki zdrowotnej (Dz.U. 2025 poz. 1461): art. 81 ust. 2g pomniejsza przychody
  z ust. 2e (roczne) i 2f (od początku roku) o „kwoty opłaconych składek” bez wskazania, w jakim okresie zostały
  opłacone; art. 81 ust. 2h przy przychodzie z poprzedniego roku mówi o składkach „opłaconych w poprzednim roku
  kalendarzowym”.
- Poradnik ZUS „ZUS DRA…” (maj 2026) przy rocznym rozliczeniu na ryczałcie: „Odejmujesz od tego opłacone składki
  na ubezpieczenia emerytalne, rentowe, chorobowe i wypadkowe”; przy skali podatkowej mówi o składkach
  „zapłaconych od początku roku”. Składki za dany miesiąc są płatne w następnym miesiącu (termin.zus), więc obie
  kwoty różnią się zwykle o składki za jeden miesiąc.
- Pytanie: czy przy ustalaniu przychodu od początku roku (art. 81 ust. 2f) i przychodu rocznego (art. 81 ust. 2e)
  odejmuje się składki faktycznie zapłacone w tym okresie (według dnia zapłaty), czy składki należne za miesiące
  tego okresu? Jak traktuje się składki za grudzień zapłacone w styczniu następnego roku?

## P45. Kwota do zwrotu w rocznym rozliczeniu (ZUS DRA, pole XII 27): składki należne czy wpłacone

- Wpisy: `zasada.dra_bloki_zdrowotne` (od 2026-05-01), krok 7; `zasada.ryczalt_zdrowotna_prog` (wersje od 2025-01-01
  i od 2027-01-01), krok 5.
- Zgłoszone: 2026-11-27.
- Ustawa o świadczeniach opieki zdrowotnej (Dz.U. 2025 poz. 1461): niedopłatę liczy się jako różnicę między roczną
  składką „a sumą składek na ubezpieczenie zdrowotne wynikającą ze złożonych dokumentów za poszczególne miesiące”
  (art. 81 ust. 2j), a zwrot jako różnicę, w której występuje „suma wpłaconych za poszczególne miesiące roku
  składkowego albo roku kalendarzowego” składek (art. 81 ust. 2i).
- Wzór ZUS DRA (w poradniku ZUS „ZUS DRA…”, maj 2026): pole XII 25 „Suma miesięcznych należnych składek wynikająca
  ze złożonych dokumentów za rok, którego dotyczy roczne rozliczenie”, pole 26 „Kwota do dopłaty (p. 24 – p. 25)”,
  pole 27 „Kwota do zwrotu (p. 25 – p. 24)”, z przypisem 17: „Wypełnij, jeśli składka roczna jest mniejsza od sumy
  miesięcznych należnych składek wynikających ze złożonych dokumentów za rok, którego dotyczy roczne rozliczenie.”
  Analogicznie pola 10–12 (skala) i 18–20 (podatek liniowy).
- W przykładzie z poradnika (ryczałt, zwolnienie ze składki przez część roku) opis porównuje roczną składkę
  z „opłaconymi składkami”, a w polu 25 wpisuje kwotę składek opłaconych za te miesiące; przykład nie pokazuje
  przypadku, w którym składki należne i wpłacone się różnią.
- Pytanie: gdy suma składek należnych za miesiące roku różni się od sumy składek faktycznie wpłaconych za te miesiące
  (na przykład składka za jeden miesiąc nie została zapłacona albo zapłacono więcej), od której z nich ustala się
  kwotę do zwrotu w polu 27? Czy pole 25 zawsze zawiera składki należne, także przy nadpłacie?

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
- Dalsze źródła sprawdzone 2026-11-27, bez rozstrzygnięcia:
  - Interpretacja indywidualna Dyrektora Izby Skarbowej w Katowicach z 19 grudnia 2016 r., sygn. 2461-IBPB-1-1.4511.577.2016.1.WRz
    (https://eureka.mf.gov.pl/informacje/podglad/328874), wiąże tylko wnioskodawcę: po utracie prawa do podatku liniowego
    (art. 9a ust. 3) „dokonany 11 stycznia 2015 r. wybór formy opodatkowania nie jest już skuteczny w następnych latach
    podatkowych”. Wydana według dawnego art. 9a ust. 4; nie dotyczy ryczałtu.
  - Interpretacja indywidualna KIS z 18 czerwca 2026 r., sygn. 0115-KDST2-1.4011.303.2026.1.NC
    (https://eureka.mf.gov.pl/informacje/podglad/696705), wiąże tylko wnioskodawcę: po utracie ryczałtu z powodu przekroczenia
    limitu z art. 6 ust. 4 przelew opisany „PIT28” „może być uznany za skutecznie złożone oświadczanie o wyborze formy
    opodatkowania, o którym mowa w art. 9 ust. 1”. Nie dotyczy art. 8 ust. 2 i 3 ani nie rozstrzyga, czy wcześniejszy wybór
    przechodzi na kolejny rok.

## P56. Zaliczki i ryczałt za miesiąc lub kwartał, w którego trakcie zawieszono albo wznowiono działalność

- Wpis: `zasada.zaliczki_zawieszenie` (od 2026-01-01), kroki o zaliczkach na PIT i o okresie częściowym.
- Zgłoszone: 2026-11-26.
- Ustawa o PIT (Dz.U. 2026 poz. 592), art. 44 ust. 10: podatnik, który zawiesił działalność, „jest zwolniony, w zakresie
  tej działalności, z obowiązków wynikających z ust. 1 pkt 1, ust. 3, 3f, 3g, 6 i 6b za okres objęty zawieszeniem”;
  ust. 13: po zawieszeniu podatnicy „wpłacają zaliczki według zasad, o których mowa w ust. 3, 3f, 3g, 6 i 6b”.
  Oba przepisy nie wymieniają ust. 3h (zaliczki kwartalne przy podatku liniowym).
- Ustawa o ryczałcie (Dz.U. 2025 poz. 843), art. 21 ust. 1d: zwolnienie z obowiązków z ust. 1 lub 1a „za okres objęty
  zawieszeniem”; ust. 1g: ryczałt „dotyczący okresu zawieszenia” wpłaca się po wznowieniu.
- Prawo przedsiębiorców (Dz.U. 2026 poz. 1484), art. 24 ust. 7: wobec zobowiązań publicznoprawnych zawieszenie działa
  od dnia rozpoczęcia zawieszenia do dnia poprzedzającego dzień wznowienia, a więc może obejmować część miesiąca.
- biznes.gov.pl (Podatki przy zawieszeniu, wznowieniu i likwidacji działalności, aktualizacja 20.10.2026) podaje w przykładzie,
  że przy zawieszeniu od 16 marca zaliczkę za przychody sprzed zawieszenia wpłaca się w zwykłym terminie; strona portalu
  nie rozstrzyga tej kwestii.
- Pytania: jak ustala się i kiedy wpłaca zaliczkę na PIT (skala, podatek liniowy) oraz ryczałt za miesiąc albo kwartał,
  w którego trakcie zawieszenie się zaczęło albo skończyło? Czy przychód z części miesiąca sprzed zawieszenia rozlicza się
  w zwykłym terminie, a na ryczałcie przychód z części okresu objętej zawieszeniem dopiero po wznowieniu? Czy zwolnienie
  z art. 44 ust. 10 obejmuje zaliczki kwartalne przy podatku liniowym (ust. 3h), skoro przepis wymienia ust. 1 pkt 1,
  ale nie ust. 3h?
- Dalsze źródła sprawdzone 2026-11-27, bez rozstrzygnięcia:
  - Ustawa o ryczałcie (Dz.U. 2025 poz. 843), art. 21 ust. 1h–1j: przy wznowieniu w ostatnim miesiącu (kwartale) roku ryczałt
    za okres zawieszenia wpłaca się „w terminie do dnia 20 stycznia następnego roku podatkowego”; gdy wznowienie następuje
    w następnym roku albo dwa lata później, ryczałt za okres zawieszenia w każdym wcześniejszym roku wpłaca się do 20 stycznia
    roku następującego po tym roku, a za rok wznowienia na zasadach z ust. 1g i 1h. Przepisy dotyczą terminu wpłaty za okres
    zawieszenia, nie przychodu z części miesiąca lub kwartału, i nie dotyczą PIT.

## P57. Faktury poza KSeF do 10 000 zł miesięcznie w 2026 r.: czy prawo wraca w kolejnym miesiącu (rozstrzygnięte 2026-11-27, bez eksperta)

- Rozstrzygnięcie: wyjaśnienia MF na ksef.podatki.gov.pl podają wprost, że prawo nie wraca. Wyjaśnienie „Co warto
  wiedzieć przed startem II etapu wdrożenia Krajowego Systemu e-Faktur” (31.03.2026): „Po przekroczeniu limitu nie wracasz
  już do poprzednich zasad, nawet jeśli w kolejnych miesiącach wartość sprzedaży dokumentowana fakturami będzie niższa.”
  „Najczęstsze pytania”, pytanie 14 (strona opublikowana 15.04.2026, zmieniona 29.04.2026): obowiązek „powstaje od faktury, którą limit został przekroczony, oraz dla
  wszystkich kolejnych faktur. Późniejsze nieprzekroczenie limitu (np. w czerwcu) nie ma już znaczenia.” Zgadza się to
  z art. 145m ust. 2 i z uzasadnieniem projektu. Strona „Zakres obowiązkowego KSeF” nadal pomija ust. 2, a komunikat
  z 26.03.2026 nie mówi nic o przekroczeniu limitu; oba upraszczają, ale nie przeczą wyjaśnieniom. Krok zasady poprawiony,
  P57 usunięty z otwartych pytań. Opis poniżej to stan sprzed rozstrzygnięcia.

- Wpis: `zasada.ksef_obowiazek` (2026-02-01 – 2026-12-31), krok o art. 145m.
- Zgłoszone: 2026-11-26.
- Ustawa o VAT (Dz.U. 2026 poz. 1263), art. 145m ust. 1: od 1 kwietnia do 31 grudnia 2026 r. podatnik może wystawiać
  faktury elektroniczne lub papierowe, jeżeli łączna wartość sprzedaży z podatkiem „udokumentowana tymi fakturami
  wystawionymi w danym miesiącu jest mniejsza lub równa 10 000 zł”; ust. 2: podatnik „traci prawo do wystawiania faktur
  elektronicznych oraz faktur w postaci papierowej począwszy od faktury, którą przekroczono wartość”.
- Uzasadnienie projektu ustawy Dz.U. 2025 poz. 1203 (druk sejmowy nr 1407, w projekcie art. 145o): „jeżeli w danym miesiącu
  faktury nie spełnią wskazanego wyżej warunku, podatnik nie może ponownie skorzystać z możliwości wystawiania faktur
  w postaci papierowej lub faktur elektronicznych”. Uzasadnienie nie jest źródłem prawa.
- Strona MF ksef.podatki.gov.pl „Zakres obowiązkowego KSeF”
  (https://ksef.podatki.gov.pl/informacje-ogolne-ksef-20/zakres-obowiazkowego-ksef/) podaje próg w dwóch ujęciach.
  W opisie terminów: podatnicy, u których „wartość sprzedaży dokumentowana fakturami za okresy miesięczne nie przekracza
  kwoty 10 000 zł (brutto)”, do końca 2026 r. „nie mają obowiązku wystawiania faktur w KSeF”. W punkcie o przepisach
  epizodycznych powtarza prawie dosłownie art. 145m ust. 1 (podatnicy „mogą wystawiać faktury elektroniczne lub faktury
  w postaci papierowej”). Art. 145m ust. 2 (utrata prawa od faktury, którą przekroczono wartość) strona pomija.
  Komunikat MF z 26.03.2026 (https://www.podatki.gov.pl/aktualnosci/drugi-etap-wdrozenia-krajowego-systemu-e-faktur-260326/) podaje, że tacy podatnicy „Będą oni wystawiać faktury w KSeF dopiero od 1 stycznia
  2027 r.”. Źródła się różnią.
- Pytania: czy podatnik, który w danym miesiącu 2026 r. przekroczył 10 000 zł, może w kolejnym miesiącu znów wystawiać
  faktury poza KSeF, jeżeli w tym miesiącu nie przekroczy tej wartości? Czy po przekroczeniu traci prawo od faktury, którą
  przekroczono wartość (art. 145m ust. 2), czy, jak opisuje strona MF, próg oznacza brak obowiązku do końca 2026 r.?

## P64. IP Box: odliczenie kosztów kwalifikowanych od dochodu z kwalifikowanego prawa (art. 30ca ust. 9a)

- Wpis: `zasada.ip_box` (od 2026-01-01), krok o odliczeniu kosztów kwalifikowanych; `zasada.ulga_br` (od 2026-01-01), krok o podstawie odliczenia i krok o przepisach, których zasada nie opisuje.
- Zgłoszone: 2026-11-26.
- Ustawa o PIT (Dz.U. 2026 poz. 592), art. 30ca ust. 9a: „Od dochodu z kwalifikowanego prawa własności intelektualnej
  podatnik może odliczyć koszty kwalifikowane określone w art. 26e ust. 2–3b, które doprowadziły do wytworzenia,
  rozwinięcia lub ulepszenia przez podatnika tego prawa, przy czym przepisy art. 26e ust. 1 zdanie drugie i ust. 3c–10
  stosuje się odpowiednio.” Ustęp dodała ustawa Dz.U. 2021 poz. 2105 (art. 1 pkt 55 lit. b), od 1 stycznia 2022 r.
- Art. 30ca ust. 4: kwalifikowany dochód to iloczyn „dochodu z kwalifikowanego prawa własności intelektualnej”
  i wskaźnika; ust. 3: podstawą opodatkowania jest suma kwalifikowanych dochodów.
- Objaśnienia podatkowe MF z 15 lipca 2019 r. (IP Box), akapit 151, wydane przed dodaniem ust. 9a: „ulga B+R
  nie podlega uwzględnieniu w obliczeniu podstawy opodatkowania podlegającej 5% podatkowi z IP Box”, a podatnik
  nie może stosować obu preferencji do tego samego dochodu. Strony podatki.gov.pl o IP Box (aktualizacja 24.06.2026)
  i o uldze badawczo-rozwojowej (aktualizacja 23.11.2026) nie opisują ust. 9a.
- Ustawa o PIT, art. 26i ust. 1: „Podstawa obliczenia podatku ustalona zgodnie z art. 26 ust. 1, art. 30c ust. 2 lub
  art. 30ca ust. 3 oraz po uprzednim odliczeniu kwot określonych w art. 26e […]”. Art. 26e ust. 1 w tekście jednolitym
  z 2026 r. nadal odsyła tylko do podstawy ustalonej zgodnie z „art. 26 ust. 1 lub art. 30c ust. 2”, a ust. 9a przewiduje
  odliczenie od dochodu z kwalifikowanego prawa, a nie od podstawy.
- Pytania: czy odliczenie z ust. 9a pomniejsza dochód z kwalifikowanego prawa przed pomnożeniem przez wskaźnik
  z ust. 4, czy kwalifikowany dochód po pomnożeniu? Czy akapit 151 objaśnień MF jest po 2021 r. nadal aktualny?
  Czy art. 26i ust. 1 oznacza, że kwoty z art. 26e odlicza się także od podstawy z art. 30ca ust. 3, czy tylko opisuje
  kolejność wobec odliczenia z ust. 9a?
- Dalsze źródła sprawdzone 2026-11-27, bez rozstrzygnięcia:
  - Formularz PIT/IP(5) (https://podatki.gov.pl/media/litajg0p/pit_ip_-5-02.pdf), wariant wskazany przez MF na lata 2023
    i 2024: poz. 18 „Dochody z kwalifikowanych praw”, poz. 19 „Odliczenie zmniejszające dochód z kwalifikowanego prawa
    z tytułu kosztów uzyskania przychodów poniesionych na działalność badawczo-rozwojową, które doprowadziły do wytworzenia,
    rozwinięcia lub ulepszenia przez podatnika tego prawa”, poz. 20 „Kwalifikowany dochód (dochody) z kwalifikowanych praw
    obliczony (obliczone) zgodnie z art. 30ca ust. 4 ustawy”. Objaśnienia nie mówią, czy odliczenie z poz. 19 stosuje się
    przed wskaźnikiem z ust. 4, czy po nim; kolejność wynika tylko z układu pozycji. Na lata 2025 i 2026 MF nie podaje
    wariantu tego formularza.

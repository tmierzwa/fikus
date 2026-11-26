# Pytania do eksperta

Pytania, na które źródła nie dają jednoznacznej odpowiedzi. Opiekun przekazuje je doradcy podatkowemu
albo biuru rachunkowemu, a odpowiedź (imię, data, podstawa) trafia do pola `verification.expert`
wpisu. Do czasu odpowiedzi wpis ma `open_issue` i pewność niską.

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
  - Niesprawdzone: decyzje Prezesa NFZ (art. 109a), orzeczenia sądów administracyjnych (CBOSA).

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
  wprost tylko materiały ZUS (poradnik i strona o informacji ZUS IWA).
- Pytanie: czy dla płatnika zgłaszającego nie więcej niż 9 ubezpieczonych stopa w latach składkowych
  2025/2026 i 2026/2027 wynosi 1,67%, i czy istnieje urzędowe źródło poza materiałami ZUS, które
  podaje tę stopę wprost?

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

## P6. Stawka ryczałtu bez ewidencji pozwalającej ustalić przychody z każdego rodzaju działalności

- Wpis: `zasada.ryczalt_podstawa` (od 2024-01-01), krok o stawce bez takiej ewidencji.
- Zgłoszone: 2026-11-26.
- Ustawa o zryczałtowanym podatku dochodowym (Dz.U. 2025 poz. 843), art. 12 ust. 3 zdanie drugie: gdy
  ewidencja nie pozwala ustalić przychodów z każdego rodzaju działalności, „ryczałt od przychodów
  ewidencjonowanych wynosi 8,5 % przychodów, z tym że w przypadku osiągania również przychodów”
  z ust. 1 pkt 1, 2, 2a, 2b, 3 albo 4 wynosi odpowiednio 17, 15, 14, 12, 10 albo 12,5%.
- Pytania: czy stawkę podwyższoną stosuje się do wszystkich przychodów, czy tylko do przychodów z danego
  punktu? Którą stawkę stosuje się, gdy podatnik ma przychody z kilku z tych punktów?

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
  kolejnego miesiąca”. ZUS (to samo wyjaśnienie): po rezygnacji okres liczy się od dnia objęcia ubezpieczeniami, a po
  upływie ulgi od dnia następnego po upływie 6 miesięcy kalendarzowych.
- Pytanie: jak liczyć 24 miesiące z art. 18aa ust. 1 i 3, gdy objęcie ubezpieczeniami następuje w trakcie miesiąca?

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

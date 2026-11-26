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

## P16. Wniosek o łączne opodatkowanie w zeznaniu złożonym po terminie albo w korekcie; okres samotnego wychowywania dzieci

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
  dzieci) można skutecznie wyrazić w zeznaniu złożonym po terminie z art. 45 ust. 1 albo w korekcie zeznania
  i na jakiej podstawie (art. 81 Ordynacji podatkowej?), oraz czy korektą można z niego zrezygnować?
- Art. 6 ust. 4c: sposób opodatkowania dotyczy rodzica, który „w roku podatkowym samotnie wychowuje dzieci”.
  Przepis nie mówi, czy przez cały rok. podatki.gov.pl (Osoba samotnie wychowująca dziecko) podaje, że nie
  trzeba samotnie wychowywać dziecka przez cały rok (przykład rozwodu w trakcie roku).
- Pytanie: czy warunek samotnego wychowywania dzieci jest spełniony, gdy trwał tylko przez część roku
  podatkowego, i czy można to dopisać do zasady?

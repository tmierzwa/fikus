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

## P2. Minimalna składka zdrowotna na skali i liniowym w roku składkowym 2025/2026 (rozstrzygnięte 2026-11-26, bez eksperta)

- Rozstrzygnięcie: Podatnik.info samo podaje 314,96 zł „od lutego 2025 r. do stycznia 2026 r.”; dodane jako źródło kontrolne, `open_issue` usunięty.

- Wpis: `zdrowotna.minimum` (2025-02-01 – 2026-01-31, 314,96 zł).
- Zgłoszone: 2026-11-26.
- Komunikat ZUS z 30 stycznia 2025 r. podaje 314,96 zł „za miesiące od lutego 2025 r. do stycznia 2026 r.”
  (9% z 3499,50 zł, czyli 75% minimalnego wynagrodzenia 4666 zł, art. 4 ustawy z 6 grudnia 2024 r.).
- Żadne niezależne źródło nie podaje tej kwoty za cały ten okres: komunikat ZUS z 2026 r. i ifirma
  podają ją tylko za styczeń 2026, a PITax podaje okres do grudnia 2026.
- Pytanie: czy minimalna miesięczna składka zdrowotna przedsiębiorcy na skali i na podatku liniowym
  wynosiła 314,96 zł za każdy miesiąc od lutego 2025 r. do stycznia 2026 r.?
- Zamiast eksperta wystarczą też deklaracje DRA za ten okres (podatnika na liniowym), jeśli w którymś
  miesiącu składka była minimalna. Wtedy wpis dostaje `filed_documents`.

## P3. Minimalna składka zdrowotna na skali i liniowym za styczeń 2027 (rozstrzygnięte 2026-11-26, bez eksperta)

- Rozstrzygnięcie: Poradnik Przedsiębiorcy samo podaje 432,54 zł „od lutego 2026 roku do stycznia 2027 roku” (tabela według miesięcy DRA); dodane jako źródło kontrolne, `open_issue` usunięty. Wynika to też wprost z art. 81 ust. 2 i 2d (minimalne wynagrodzenie z pierwszego dnia roku składkowego).

- Wpis: `zdrowotna.minimum` (2026-02-01 – 2027-01-31, 432,54 zł).
- Zgłoszone: 2026-11-26.
- Komunikat ZUS z 2 lutego 2026 r. podaje 432,54 zł „za miesiące od lutego 2026 r. do stycznia 2027 r.”
  (9% z 4806 zł, art. 81 ust. 2d). Źródło kontrolne (ifirma) potwierdza kwotę tylko za luty–grudzień 2026.
- Pytanie: czy minimalna składka za styczeń 2027 r. (ostatni miesiąc roku składkowego) wynosi 432,54 zł,
  mimo że od 1 stycznia 2027 r. obowiązuje nowe minimalne wynagrodzenie?

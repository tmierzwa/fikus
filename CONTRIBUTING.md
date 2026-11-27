# Jak współtworzyć Fikusa

Fikus to dane o przepisach dla JDG z dowodami, skąd pochodzi każda wartość. Najbardziej przydają się:
zgłoszenia błędów w danych, nowe wersje parametrów (na przykład stawki na kolejny rok), drugie
niezależne źródła dla wpisów z pewnością `niska` i poprawki kodu. Wpis z pewnością `średnia` ma już
komplet dowodów; podnosi go tylko rozstrzygnięcie otwartego pytania.

## Czego tu nie robimy

- Nie odpowiadamy na pytania o sytuację konkretnego podatnika („jak mam się rozliczyć”, „czy mogę
  odliczyć”). Takich porad może zawodowo udzielać tylko doradca podatkowy, adwokat, radca prawny
  albo biegły rewident (art. 2 ust. 2 i art. 3 ust. 1 ustawy o doradztwie podatkowym). Zgłoszenia
  z takim pytaniem zamykamy.
- Nie publikuj swoich danych podatkowych: kwot z deklaracji, NIP, PESEL, numerów rachunków, skanów
  dokumentów. Repozytorium i zgłoszenia są publiczne. Jeśli wartość zgadza się z Twoją deklaracją,
  napisz tylko, z jaką deklaracją i za jaki okres (pole `filed_documents`), bez kwot.
- Dane opierają się wyłącznie na źródłach publicznych i na wkładzie kontrybutorów.
- Nie dodajemy kalkulatorów, przykładów liczbowych ani formuł wykonywalnych. Serwer podaje
  wartości i opisuje zasady słowami; liczy klient.

## Zasady dla danych

Klucze i wartości pól wyliczeniowych (na przykład `kind: control`) są po angielsku, a cała treść
(notatki, kroki zasad, tytuły źródeł) po polsku, bez nazw pól w zdaniach.

Każda wersja parametru musi mieć:

1. okres obowiązywania (`valid_from`, opcjonalnie `valid_to`);
2. źródło pierwotne: tekst jednolity z ISAP/ELI, obwieszczenie w M.P., komunikat ZUS lub MF,
   z dosłownym cytatem (`quote`), z którego wynika wartość. Gdy zmiany nie ma jeszcze w tekście
   jednolitym, cytuj ustawę zmieniającą z Dz.U. obok ostatniego tekstu jednolitego;
3. pole `verification` z datą sprawdzenia.

Portale, blogi i kalkulatory mogą być tylko źródłem kontrolnym (`kind: control`). Bez źródła
pierwotnego wartość nie trafia do danych. Drugie źródło (`kind: control` albo `independent: true`)
liczy się jako dowód tylko z własnym dosłownym cytatem i tylko wtedy, gdy jest innym dokumentem
(adresem) niż źródło pierwotne z cytatem. Starych wersji nie zmieniamy; dodaj nową. Notatka opisuje
obecny stan wersji, bez historii edycji. Poprawkę błędu w starej wersji opisz w PR. Gdy zmienia wartość,
okres, podstawę prawną albo kroki zasady, dopisz w notatce jedno krótkie zdanie, na przykład „Korekta
z 27 listopada 2026 r.: zmienione kroki 2 i 4.”, bez opisu poprzedniego błędu.

Gdy źródła się różnią albo przepis wymaga interpretacji, nie zgaduj. Wpisz `open_issue` i dopisz
pytanie w [docs/pytania-do-eksperta.md](docs/pytania-do-eksperta.md). Gdy pytanie dotyczy tylko przypadku
brzegowego, a nie samej wartości ani rdzenia zasady, a krok opisuje ten przypadek jako niewyjaśniony, dopisz `open_issue_scope: edge_case`; w razie wątpliwości go nie wpisuj.
Odpowiedź eksperta zapisujemy w `verification.expert` z datą i podstawą. Imię i nazwisko eksperta
wpisujemy tylko za jego zgodą na publikację; bez zgody wpisujemy samą kwalifikację, na przykład „doradca podatkowy”.

## Odpowiedzi ekspertów

Otwarte pytania mają dyskusje w kategorii
[Pytania do ekspertów](https://github.com/tmierzwa/fikus/discussions/categories/pytania-do-ekspert%C3%B3w),
jedna dyskusja na jedno pytanie z [docs/pytania-do-eksperta.md](docs/pytania-do-eksperta.md). Jeśli jesteś
doradcą podatkowym, księgową albo prawnikiem, odpowiedz w dyskusji i podaj podstawę prawną: przepis,
interpretację, wyrok albo komunikat urzędu.

Sama odpowiedź w dyskusji nie jest jeszcze dowodem. Opiekun potwierdza Twoją kwalifikację i to, że
odpowiedź podaje podstawę, a potem oznacza ją jako odpowiedź. Wtedy trafia do danych z datą, podstawą
i linkiem do Twojego komentarza. Twoje imię i nazwisko wpiszemy tylko wtedy, gdy napiszesz w dyskusji,
że się na to zgadzasz. Login na GitHubie nie jest taką zgodą. Bez niej wpisujemy samą kwalifikację.

W dyskusjach obowiązują te same zasady co w zgłoszeniach: nie wpisujemy kwot z deklaracji, NIP, PESEL
ani informacji o tym, kto jak się rozlicza, a pytania o własne rozliczenie zamykamy.

Szczegółowy opis pól jest w [src/fikus/model.py](src/fikus/model.py), a procedura dla agentów w
[CLAUDE.md](CLAUDE.md) i `.claude/skills/dodaj-parametr/`.

## Jak przygotować zmianę

1. Jeden PR dotyczy jednego obszaru przepisów (na przykład składki zdrowotnej na ryczałcie).
2. Przed wysłaniem uruchom:

   ```
   pip install -e ".[dev]"
   pytest
   python scripts/sprawdz_cytaty.py
   ```

   Skrypt pobiera oficjalne teksty (potrzebny jest `pdftotext` z pakietu poppler) i odrzuca cytat,
   którego w nich nie ma.
3. W opisie PR podaj źródła, wynik skryptu cytatów i poziom pewności zmienionych wpisów.

## Licencja wkładu i podpis (DCO)

Wysyłając zmianę, zgadzasz się, że:

- kod udostępniasz na licencji Apache 2.0, a dane w `data/` na licencji CC BY 4.0, tak jak resztę
  projektu;
- masz prawo udostępnić wnoszoną treść, zgodnie z
  [Developer Certificate of Origin 1.1](https://developercertificate.org/).

Każdy commit podpisz linią `Signed-off-by` (polecenie `git commit -s`). Imię i nazwisko w tej linii
oraz adres e-mail staną się publiczne w historii repozytorium. Możesz użyć adresu `noreply`
z ustawień GitHuba.

## Zachowanie

Obowiązuje [kodeks postępowania](CODE_OF_CONDUCT.md).

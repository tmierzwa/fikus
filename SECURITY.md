# Bezpieczeństwo i kontakt

## Błędy w danych

Błędną wartość, termin albo zasadę zgłoś jako issue z szablonem „Błąd w danych”. To najważniejsze
zgłoszenia w projekcie, bo ktoś może się na tych danych oprzeć przy płaceniu podatku.

## Luki bezpieczeństwa

Lukę w kodzie (na przykład w pobieraniu i przetwarzaniu źródeł) zgłoś prywatnie przez
„Report a vulnerability” w zakładce Security repozytorium. Nie opisuj jej w publicznym issue.

Serwer MCP działa lokalnie przez stdio i tylko czyta pliki z `data/`. Nie łączy się z siecią
i nie przyjmuje połączeń z zewnątrz. Z siecią łączą się tylko skrypty `scripts/sprawdz_cytaty.py`
i `scripts/wykryj_zmiany.py` (API ELI Sejmu). Pobierają wyłącznie adresy `https://`, nie idą
za przekierowaniem na inny protokół i mają limit rozmiaru odpowiedzi. Teksty źródeł trafiają
do `.cache/zrodla/`. Adresy źródeł pochodzą z danych w repozytorium, więc nowe adresy w PR warto
obejrzeć przed uruchomieniem skryptów.

## Kontakt

Sprawy poufne, w tym naruszenia kodeksu postępowania, zgłaszaj prywatnie przez „Report a vulnerability”
w zakładce Security repozytorium. W tytule napisz „Kodeks postępowania”. Zgłoszenie widzą tylko opiekunowie.

## Wersje i czas odpowiedzi

Poprawki bezpieczeństwa wydajemy tylko dla najnowszej wersji z gałęzi `main`. Na zgłoszenie
luki odpowiadamy w ciągu 7 dni. Po wydaniu poprawki opisujemy lukę w publicznym komunikacie
(GitHub Security Advisory) i podziękujemy zgłaszającemu, jeśli się na to zgodzi.

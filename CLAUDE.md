# Fikus: zasady dla agentów

Fikus to serwer MCP z parametrami przepisów dla JDG. To samodzielny projekt społecznościowy. Pierwszym klientem jest Staffkey.

## Zasady nadrzędne

1. Serwer niczego nie liczy. Udostępnia wartości, reguły terminów, dni wolne i zasady obliczeń opisane krokami z podstawą prawną.
2. Serwer nie odpowiada na pytania o sytuację konkretnego podatnika, bo to byłoby doradztwo podatkowe. To samo dotyczy odpowiedzi w zgłoszeniach i PR-ach.
3. Każda wersja ma okres obowiązywania, pole `verification` z dowodami i co najmniej jedno źródło pierwotne z dosłownym cytatem (`quote`), z którego wynika wartość.
4. Źródło pierwotne to tekst jednolity w ISAP/ELI, obwieszczenie w M.P. albo komunikat ZUS lub MF. Blog, kalkulator i portal mogą być tylko źródłem kontrolnym (`kind: control`).
5. Bez źródła pierwotnego wartość nie trafia do danych. Lepiej nie mieć wartości niż mieć niepewną.

## Praca z danymi

- Jeden obszar przepisów (na przykład składka zdrowotna na ryczałcie) to jeden PR.
- Dodajesz nową wersję, starej nie edytujesz. Poprawkę błędu w starej wersji opisz w PR i w polu `note`.
- Opiekun projektu nie jest ekspertem podatkowym i nie sprawdzi przepisów. Nie proś go o ocenę przepisów ani o wybór źródeł. Pytaj go o fakty, dokumenty i decyzje.
- Pewność liczy model (`confidence`). Jest wysoka, gdy wersja ma cytat ze źródła pierwotnego, co najmniej dwa inne dowody i nie ma `open_issue`. Dowody to:
  - `independent: true` lub `kind: control` przy źródle, które samo podaje tę samą wartość (źródła, które dają wartość dopiero razem, nie są niezależne);
  - `agent_check`: data raportu subagenta `weryfikator-zrodel` bez niezgodności; wpisujesz ją dopiero po takim raporcie;
  - `filed_documents`: zgodność z deklaracją złożoną w urzędzie, opisana bez kwot i danych podatnika;
  - `expert`: tylko z odpowiedzi eksperta przekazanej przez opiekuna, z datą i podstawą. Imię i nazwisko wpisujesz tylko wtedy, gdy ekspert zgodził się na publikację; inaczej wpisujesz samą kwalifikację.
- Gdy źródła się różnią, przepis wymaga interpretacji albo brakuje drugiego źródła, wpisz `open_issue` i dopisz pytanie w `docs/pytania-do-eksperta.md`. Nie zgaduj.
- Przed commitem uruchom `pytest` i `python scripts/sprawdz_cytaty.py`. Skrypt pobiera oficjalne teksty i odrzuca cytat, którego w nich nie ma.

## Czego nie robić

- Nie dodawać kalkulatorów, przykładów liczbowych ani formuł wykonywalnych.
- Nie kopiować stałych ze Staffkey bez sprawdzenia w źródle pierwotnym.
- Nie umieszczać w repozytorium ani w zgłoszeniach żadnych danych podatnika: kwot z deklaracji, NIP, PESEL, informacji o tym, kto jak się rozlicza. Profile w `data/profiles.yaml` są przykładowe.

## Decyzje

Decyzje projektowe prowadzi opiekun w dokumencie projektowym (dostęp ma tylko on): https://claude.ai/artifact/DDEwjBDuVupHq7TVkogc6p. Nowa decyzja trafia najpierw tam, potem do kodu i do tego pliku.

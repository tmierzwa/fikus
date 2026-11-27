# Fikus: zasady dla agentów

Fikus to serwer MCP z parametrami przepisów dla JDG. To samodzielny projekt społecznościowy. Pierwszym klientem jest Staffkey.

## Zasady nadrzędne

1. Serwer niczego nie liczy. Udostępnia wartości, reguły terminów, dni wolne i zasady obliczeń opisane krokami z podstawą prawną.
2. Serwer nie odpowiada na pytania o sytuację konkretnego podatnika, bo to byłoby doradztwo podatkowe. To samo dotyczy odpowiedzi w zgłoszeniach i PR-ach.
3. Każda wersja ma okres obowiązywania, pole `verification` z dowodami i co najmniej jedno źródło pierwotne z dosłownym cytatem (`quote`), z którego wynika wartość.
4. Źródło pierwotne to tekst jednolity w ISAP/ELI, obwieszczenie w M.P. albo komunikat ZUS lub MF. Gdy zmiany nie ma jeszcze w tekście jednolitym, źródłem nowego brzmienia jest ustawa zmieniająca w Dz.U., cytowana obok ostatniego tekstu jednolitego; nowy tekst jednolity dopisujesz po ogłoszeniu. Blog, kalkulator i portal mogą być tylko źródłem kontrolnym (`kind: control`).
5. Bez źródła pierwotnego wartość nie trafia do danych. Lepiej nie mieć wartości niż mieć niepewną.
6. Serwer opiera się wyłącznie na źródłach publicznych i na wkładzie kontrybutorów.

## Praca z danymi

- Jeden obszar przepisów (na przykład składka zdrowotna na ryczałcie) to jeden PR.
- Klucze i wartości pól wyliczeniowych (`kind: control`, `rule`) zostają po angielsku. Treść (notatki, kroki, tytuły, pytania, komunikaty serwera) piszesz po polsku, bez nazw pól w zdaniach: zamiast „valid_from” piszesz „data początku obowiązywania”.
- Dodajesz nową wersję, starej nie edytujesz. Poprawkę błędu w starej wersji opisz w PR. W polu `note` opisz ją tylko wtedy, gdy zmienia coś, co klient mógł już odczytać: wartość, okres, podstawę prawną albo kroki zasady. Poprawki samych źródeł i procesu (zaślepka, wycofany `agent_check`) idą tylko do PR.
- Opiekun projektu nie jest ekspertem podatkowym i nie sprawdzi przepisów. Nie proś go o ocenę przepisów ani o wybór źródeł. Pytaj go o fakty, dokumenty i decyzje.
- Pewność liczy model (`confidence`). Jest wysoka, gdy wersja ma cytat ze źródła pierwotnego, co najmniej dwa inne dowody i nie ma `open_issue`. Jest średnia, gdy ma ten sam komplet dowodów, a `open_issue` dotyczy tylko przypadku brzegowego (`open_issue_scope: edge_case`). W każdym innym przypadku jest niska. Dowody to:
  - `independent: true` lub `kind: control` przy źródle, które samo podaje tę samą wartość (źródła, które dają wartość dopiero razem, nie są niezależne). Przy zasadzie obliczeń źródło musi samo podawać wszystkie kroki; strona MF lub ZUS, która potwierdza część kroków, jest zwykłym źródłem z cytatem, a częściowej strony portalu nie dodajesz;
  - przy wartości złożonej z kilku pól: `confirms` przy źródłach, gdy każde pole i okres (`period`) podają co najmniej dwa różne dokumenty z cytatem, w tym źródło pierwotne; jeden dokument liczy się raz. Adres pliku schematu potwierdza też sam plik spod tego adresu, gdy cytat z niego podaje kod systemowy formularza;
  - `agent_check`: data raportu subagenta `weryfikator-zrodel` bez niezgodności; wpisujesz ją dopiero po takim raporcie;
  - `filed_documents`: zgodność z deklaracją złożoną w urzędzie, zgłoszona przez kontrybutora i opisana bez kwot i danych podatnika; deklaracje opiekuna nie są dowodem;
  - `expert`: tylko z odpowiedzi eksperta przekazanej przez opiekuna, z datą i podstawą. Imię i nazwisko wpisujesz tylko wtedy, gdy ekspert zgodził się na publikację; inaczej wpisujesz samą kwalifikację.
- Gdy źródła się różnią, przepis wymaga interpretacji albo brakuje drugiego źródła, wpisz `open_issue` i dopisz pytanie w `docs/pytania-do-eksperta.md`. Nie zgaduj.
- `open_issue_scope: edge_case` wpisujesz tylko wtedy, gdy pytanie nie dotyczy samej wartości ani rdzenia zasady, a krok opisuje ten przypadek jako niewyjaśniony. W razie wątpliwości zostaw zakres `value` (domyślny). Zakres sprawdza `weryfikator-zrodel`.
- Gdy wartość ma pełny komplet dowodów, a otwarte pytanie dotyczy tylko tego, jak ją stosować (na przykład od jakiej podstawy liczy się limit albo jak liczy się okres), pytanie przenosisz do parametru, który opisuje sposób stosowania (zwykle zasady). Przy wartości wpisujesz `not_covered` (czego wartość nie rozstrzyga) i `see_also` (ten parametr). Nie rozbijasz parametru, gdy pytanie dotyczy samej wartości, jej okresu albo pól. Zasady nie dzielisz na części, jeśli żadne źródło nie podaje samo wszystkich kroków części. Rozbicie sprawdza `weryfikator-zrodel`.
- Źródłem pierwotnym nie jest tabela kursów NBP. Broszura informacyjna MF lub KAS jest komunikatem MF, a poradnik ZUS opublikowany na zus.pl jest komunikatem ZUS.
- Przed commitem uruchom `pytest` i `python scripts/sprawdz_cytaty.py`. Skrypt pobiera oficjalne teksty i odrzuca cytat, którego w nich nie ma.

## Czego nie robić

- Nie dodawać kalkulatorów, przykładów liczbowych ani formuł wykonywalnych.
- Nie kopiować stałych ze Staffkey bez sprawdzenia w źródle pierwotnym.
- Nie umieszczać w repozytorium ani w zgłoszeniach żadnych danych podatnika: kwot z deklaracji, NIP, PESEL, informacji o tym, kto jak się rozlicza. Profile w `data/profiles.yaml` są przykładowe.

## Zmiany w aktach

- `python scripts/wykryj_zmiany.py` sprawdza w API ELI Sejmu, czy akty cytowane w danych mają nowelizacje lub nowy tekst jednolity, których dane jeszcze nie uwzględniają. W CI robi to co tydzień zadanie `zmiany`.
- Nowelizacja, która zmienia wartość, termin albo zasadę, to nowa wersja parametru (skill `dodaj-parametr`).
- Nowelizacja, która nie dotyka naszych parametrów, to wpis w `data/zmiany_sprawdzone.yaml`: identyfikator ELI aktu, data przejrzenia i notatka z dokładną listą zmienianych artykułów. Pole `for` dodajesz, gdy nowelizacja zmienia kilka aktów, a wpis dotyczy tylko jednego. Listę artykułów sprawdza `weryfikator-zrodel`.

## Git i pull requesty

- Każda zmiana powstaje na osobnej gałęzi wyprowadzonej z `origin/main` (najpierw `git fetch`). Przy pracy równoległej używasz osobnego worktree, nie przełączasz gałęzi we wspólnej kopii.
- Każdy commit ma podpis DCO: `git commit -s`.
- Na `main` zmiany trafiają tylko przez PR. Nie scalasz gałęzi w lokalnym `main`. Wymagane sprawdzenia to `testy`, `dco` i `python-min`. Nadpisywanie historii jest zablokowane, więc commit bez podpisu przenosisz na nową gałąź przez `git cherry-pick -s`.
- Po scaleniu PR lokalny `main` ustawiasz na `origin/main` dopiero po sprawdzeniu, że nie ma w nim pracy, której brakuje na GitHubie.

## Wydanie

1. W PR wydania podnosisz wersję w `pyproject.toml`, w `server.json` (dwa pola `version`) i w `CITATION.cff` (razem z datą wydania), a sekcję „Niewydane” w `CHANGELOG.md` przenosisz pod nową wersję.
2. Po scaleniu tworzysz wydanie na GitHubie z tagiem `vX.Y.Z`. Workflow `publikacja.yml` sprawdza zgodność wersji i publikuje paczkę na PyPI (Trusted Publishing, środowisko `pypi`).
3. Na końcu aktualizujesz wpis w MCP Registry: `mcp-publisher login github` i `mcp-publisher publish`. Logowanie robi opiekun.

## Decyzje

Decyzje projektowe prowadzi opiekun w dokumencie projektowym (dostęp ma tylko on): https://claude.ai/artifact/DDEwjBDuVupHq7TVkogc6p. Nowa decyzja trafia najpierw tam, potem do kodu i do tego pliku.

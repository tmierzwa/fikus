"""Model danych: parametr = lista wersji z okresem obowiązywania, źródłami i dowodami."""
from __future__ import annotations

import re
from datetime import date, timedelta
from typing import Literal, get_args

from pydantic import BaseModel, Field, PrivateAttr, field_validator, model_validator

from .cytaty import normalize

PERIOD = "period"   # w confirms: okres obowiązywania wersji
XSD_URL = "xsd_url"     # w schemacie: adres pliku XSD
SYSTEM_CODE = "system_code"
SCHEMA_VERSION = "schema_version"
# Wyróżnik i plik schematu tego samego wzoru w Centralnym Repozytorium Wzorów Dokumentów Elektronicznych.
_CRWDE_CARD = re.compile(r"crd\.gov\.pl/wzor/(\d{4}/\d{2}/\d{2}/\d+)/wyroznik\.xml")
_CRWDE_XSD = re.compile(r"crd\.gov\.pl/wzor/(\d{4}/\d{2}/\d{2}/\d+)/schemat\.xsd")
STEP = "step_"         # w confirms zasady: step_1, step_2, … (numer kroku od 1)


def _fields(value) -> list[str]:
    """Co potwierdza się osobno: kroki zasady (step_N) albo klucze wartości złożonej."""
    steps = value.get("steps") if isinstance(value, dict) else None
    if isinstance(steps, list):
        return [f"{STEP}{i}" for i in range(1, len(steps) + 1)]
    return list(value)


def _address(url: str) -> str:
    """Adres bez protokołu: rejestr wzorów podaje http://, a źródło musi mieć https://."""
    return url.split("://", 1)[-1]


class Source(BaseModel):
    """Źródło pierwotne (akt, obwieszczenie, komunikat) albo kontrolne (np. finwire)."""
    title: str                      # np. "M.P. 2026 poz. 117" albo "Komunikat ZUS"
    url: str
    article: str | None = None      # np. "art. 81 ust. 2e"
    kind: Literal["primary", "control"] = "primary"
    # Dosłowny fragment tekstu źródła, z którego wynika wartość. scripts/sprawdz_cytaty.py
    # pobiera tekst spod url i sprawdza, że fragment w nim jest.
    quote: str | None = None
    as_of: date | None = None       # stan prawny tekstu jednolitego albo data ogłoszenia
    # Źródło pierwotne, które samo, niezależnie od pozostałych, podaje tę samą wartość
    # (np. ustawa budżetowa obok obwieszczenia). Źródła, które dopiero razem dają wartość, nie są niezależne.
    independent: bool = False
    # Pola wartości złożonej (klucze value i "period" dla okresu obowiązywania), które to źródło
    # samo podaje. Pozwala potwierdzić drugie źródło pole po polu (Version.confidence).
    confirms: list[str] | None = None   # pola wartości złożonej, period albo kroki zasady (step_N)

    @field_validator("url")
    @classmethod
    def _https(cls, v: str) -> str:
        if not v.startswith("https://"):
            raise ValueError("adres źródła musi zaczynać się od https://")
        return v


class Expert(BaseModel):
    """Odpowiedź eksperta (doradca podatkowy, księgowa). Wpisywana tylko z jego odpowiedzi."""
    name: str                       # imię i nazwisko tylko za zgodą na publikację; inaczej kwalifikacja
    answered_at: date
    basis: str                      # co ekspert potwierdził i na jakiej podstawie
    url: str | None = None          # link do odpowiedzi (komentarz w GitHub Discussions)

    @field_validator("url")
    @classmethod
    def _https(cls, v: str | None) -> str | None:
        if v is not None and not v.startswith("https://"):
            raise ValueError("adres odpowiedzi eksperta musi zaczynać się od https://")
        return v


class Verification(BaseModel):
    """Dowody za wartością. Poziom pewności liczy Version.confidence."""
    checked_at: date
    agent_check: date | None = None     # niezależne sprawdzenie agentem, który nie widział pracy autora
    filed_documents: str | None = None  # zgodność z deklaracjami przyjętymi przez urząd, bez danych podatnika
    expert: Expert | None = None
    open_issue: str | None = None       # niejasność albo pytanie do eksperta; blokuje wysoki poziom
    # Czego dotyczy otwarte pytanie: samej wartości lub rdzenia zasady (value) albo tylko przypadku
    # brzegowego (edge_case). Przy edge_case i pełnym komplecie dowodów pewność jest średnia.
    open_issue_scope: Literal["value", "edge_case"] | None = None

    @model_validator(mode="after")
    def _scope(self) -> "Verification":
        if self.open_issue_scope and not self.open_issue:
            raise ValueError("zakres pytania (open_issue_scope) bez otwartego pytania")
        return self


class Version(BaseModel):
    valid_from: date
    valid_to: date | None = None    # None = obowiązuje do odwołania
    value: float | int | str | dict | list
    sources: list[Source]
    verification: Verification
    note: str | None = None
    # Czego wersja nie rozstrzyga (decyzje z 27 listopada 2026 r.). Przy wartości: sposób stosowania,
    # który opisuje osobny parametr z see_also; pytanie o niego ma tamten parametr, nie ta wersja.
    # Przy zasadzie: sprawy, których zasada nie opisuje; odsyłacz nie jest wymagany. Tego opisu
    # nie potwierdza się dokumentami.
    not_covered: str | None = None
    see_also: list[str] = Field(default_factory=list)   # parametry, które opisują to, czego wersja nie rozstrzyga
    # Początek następnej wersji tego samego parametru, gdy jej okres jest potwierdzony (ustawia Parameter).
    _next_confirmed_from: date | None = PrivateAttr(default=None)

    @model_validator(mode="after")
    def _check(self) -> "Version":
        if self.see_also and not self.not_covered:
            raise ValueError("lista parametrów, które opisują to, czego wersja nie rozstrzyga, wymaga opisu tego, czego nie rozstrzyga")
        if self.valid_to and self.valid_to < self.valid_from:
            raise ValueError("koniec obowiązywania wersji jest wcześniejszy niż jej początek")
        if not any(s.kind == "primary" for s in self.sources):
            raise ValueError("każda wersja potrzebuje źródła pierwotnego")
        if any(s.confirms is not None for s in self.sources):
            if not isinstance(self.value, dict):
                raise ValueError("potwierdzanie pól (confirms) dotyczy tylko wartości złożonej albo kroków zasady")
            if PERIOD in self.value:
                raise ValueError(f"klucz wartości {PERIOD!r} jest zarezerwowany dla okresu w confirms")
            known = set(_fields(self.value)) | {PERIOD}
            for s in self.sources:
                if s.confirms is None:
                    continue
                if not s.confirms or not s.quote:
                    raise ValueError(f"źródło {s.url}: confirms wymaga cytatu i co najmniej jednego pola")
                unknown = set(s.confirms) - known
                if unknown:
                    raise ValueError(f"źródło {s.url} potwierdza nieznane pola: {', '.join(sorted(unknown))}")
                self._check_xsd_self(s)
        return self

    def _check_xsd_self(self, s: Source) -> None:
        """Plik spod adresu schematu potwierdza ten adres tylko wtedy, gdy jego cytat podaje kod
        systemowy formularza (decyzja z 27 listopada 2026 r.). Inaczej nie wiadomo, że to ten schemat."""
        url, code = self.value.get(XSD_URL), self.value.get(SYSTEM_CODE)
        if XSD_URL not in s.confirms or not isinstance(url, str) or _address(s.url) != _address(url):
            return
        if not isinstance(code, str) or normalize(code) not in normalize(s.quote or ""):
            raise ValueError(f"źródło {s.url}: plik schematu potwierdza swój adres tylko cytatem "
                             "z kodem systemowym formularza")

    def _unconfirmed_fields(self) -> list[str] | None:
        """Pola wartości złożonej (i okres), których nie podają co najmniej dwa różne dokumenty z cytatem,
        w tym źródło pierwotne. Jeden dokument (adres) liczy się raz, także przy kilku cytatach.
        Wyjątki dla schematów z CRWDE opisuje _crwde_confirmed. None, gdy wersja nie potwierdza pól osobno."""
        if not isinstance(self.value, dict) or not any(s.confirms for s in self.sources):
            return None
        # Okresu zasady nie potwierdza się osobno: wersje często zaczynają się na początku zakresu danych.
        is_rule = isinstance(self.value.get("steps"), list)
        fields = [*_fields(self.value), *([] if is_rule else [PERIOD])]
        missing = [f for f in fields if not self._two_documents(f)]
        if not is_rule:
            missing = [f for f in missing if f not in self._crwde_confirmed(missing)]
        return missing

    def _two_documents(self, field: str) -> bool:
        docs = {s.url for s in self.sources if s.quote and field in (s.confirms or [])}
        primary = {s.url for s in self.sources if s.quote and s.kind == "primary" and field in (s.confirms or [])}
        return len(docs) >= 2 and bool(primary)

    def _crwde_confirmed(self, missing: list[str]) -> set[str]:
        """Urzędowy łańcuch dokumentów schematu z CRWDE zastępuje drugi dokument (decyzja z 27 listopada
        2026 r.). Plik schematu, którego adres potwierdzają dwa dokumenty, a cytat z pliku podaje kod
        systemowy, sam potwierdza kod systemowy i wersję schematu. Wyróżnik wzoru o tym samym numerze
        co adres schematu sam potwierdza okres; koniec okresu wersji zamkniętej wynika z początku
        następnej wersji, gdy zaczyna się ona dzień później i ma potwierdzony okres."""
        url = self.value.get(XSD_URL)
        if not isinstance(url, str):
            return set()
        ok: set[str] = set()
        if XSD_URL not in missing:
            for s in self.sources:      # cytat z kodem systemowym sprawdza już _check_xsd_self
                if s.quote and XSD_URL in (s.confirms or []) and _address(s.url) == _address(url):
                    ok |= {f for f in (SYSTEM_CODE, SCHEMA_VERSION) if f in s.confirms}
        number = _CRWDE_XSD.fullmatch(_address(url))
        card = number and any(
            s.quote and s.kind == "primary" and PERIOD in (s.confirms or [])
            and (m := _CRWDE_CARD.fullmatch(_address(s.url))) and m.group(1) == number.group(1)
            for s in self.sources)
        if card and (self.valid_to is None
                     or self._next_confirmed_from == self.valid_to + timedelta(days=1)):
            ok.add(PERIOD)
        return ok

    def _second_source(self) -> bool:
        """Drugie źródło: źródło kontrolne albo niezależne z własnym cytatem, które jest innym dokumentem
        (adresem) niż źródło pierwotne z cytatem. Bez cytatu nie wiadomo, że podaje tę samą wartość,
        a źródło, które dało cytat, nie potwierdza samego siebie."""
        primary = {s.url for s in self.sources if s.kind == "primary" and s.quote}
        return any(s.quote and (s.kind == "control" or s.independent) and primary - {s.url}
                   for s in self.sources)

    def confidence(self) -> dict:
        """Wysoka: cytat ze źródła pierwotnego i co najmniej dwa inne dowody, bez otwartych pytań.
        Średnia: ten sam komplet dowodów, a otwarte pytanie dotyczy tylko przypadku brzegowego.
        Niska: każdy inny przypadek."""
        ver = self.verification
        evidence = []
        if any(s.kind == "primary" and s.quote for s in self.sources):
            evidence.append("cytat")
        # Gdy wersja potwierdza pola osobno, liczy się tylko ta ścieżka.
        unconfirmed = self._unconfirmed_fields()
        if (unconfirmed is None and self._second_source()) or unconfirmed == []:
            evidence.append("drugie_zrodlo")
        if ver.agent_check:
            evidence.append("agent")
        if ver.filed_documents:
            evidence.append("deklaracje")
        if ver.expert:
            evidence.append("ekspert")
        full = "cytat" in evidence and len(evidence) >= 3
        scope = (ver.open_issue_scope or "value") if ver.open_issue else None
        if full and not ver.open_issue:
            level = "wysoka"
        elif full and scope == "edge_case":
            level = "średnia"
        else:
            level = "niska"
        result = {"level": level, "evidence": evidence, "open_issue": ver.open_issue,
                  "open_issue_scope": scope}
        if unconfirmed is not None:
            result["unconfirmed_fields"] = unconfirmed
        return result

    def covers(self, d: date) -> bool:
        return self.valid_from <= d and (self.valid_to is None or d <= self.valid_to)


class Parameter(BaseModel):
    id: str                         # np. "zdrowotna.liniowy.minimum"
    name: str                       # nazwa po polsku dla człowieka
    kind: Literal["value", "deadline", "rule", "calendar"] = "value"
    unit: str | None = None
    applies_to: dict[str, list[str]] = Field(default_factory=dict)  # {} = wszystkie profile
    versions: list[Version]

    @model_validator(mode="after")
    def _known_profile_fields(self) -> "Parameter":
        """Literówka w applies_to po cichu wyłączyłaby parametr ze wszystkich profili."""
        allowed = _profile_values()
        for key, values in self.applies_to.items():
            if key not in allowed:
                raise ValueError(f"{self.id}: applies_to ma nieznane pole profilu {key!r} "
                                 f"(znane: {', '.join(sorted(allowed))})")
            unknown = [v for v in values if v not in allowed[key]]
            if unknown:
                raise ValueError(f"{self.id}: applies_to.{key} ma nieznane wartości {', '.join(unknown)} "
                                 f"(znane: {', '.join(allowed[key])})")
        return self

    @model_validator(mode="after")
    def _no_overlap(self) -> "Parameter":
        vs = sorted(self.versions, key=lambda v: v.valid_from)
        for a, b in zip(vs, vs[1:]):
            if a.valid_to is None or a.valid_to >= b.valid_from:
                raise ValueError(f"{self.id}: okresy {a.valid_from} i {b.valid_from} nakładają się")
        self.versions = vs
        for v in vs:
            self._check_value_shape(v)
        # Od najpóźniejszej: koniec okresu wersji zamkniętej może wynikać z potwierdzonego początku następnej.
        for a, b in zip(reversed(vs[:-1]), reversed(vs[1:])):
            unconfirmed = b._unconfirmed_fields()
            if unconfirmed is not None and PERIOD not in unconfirmed:
                a._next_confirmed_from = b.valid_from
        return self

    def _check_value_shape(self, v: Version) -> None:
        """Wymagany kształt wartości zależy od rodzaju parametru. Błąd w YAML wychodzi przy ładowaniu."""
        where = f"{self.id} {v.valid_from}"
        if self.kind == "deadline":
            day = v.value.get("day_of_month") if isinstance(v.value, dict) else None
            if not isinstance(day, int) or not 1 <= day <= 31:
                raise ValueError(f"{where}: termin potrzebuje value.day_of_month od 1 do 31")
        elif self.kind == "rule":
            steps = v.value.get("steps") if isinstance(v.value, dict) else None
            if not steps or not all(isinstance(s, dict) and s.get("text") for s in steps):
                raise ValueError(f"{where}: zasada potrzebuje value.steps, a każdy krok pola text")
            return          # zasada może opisać, czego nie obejmuje, bez odsyłacza
        elif self.kind == "calendar" and not isinstance(v.value, list):
            raise ValueError(f"{where}: kalendarz potrzebuje listy dat")
        if v.not_covered and not v.see_also:
            raise ValueError(f"{where}: opis tego, czego wartość nie rozstrzyga, wymaga listy parametrów, które to opisują")

    def at(self, d: date) -> Version | None:
        return next((v for v in self.versions if v.covers(d)), None)

    def matches(self, profile: dict[str, str]) -> bool:
        return all(profile.get(k) in allowed for k, allowed in self.applies_to.items())


class Profile(BaseModel):
    id: str
    tax_form: Literal["ryczalt", "liniowy", "skala"]
    vat: Literal["czynny_miesiecznie", "czynny_kwartalnie", "zwolniony"]
    zus: Literal["pelny", "preferencyjny", "maly_zus_plus", "ulga_na_start"]

    def as_dict(self) -> dict[str, str]:
        return {"tax_form": self.tax_form, "vat": self.vat, "zus": self.zus}


def _profile_values() -> dict[str, tuple[str, ...]]:
    """Pola profilu, po których applies_to wybiera parametry, i ich dozwolone wartości."""
    return {name: get_args(f.annotation) for name, f in Profile.model_fields.items() if name != "id"}

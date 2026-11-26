"""Model danych: parametr = lista wersji z okresem obowiązywania, źródłami i dowodami."""
from __future__ import annotations

from datetime import date
from typing import Literal

from pydantic import BaseModel, Field, field_validator, model_validator


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


class Verification(BaseModel):
    """Dowody za wartością. Poziom pewności liczy Version.confidence."""
    checked_at: date
    agent_check: date | None = None     # niezależne sprawdzenie agentem, który nie widział pracy autora
    filed_documents: str | None = None  # zgodność z deklaracjami przyjętymi przez urząd, bez danych podatnika
    expert: Expert | None = None
    open_issue: str | None = None       # niejasność albo pytanie do eksperta; blokuje wysoki poziom


class Version(BaseModel):
    valid_from: date
    valid_to: date | None = None    # None = obowiązuje do odwołania
    value: float | int | str | dict | list
    sources: list[Source]
    verification: Verification
    note: str | None = None

    @model_validator(mode="after")
    def _check(self) -> "Version":
        if self.valid_to and self.valid_to < self.valid_from:
            raise ValueError("koniec obowiązywania wersji jest wcześniejszy niż jej początek")
        if not any(s.kind == "primary" for s in self.sources):
            raise ValueError("każda wersja potrzebuje źródła pierwotnego")
        return self

    def confidence(self) -> dict:
        """Wysoka: cytat ze źródła pierwotnego i co najmniej dwa inne dowody, bez otwartych pytań."""
        ver = self.verification
        evidence = []
        if any(s.kind == "primary" and s.quote for s in self.sources):
            evidence.append("cytat")
        if any(s.kind == "control" or s.independent for s in self.sources):
            evidence.append("drugie_zrodlo")
        if ver.agent_check:
            evidence.append("agent")
        if ver.filed_documents:
            evidence.append("deklaracje")
        if ver.expert:
            evidence.append("ekspert")
        high = "cytat" in evidence and len(evidence) >= 3 and not ver.open_issue
        return {"level": "wysoka" if high else "niska", "evidence": evidence,
                "open_issue": ver.open_issue}

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
    def _no_overlap(self) -> "Parameter":
        vs = sorted(self.versions, key=lambda v: v.valid_from)
        for a, b in zip(vs, vs[1:]):
            if a.valid_to is None or a.valid_to >= b.valid_from:
                raise ValueError(f"{self.id}: okresy {a.valid_from} i {b.valid_from} nakładają się")
        self.versions = vs
        for v in vs:
            self._check_value_shape(v)
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
        elif self.kind == "calendar" and not isinstance(v.value, list):
            raise ValueError(f"{where}: kalendarz potrzebuje listy dat")

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

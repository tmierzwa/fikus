"""Ładowanie danych z YAML i zapytania na dzień X."""
from __future__ import annotations

import calendar
from datetime import date
from pathlib import Path

import yaml

from .model import Parameter, Profile

_REPO_DATA = Path(__file__).resolve().parents[2] / "data"   # kopia robocza repozytorium
_PKG_DATA = Path(__file__).resolve().parent / "data"        # paczka zainstalowana z wheel
DATA = _REPO_DATA if (_REPO_DATA / "parameters").is_dir() else _PKG_DATA


class Store:
    """Wszystkie parametry i profile wczytane z YAML. Błąd w danych zatrzymuje start serwera."""

    def __init__(self, data_dir: Path = DATA):
        self.params: dict[str, Parameter] = {}
        for f in sorted((data_dir / "parameters").glob("*.yaml")):
            for raw in yaml.safe_load(f.read_text(encoding="utf-8")) or []:
                p = Parameter.model_validate(raw)
                if p.id in self.params:
                    raise ValueError(f"zduplikowany parametr {p.id} ({f.name})")
                self.params[p.id] = p
        self._check_rule_refs()
        for required in ("kalendarz.dni_wolne", "zasada.przesuniecie_terminu"):   # potrzebne w deadlines()
            if required not in self.params:
                raise ValueError(f"w danych brakuje parametru {required}")
        raw_profiles = yaml.safe_load((data_dir / "profiles.yaml").read_text(encoding="utf-8"))
        self.profiles = {r["id"]: Profile.model_validate(r) for r in raw_profiles}

    def _check_rule_refs(self) -> None:
        for p in self.params.values():
            if p.kind != "rule":
                continue
            for v in p.versions:
                for step in v.value["steps"]:
                    for ref in step.get("uses", []):
                        if ref not in self.params:
                            raise ValueError(f"{p.id}: krok odwołuje się do nieznanego parametru {ref}")
        for p in self.params.values():
            for v in p.versions:
                for ref in v.see_also:
                    if ref == p.id or ref not in self.params:
                        raise ValueError(f"{p.id}: odsyłacz do nieznanego parametru {ref}")

    def get(self, pid: str, d: date) -> dict:
        """Wersja parametru obowiązująca w dniu d albo found=False z powodem."""
        p = self.params[pid]
        v = p.at(d)
        if v is None:
            return {"id": pid, "found": False, "reason": f"brak wersji obowiązującej {d}"}
        return {
            "id": pid, "found": True, "name": p.name, "unit": p.unit, "value": v.value,
            "valid_from": str(v.valid_from), "valid_to": str(v.valid_to) if v.valid_to else None,
            "sources": [s.model_dump(mode="json", exclude_none=True) for s in v.sources],
            "confidence": v.confidence(),
            "verification": v.verification.model_dump(mode="json", exclude_none=True),
            "note": v.note,
            "not_covered": v.not_covered, "see_also": v.see_also,
        }

    def unknown_profile(self, profile_id: str) -> dict | None:
        if profile_id in self.profiles:
            return None
        return {"profile": profile_id, "found": False, "reason": "nieznany profil",
                "known": sorted(self.profiles)}

    def for_profile(self, profile_id: str, d: date) -> list[dict]:
        """Parametry, których applies_to pasuje do profilu, w wersji na dzień d."""
        if err := self.unknown_profile(profile_id):
            return [err]
        prof = self.profiles[profile_id].as_dict()
        return [self.get(p.id, d) for p in self.params.values() if p.matches(prof)]

    def changes(self, since: date) -> list[dict]:
        """Wersje sprawdzone (checked_at) w dniu since lub później, od najnowszych."""
        out = []
        for p in self.params.values():
            for v in p.versions:
                if v.verification.checked_at >= since:
                    out.append({"id": p.id, "valid_from": str(v.valid_from),
                                "checked_at": str(v.verification.checked_at), "value": v.value,
                                "confidence": v.confidence()["level"]})
        return sorted(out, key=lambda x: x["checked_at"], reverse=True)

    def deadlines(self, profile_id: str, year: int, month: int) -> dict:
        """Reguły terminów przypadających w miesiącu i dni wolne tego miesiąca. Bez wyliczania dat."""
        if err := self.unknown_profile(profile_id):
            return err
        if not (1 <= month <= 12 and 1 <= year <= 9999):
            return {"year": year, "month": month, "found": False, "reason": "niepoprawny rok lub miesiąc"}
        prof = self.profiles[profile_id].as_dict()
        d = date(year, month, 1)
        last = date(year, month, calendar.monthrange(year, month)[1])
        rules = []
        for p in self.params.values():
            if p.kind != "deadline" or not p.matches(prof):
                continue
            # wszystkie wersje, które obowiązują choćby jeden dzień w tym miesiącu
            for v in p.versions:
                if v.valid_from > last or (v.valid_to is not None and v.valid_to < d):
                    continue
                if v.value.get("month", month) != month:
                    continue
                if "months" in v.value and month not in v.value["months"]:
                    continue
                rules.append({"id": p.id, "name": p.name, "day_of_month": v.value["day_of_month"],
                              "valid_from": str(v.valid_from),
                              "valid_to": str(v.valid_to) if v.valid_to else None,
                              "sources": [s.model_dump(mode="json", exclude_none=True) for s in v.sources],
                              "confidence": v.confidence()["level"]})
        cal = self.params["kalendarz.dni_wolne"].at(d)
        holidays = [str(x) for x in (cal.value if cal else []) if str(x).startswith(f"{year}-{month:02d}")]
        return {"year": year, "month": month, "deadlines": rules,
                "non_working_days": holidays, "calendar_found": cal is not None,
                "shift_rule": self.get("zasada.przesuniecie_terminu", d)}

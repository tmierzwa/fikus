"""Równoległe pobieranie źródeł w sprawdz_cytaty.py: pula, limit na serwer i stała kolejność (bez sieci)."""
import importlib.util
import threading
import time
from collections import Counter
from pathlib import Path
from types import SimpleNamespace
from urllib.parse import urlsplit

import pytest

from fikus import cytaty

_SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "sprawdz_cytaty.py"


class _Opener:
    """Opener jak w test_pobieranie.py, ale współdzielony przez wątki: liczy jednoczesne połączenia."""

    def __init__(self, pages, delay=0.05):
        self.pages = pages          # adres → treść albo wyjątek
        self.delay = delay
        self.lock = threading.Lock()
        self.now: Counter[str] = Counter()
        self.peak: Counter[str] = Counter()
        self.now_total = self.peak_total = 0
        self.calls: Counter[str] = Counter()

    def open(self, req, timeout):
        url = req.full_url
        host = urlsplit(url).hostname
        with self.lock:
            self.calls[url] += 1
            self.now[host] += 1
            self.now_total += 1
            self.peak[host] = max(self.peak[host], self.now[host])
            self.peak_total = max(self.peak_total, self.now_total)
        try:
            time.sleep(self.delay)
            page = self.pages[url]
            if isinstance(page, Exception):
                raise page
            return _Response(page)
        finally:
            with self.lock:
                self.now[host] -= 1
                self.now_total -= 1


class _Response:
    def __init__(self, body):
        self._chunks = [body]
        self.headers = {"Content-Type": "text/html"}

    def read1(self, n):
        return self._chunks.pop(0) if self._chunks else b""

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


@pytest.fixture
def net(monkeypatch, tmp_path):
    monkeypatch.setattr(cytaty, "CACHE", tmp_path)
    cytaty._read_cached.cache_clear()

    def install(pages, delay=0.05):
        o = _Opener(pages, delay)
        monkeypatch.setattr(cytaty.urllib.request, "build_opener", lambda *a: o)
        return o
    return install


def _pages(hosts, per_host):
    return {f"https://{h}/s{i}": f"<p>tekst {h} {i}</p>".encode() for h in hosts for i in range(per_host)}


def test_prefetch_runs_in_parallel_with_host_limit(net, tmp_path):
    pages = _pages(["a.gov.pl", "b.gov.pl", "c.gov.pl", "d.gov.pl"], 6)
    o = net(pages, delay=0.05)
    start = time.monotonic()
    assert cytaty.prefetch(pages, workers=6, per_host=2) == {}
    elapsed = time.monotonic() - start
    assert elapsed < 24 * 0.05 / 2          # po kolei trwałoby 1,2 s
    assert max(o.peak.values()) == 2        # nigdy więcej niż 2 połączenia z jednym serwerem
    assert o.peak_total == 6
    assert set(o.calls.values()) == {1}
    index = (tmp_path / "indeks.tsv").read_text().splitlines()
    assert sorted(line.split("\t")[0] for line in index) == sorted(pages)
    assert all(cytaty.cached_text(u) for u in pages)
    assert not list(tmp_path.glob("*.tmp"))


def test_single_busy_host_never_exceeds_limit(net):
    pages = _pages(["api.sejm.gov.pl"], 8) | _pages(["www.zus.pl"], 1)
    o = net(pages, delay=0.03)
    cytaty.prefetch(pages, workers=6, per_host=2)
    assert o.peak["api.sejm.gov.pl"] == 2
    assert o.peak_total == 3


def test_prefetch_collects_errors_by_address(net):
    pages = _pages(["a.gov.pl"], 2)
    pages["https://a.gov.pl/zly"] = cytaty.urllib.error.HTTPError(
        "https://a.gov.pl/zly", 404, "Not Found", {}, None)
    net(pages, delay=0)
    errors = cytaty.prefetch([*pages, "http://a.gov.pl/bez-https"])
    assert set(errors) == {"https://a.gov.pl/zly", "http://a.gov.pl/bez-https"}
    assert isinstance(errors["http://a.gov.pl/bez-https"], ValueError)


def _store(sources_by_param):
    params = {}
    for pid, sources in sources_by_param.items():
        version = SimpleNamespace(valid_from="2026-01-01", sources=[
            SimpleNamespace(url=u, quote=q, kind=k) for u, q, k in sources])
        params[pid] = SimpleNamespace(id=pid, versions=[version])
    return SimpleNamespace(params=params)


def _run_script(monkeypatch, capsys, store, argv=()):
    spec = importlib.util.spec_from_file_location("sprawdz_cytaty", _SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    monkeypatch.setattr(mod, "Store", lambda: store)
    monkeypatch.setattr("sys.argv", ["sprawdz_cytaty.py", *argv])
    code = mod.main()
    return code, capsys.readouterr().out


def test_script_output_is_deterministic(net, monkeypatch, capsys, tmp_path):
    hosts = ["a.gov.pl", "b.gov.pl", "c.gov.pl"]
    pages = _pages(hosts, 4)
    pages["https://b.gov.pl/zly"] = cytaty.urllib.error.HTTPError(
        "https://b.gov.pl/zly", 404, "Not Found", {}, None)
    store = _store({
        f"p{i}": [(u, "tekst" if "zly" in u or i % 3 else "nie ma", "primary")]
        for i, u in enumerate(pages)
    } | {"q": [("https://b.gov.pl/zly", "x", "primary"), ("https://a.gov.pl/s0", "tekst", "control")]})
    outputs = []
    for delay in (0.03, 0.0):               # inna kolejność kończenia pobrań w wątkach
        for p in tmp_path.iterdir():
            p.unlink()
        cytaty._read_cached.cache_clear()
        o = net(pages, delay=delay)
        outputs.append(_run_script(monkeypatch, capsys, store))
        assert o.calls["https://b.gov.pl/zly"] == 1    # nieudany adres nie jest pobierany drugi raz
    assert outputs[0] == outputs[1]
    code, out = outputs[0]
    lines = out.splitlines()
    assert code == 1
    assert [ln for ln in lines if ln.startswith("BŁĄD")] == [
        f"BŁĄD   {pid} 2026-01-01: nie da się pobrać https://b.gov.pl/zly: HTTP Error 404: Not Found"
        for pid in ("p12", "q")]
    assert [ln.split()[1] for ln in lines if ln.startswith("ŹLE")] == ["p0", "p3", "p6", "p9"]
    assert lines[-1] == "zgodne cytaty: 9, niezgodne: 6, wersje bez cytatu pierwotnego: 6"


def test_offline_mode_does_not_fetch(net, monkeypatch, capsys):
    o = net(_pages(["a.gov.pl"], 1), delay=0)
    store = _store({"p": [("https://a.gov.pl/s0", "tekst", "primary")]})
    code, out = _run_script(monkeypatch, capsys, store, ["--offline"])
    assert sum(o.calls.values()) == 0
    assert code == 0
    assert out.startswith("BRAK   p 2026-01-01: brak tekstu w pamięci dla https://a.gov.pl/s0")
    assert out.splitlines()[-1].endswith("niesprawdzone offline: 1")

"""Pobieranie źródeł: łączny limit czasu, limit rozmiaru i ponowna próba (bez sieci)."""
import time
import urllib.error

import pytest

from fikus import cytaty


class _Response:
    def __init__(self, chunks, delay=0.0, ctype="text/html"):
        self._chunks = list(chunks)
        self._delay = delay
        self.headers = {"Content-Type": ctype}

    def read1(self, n):
        time.sleep(self._delay)
        return self._chunks.pop(0) if self._chunks else b""

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


class _Opener:
    """Kolejne wywołania open zwracają kolejne odpowiedzi albo zgłaszają kolejne wyjątki."""

    def __init__(self, *results):
        self.results = list(results)
        self.calls = 0

    def open(self, req, timeout):
        self.calls += 1
        r = self.results.pop(0)
        if isinstance(r, Exception):
            raise r
        return r


@pytest.fixture
def opener(monkeypatch):
    def install(*results):
        o = _Opener(*results)
        monkeypatch.setattr(cytaty.urllib.request, "build_opener", lambda *a: o)
        return o
    return install


def test_slow_server_hits_total_timeout(opener):
    drip = lambda: _Response([b"x"] * 1000, delay=0.02)   # noqa: E731
    o = opener(drip(), drip())
    start = time.monotonic()
    with pytest.raises(TimeoutError, match="trwa ponad"):
        cytaty.fetch_bytes("https://example.org/a", {}, 1024 * 1024, timeout=0.1)
    assert o.calls == 2                         # jedna ponowna próba
    assert time.monotonic() - start < 2


def test_network_error_is_retried_once(opener):
    o = opener(urllib.error.URLError(ConnectionResetError()), _Response([b"abc", b"def"]))
    body, ctype = cytaty.fetch_bytes("https://example.org/a", {}, 100, timeout=5)
    assert (body, ctype, o.calls) == (b"abcdef", "text/html", 2)


def test_client_error_and_bad_redirect_are_not_retried(opener):
    o = opener(urllib.error.HTTPError("https://example.org/a", 404, "Not Found", {}, None))
    with pytest.raises(urllib.error.HTTPError):
        cytaty.fetch_bytes("https://example.org/a", {}, 100, timeout=5)
    o = opener(urllib.error.URLError("przekierowanie poza https: http://example.org/b"))
    with pytest.raises(urllib.error.URLError):
        cytaty.fetch_bytes("https://example.org/a", {}, 100, timeout=5)
    assert o.calls == 1


def test_size_limit_is_kept(opener):
    opener(_Response([b"x" * 60, b"x" * 60]))
    with pytest.raises(ValueError, match="ponad"):
        cytaty.fetch_bytes("https://example.org/a", {}, 100, timeout=5)


def test_fetch_text_uses_limits_and_caches(opener, monkeypatch, tmp_path):
    monkeypatch.setattr(cytaty, "CACHE", tmp_path)
    o = opener(_Response([b"<p>Ala &amp; kot</p>"]))
    assert "Ala & kot" in cytaty.fetch_text("https://example.org/strona")
    assert "Ala & kot" in cytaty.fetch_text("https://example.org/strona")   # z pamięci
    assert o.calls == 1
    assert (tmp_path / "indeks.tsv").read_text().count("\n") == 1

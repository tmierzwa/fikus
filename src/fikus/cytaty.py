"""Mechaniczne sprawdzanie cytatów: czy dosłowny fragment zapisany przy źródle jest w jego tekście.

Tekst źródła pobiera się spod oficjalnego adresu (PDF tekstu jednolitego, obwieszczenia, strona
urzędu) i zapisuje w .cache/zrodla/. Porównanie ignoruje wielkość liter, białe znaki, przeniesienia
wyrazów i rodzaj cudzysłowów i myślników, bo tak różnią się teksty wyciągnięte z PDF.
"""
from __future__ import annotations

import functools
import hashlib
import html
import os
import re
import subprocess
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
CACHE = Path(os.environ.get("FIKUS_CACHE") or (
    _REPO / ".cache" / "zrodla" if (_REPO / "pyproject.toml").is_file()
    else Path.home() / ".cache" / "fikus" / "zrodla"))

MAX_BYTES = 50 * 1024 * 1024    # górny limit pobieranego pliku, żeby zły adres nie zapchał dysku i pamięci
FETCH_TIMEOUT = 120.0           # łączny limit czasu jednego pobrania w sekundach, nie tylko jednej operacji
_SOCKET_TIMEOUT = 30.0          # limit jednej operacji na gnieździe (połączenie, odczyt)
_CHUNK = 64 * 1024

_ELI_PAGE = re.compile(r"^https://eli\.gov\.pl/eli/(DU|MP)/(\d{4})/(\d+)/ogl/?$")


def text_url(url: str) -> str:
    """Strona ELI aktu → adres jego tekstu w PDF (API Sejmu)."""
    m = _ELI_PAGE.match(url)
    if m:
        return f"https://api.sejm.gov.pl/eli/acts/{m[1]}/{m[2]}/{m[3]}/text.pdf"
    return url


class _HttpsOnlyRedirects(urllib.request.HTTPRedirectHandler):
    """Przekierowanie tylko na inny adres https://. Bez tego serwer mógłby odesłać na http://."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if not newurl.startswith("https://"):
            raise urllib.error.URLError(f"przekierowanie poza https: {newurl}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _retryable(e: Exception) -> bool:
    """Błąd sieci albo serwera, po którym warto spróbować jeszcze raz."""
    if isinstance(e, urllib.error.HTTPError):
        return e.code >= 500
    if isinstance(e, urllib.error.URLError):
        return isinstance(e.reason, OSError)       # nie: przekierowanie poza https
    return isinstance(e, (TimeoutError, ConnectionError))


def _fetch_once(url: str, headers: dict[str, str], max_bytes: int, timeout: float) -> tuple[bytes, str]:
    deadline = time.monotonic() + timeout
    req = urllib.request.Request(url, headers=headers)
    # Opener powstaje dopiero tutaj, po truststore: HTTPSHandler tworzy kontekst SSL przy budowie.
    opener = urllib.request.build_opener(_HttpsOnlyRedirects)
    with opener.open(req, timeout=min(timeout, _SOCKET_TIMEOUT)) as r:
        ctype = r.headers.get("Content-Type", "")
        chunks: list[bytes] = []
        size = 0
        # read1 wraca po jednym odczycie z gniazda, więc serwer wysyłający dane po bajcie
        # nie zablokuje pętli dłużej niż limit jednej operacji.
        while chunk := r.read1(_CHUNK):
            chunks.append(chunk)
            size += len(chunk)
            if size > max_bytes:
                raise ValueError(f"odpowiedź spod {url} ma ponad {max_bytes // 2**20} MB")
            if time.monotonic() > deadline:
                raise TimeoutError(f"pobieranie {url} trwa ponad {timeout:g} s")
    return b"".join(chunks), ctype


def fetch_bytes(url: str, headers: dict[str, str], max_bytes: int,
                timeout: float | None = None) -> tuple[bytes, str]:
    """Pobiera adres https:// z łącznym limitem czasu i limitem rozmiaru. Zwraca treść i Content-Type.

    Po błędzie sieci, błędzie serwera (5xx) albo przekroczeniu czasu próbuje jeszcze raz."""
    try:                                   # systemowy magazyn certyfikatów, jeśli dostępny
        import truststore
        truststore.inject_into_ssl()
    except ImportError:
        pass
    limit = FETCH_TIMEOUT if timeout is None else timeout
    try:
        return _fetch_once(url, headers, max_bytes, limit)
    except Exception as e:                 # noqa: BLE001
        if not _retryable(e):
            raise
    return _fetch_once(url, headers, max_bytes, limit)


def normalize(s: str) -> str:
    """Sprowadza tekst do postaci, w której liczy się tylko treść, a nie układ strony."""
    s = re.sub("[\u00ad\u200b\u200c\u200d\u2060\ufeff]", "", s)   # miękki dywiz i znaki zerowej szerokości
    s = re.sub(r"-\s*\n\s*", "", s)                  # przeniesienie wyrazu
    s = s.translate(str.maketrans({"„": '"', "”": '"', "“": '"', "«": '"', "»": '"',
                                   "–": "-", "—": "-", "‑": "-", "’": "'", "ˮ": '"'}))
    return re.sub(r"\s+", "", s).lower()


def _cache_path(url: str) -> Path:
    return CACHE / (hashlib.sha256(url.encode()).hexdigest()[:20] + ".txt")


@functools.lru_cache(maxsize=None)
def _read_cached(p: Path) -> str:
    # Ten sam obiekt tekstu dla tego samego źródła, żeby _normalized_text liczył go raz.
    return p.read_text(encoding="utf-8")


def cached_text(url: str) -> str | None:
    p = _cache_path(text_url(url))
    return _read_cached(p) if p.exists() else None


def fetch_text(url: str) -> str:
    """Pobiera tekst źródła (z pamięci podręcznej, jeśli jest)."""
    turl = text_url(url)
    if not turl.startswith("https://"):     # tylko publiczne strony, bez file:// i http://
        raise ValueError(f"dozwolone są tylko adresy https://, a nie {turl!r}")
    p = _cache_path(turl)
    if p.exists():
        return _read_cached(p)
    body, ctype = fetch_bytes(turl, {"User-Agent": "fikus-sprawdz-cytaty/0.1"}, MAX_BYTES)
    if body[:5] == b"%PDF-" or "pdf" in ctype:
        with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
            f.write(body)
            f.flush()
            text = subprocess.run(["pdftotext", f.name, "-"], check=True, timeout=120,
                                  capture_output=True).stdout.decode("utf-8", "replace")
    else:
        raw = body.decode("utf-8", "replace")
        raw = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", raw)
        text = html.unescape(re.sub(r"(?s)<[^>]+>", " ", raw))
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    with (CACHE / "indeks.tsv").open("a", encoding="utf-8") as idx:   # adres → plik, dla weryfikatora
        idx.write(f"{turl}\t{p.name}\n")
    return _read_cached(p)


@functools.lru_cache(maxsize=32)
def _normalized_text(text: str) -> str:
    return normalize(text)


def quote_in(quote: str, text: str) -> bool:
    """Czy cytat jest w tekście, po sprowadzeniu obu do tej samej postaci (patrz normalize)."""
    return normalize(quote) in _normalized_text(text)

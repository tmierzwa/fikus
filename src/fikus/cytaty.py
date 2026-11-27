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
import threading
import time
import urllib.error
import urllib.request
from collections import Counter, deque
from collections.abc import Callable, Iterable
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from pathlib import Path
from urllib.parse import urlsplit

_REPO = Path(__file__).resolve().parents[2]
CACHE = Path(os.environ.get("FIKUS_CACHE") or (
    _REPO / ".cache" / "zrodla" if (_REPO / "pyproject.toml").is_file()
    else Path.home() / ".cache" / "fikus" / "zrodla"))

MAX_BYTES = 50 * 1024 * 1024    # górny limit pobieranego pliku, żeby zły adres nie zapchał dysku i pamięci
FETCH_TIMEOUT = 120.0           # łączny limit czasu jednego pobrania w sekundach, nie tylko jednej operacji
_SOCKET_TIMEOUT = 30.0          # limit jednej operacji na gnieździe (połączenie, odczyt)
_CHUNK = 64 * 1024
FETCH_WORKERS = 6               # równoległe pobrania razem
FETCH_PER_HOST = 2              # równoległe połączenia z jednym serwerem, żeby nie obciążać urzędów

_lock = threading.Lock()        # zapis do indeks.tsv i jednorazowe włączenie truststore
_truststore_done = False

# Wersja sposobu wydobywania tekstu. Zmiana unieważnia teksty zapisane w .cache/zrodla/.
TEXT_FORMAT = 2

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


class TotalTimeout(TimeoutError):
    """Pobieranie przekroczyło łączny limit czasu. Po nim nie ma ponownej próby."""


def _retryable(e: Exception) -> bool:
    """Błąd sieci albo serwera, po którym warto spróbować jeszcze raz."""
    if isinstance(e, TotalTimeout):
        return False
    if isinstance(e, urllib.error.HTTPError):
        return e.code >= 500
    if isinstance(e, urllib.error.URLError):
        return isinstance(e.reason, OSError)       # nie: przekierowanie poza https
    return isinstance(e, (TimeoutError, ConnectionError))


def _fetch_once(url: str, headers: dict[str, str], max_bytes: int, deadline: float,
                timeout: float) -> tuple[bytes, str]:
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        raise TotalTimeout(f"pobieranie {url} trwa ponad {timeout:g} s")
    req = urllib.request.Request(url, headers=headers)
    # Opener powstaje dopiero tutaj, po truststore: HTTPSHandler tworzy kontekst SSL przy budowie.
    opener = urllib.request.build_opener(_HttpsOnlyRedirects)
    with opener.open(req, timeout=min(remaining, _SOCKET_TIMEOUT)) as r:
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
                raise TotalTimeout(f"pobieranie {url} trwa ponad {timeout:g} s")
    return b"".join(chunks), ctype


def _use_truststore() -> None:
    """Systemowy magazyn certyfikatów, jeśli dostępny. Raz, bo podmienia klasę w module ssl."""
    global _truststore_done
    with _lock:
        if _truststore_done:
            return
        _truststore_done = True
        try:
            import truststore
            truststore.inject_into_ssl()
        except ImportError:
            pass


def fetch_bytes(url: str, headers: dict[str, str], max_bytes: int,
                timeout: float | None = None) -> tuple[bytes, str]:
    """Pobiera adres https:// z łącznym limitem czasu i limitem rozmiaru. Zwraca treść i Content-Type.

    Po błędzie sieci, błędzie serwera (5xx) albo przekroczeniu czasu jednej operacji próbuje jeszcze
    raz. Obie próby mieszczą się w jednym łącznym limicie czasu; po jego przekroczeniu nie ma drugiej."""
    if not url.startswith("https://"):     # build_opener obsługuje też file:// i http://
        raise ValueError(f"dozwolone są tylko adresy https://, a nie {url!r}")
    _use_truststore()
    limit = FETCH_TIMEOUT if timeout is None else timeout
    deadline = time.monotonic() + limit
    try:
        return _fetch_once(url, headers, max_bytes, deadline, limit)
    except Exception as e:                 # noqa: BLE001
        if not _retryable(e):
            raise
    return _fetch_once(url, headers, max_bytes, deadline, limit)


def normalize(s: str) -> str:
    """Sprowadza tekst do postaci, w której liczy się tylko treść, a nie układ strony."""
    s = re.sub("[\u00ad\u200b\u200c\u200d\u2060\ufeff]", "", s)   # miękki dywiz i znaki zerowej szerokości
    s = re.sub(r"-\s*\n\s*", "", s)                  # przeniesienie wyrazu
    s = s.translate(str.maketrans({"„": '"', "”": '"', "“": '"', "«": '"', "»": '"',
                                   "–": "-", "—": "-", "‑": "-", "’": "'", "ˮ": '"'}))
    return re.sub(r"\s+", "", s).lower()


def _cache_path(url: str) -> Path:
    key = f"{TEXT_FORMAT}:{url}"
    return CACHE / (hashlib.sha256(key.encode()).hexdigest()[:20] + ".txt")


_TAG = re.compile(r"(?s)<[^>]+>")
_ATTR = re.compile(r"""([\w:.-]+)\s*=\s*(?:"([^"]*)"|'([^']*)')""")
APPENDIX = "\n\n[atrybuty]\n"   # oddziela tekst dokumentu od wartości atrybutów


def _is_xml(body: bytes, ctype: str) -> bool:
    head = body[:200].lstrip(b"\xef\xbb\xbf \t\r\n").lower()
    return head.startswith(b"<?xml") and b"<!doctype html" not in head and b"<html" not in head \
        or ("xml" in ctype and "html" not in ctype)


def markup_text(raw: str, xml: bool) -> str:
    """Tekst strony albo pliku XML bez znaczników. Wartości atrybutów (w XML wszystkie, na stronie
    adresy linków href) idą osobno na koniec tekstu, każda w swoim wierszu, żeby nie rozdzielały
    cytatów z treści. Tak da się zacytować kod systemowy ze schematu XSD i adres pliku z linku."""
    raw = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", raw)
    values = []
    for tag in _TAG.findall(raw):
        for name, v1, v2 in _ATTR.findall(tag):
            if xml or name.lower() == "href":
                values.append(html.unescape(v1 or v2))
    text = html.unescape(_TAG.sub(" ", raw))
    return text + APPENDIX + "\n".join(values) if values else text


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
        text = markup_text(body.decode("utf-8", "replace"), _is_xml(body, ctype))
    p.parent.mkdir(parents=True, exist_ok=True)
    # Plik tymczasowy i zamiana nazwy: inny wątek albo przerwany przebieg nie zobaczy połowy tekstu.
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=p.parent, suffix=".tmp",
                                     delete=False) as tmp:
        try:
            tmp.write(text)
        except BaseException:
            tmp.close()
            os.unlink(tmp.name)
            raise
    try:
        os.replace(tmp.name, p)
    except BaseException:
        os.unlink(tmp.name)
        raise
    with _lock, (CACHE / "indeks.tsv").open("a", encoding="utf-8") as idx:   # adres → plik, dla weryfikatora
        idx.write(f"{turl}\t{p.name}\n")
    return _read_cached(p)


def prefetch(urls: Iterable[str], fetch: Callable[[str], object] = fetch_text,
             workers: int = FETCH_WORKERS, per_host: int = FETCH_PER_HOST) -> dict[str, Exception]:
    """Pobiera adresy równolegle: najwyżej `workers` naraz i `per_host` z jednego serwera.

    Zwraca błędy pobierania według adresu; pobrane teksty trafiają do pamięci podręcznej.
    Adres trafia do puli dopiero wtedy, gdy jego serwer ma wolne miejsce, więc żaden wątek nie
    czeka bezczynnie na serwer zajęty przez inne wątki. Najpierw idą serwery z najdłuższą kolejką.
    """
    queues: dict[str, deque[str]] = {}
    for url in dict.fromkeys(urls):
        queues.setdefault(urlsplit(url).hostname or "", deque()).append(url)
    active: Counter[str] = Counter()
    errors: dict[str, Exception] = {}
    with ThreadPoolExecutor(max_workers=workers) as pool:
        running = {}

        def fill() -> None:
            while len(running) < workers:
                free = [h for h, q in queues.items() if q and active[h] < per_host]
                if not free:
                    return
                host = max(free, key=lambda h: len(queues[h]))
                url = queues[host].popleft()
                active[host] += 1
                running[pool.submit(fetch, url)] = (host, url)

        fill()
        while running:
            done, _ = wait(running, return_when=FIRST_COMPLETED)
            for f in done:
                host, url = running.pop(f)
                active[host] -= 1
                if (e := f.exception()) is not None:
                    errors[url] = e   # type: ignore[assignment]
            fill()
    return errors


@functools.lru_cache(maxsize=32)
def _normalized_text(text: str) -> str:
    return normalize(text)


def quote_in(quote: str, text: str) -> bool:
    """Czy cytat jest w tekście, po sprowadzeniu obu do tej samej postaci (patrz normalize)."""
    return normalize(quote) in _normalized_text(text)

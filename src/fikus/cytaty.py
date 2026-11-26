"""Mechaniczne sprawdzanie cytatów: czy dosłowny fragment zapisany przy źródle jest w jego tekście.

Tekst źródła pobiera się spod oficjalnego adresu (PDF tekstu jednolitego, obwieszczenia, strona
urzędu) i zapisuje w .cache/zrodla/. Porównanie ignoruje wielkość liter, białe znaki, przeniesienia
wyrazów i rodzaj cudzysłowów i myślników, bo tak różnią się teksty wyciągnięte z PDF.
"""
from __future__ import annotations

import hashlib
import html
import os
import re
import subprocess
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
CACHE = Path(os.environ.get("FIKUS_CACHE") or (
    _REPO / ".cache" / "zrodla" if (_REPO / "pyproject.toml").is_file()
    else Path.home() / ".cache" / "fikus" / "zrodla"))

MAX_BYTES = 50 * 1024 * 1024    # górny limit pobieranego pliku, żeby zły adres nie zapchał dysku i pamięci

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


def normalize(s: str) -> str:
    """Sprowadza tekst do postaci, w której liczy się tylko treść, a nie układ strony."""
    s = re.sub("[\u00ad\u200b\u200c\u200d\u2060\ufeff]", "", s)   # miękki dywiz i znaki zerowej szerokości
    s = re.sub(r"-\s*\n\s*", "", s)                  # przeniesienie wyrazu
    s = s.translate(str.maketrans({"„": '"', "”": '"', "“": '"', "«": '"', "»": '"',
                                   "–": "-", "—": "-", "‑": "-", "’": "'", "ˮ": '"'}))
    return re.sub(r"\s+", "", s).lower()


def _cache_path(url: str) -> Path:
    return CACHE / (hashlib.sha256(url.encode()).hexdigest()[:20] + ".txt")


def cached_text(url: str) -> str | None:
    p = _cache_path(text_url(url))
    return p.read_text(encoding="utf-8") if p.exists() else None


def fetch_text(url: str) -> str:
    """Pobiera tekst źródła (z pamięci podręcznej, jeśli jest)."""
    turl = text_url(url)
    if not turl.startswith("https://"):     # tylko publiczne strony, bez file:// i http://
        raise ValueError(f"dozwolone są tylko adresy https://, a nie {turl!r}")
    p = _cache_path(turl)
    if p.exists():
        return p.read_text(encoding="utf-8")
    try:                                   # systemowy magazyn certyfikatów, jeśli dostępny
        import truststore
        truststore.inject_into_ssl()
    except ImportError:
        pass
    req = urllib.request.Request(turl, headers={"User-Agent": "fikus-sprawdz-cytaty/0.1"})
    # Opener powstaje dopiero tutaj, po truststore: HTTPSHandler tworzy kontekst SSL przy budowie.
    opener = urllib.request.build_opener(_HttpsOnlyRedirects)
    with opener.open(req, timeout=60) as r:
        body, ctype = r.read(MAX_BYTES + 1), r.headers.get("Content-Type", "")
    if len(body) > MAX_BYTES:
        raise ValueError(f"tekst spod {turl} ma ponad {MAX_BYTES // 2**20} MB")
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
    return text


def quote_in(quote: str, text: str) -> bool:
    """Czy cytat jest w tekście, po sprowadzeniu obu do tej samej postaci (patrz normalize)."""
    return normalize(quote) in normalize(text)

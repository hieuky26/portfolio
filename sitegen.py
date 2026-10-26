# -*- coding: utf-8 -*-
"""
Logic dung chung cho ca server dev (app.py) lan build tinh (build.py).

Diem khac nhau duy nhat giua hai che do la URL doi ngon ngu:
  - dev  : "?lang=en" / "?lang=vi"   (mot route "/" duy nhat)
  - tinh : "/"        / "/vi/"       (hai file HTML rieng)
Cho nen `build_context()` nhan tham so `urls` de template khong can biet
minh dang chay o che do nao.
"""

import hashlib
from pathlib import Path

import content as C
from ui import UI

BASE_DIR = Path(__file__).resolve().parent

# URL doi ngon ngu o tung che do
DEV_URLS = {"en": "?lang=en", "vi": "?lang=vi"}
STATIC_URLS = {"en": "/", "vi": "/vi/"}


def localize(value, lang):
    """Duyet de quy du lieu, thay moi dict {'en':..,'vi':..} bang chuoi cua `lang`."""
    if isinstance(value, dict):
        keys = set(value.keys())
        if keys and keys <= set(C.LANGS) and all(isinstance(v, str) for v in value.values()):
            return value.get(lang) or value.get(C.DEFAULT_LANG) or ""
        return {k: localize(v, lang) for k, v in value.items()}
    if isinstance(value, list):
        return [localize(v, lang) for v in value]
    return value


def site_root() -> str:
    """Dia chi goc cua site, khong co dau / o cuoi."""
    return (C.PROFILE.get("website") or "").rstrip("/")


def absolute_urls() -> dict:
    """URL tuyet doi cua tung ban ngon ngu, dung cho canonical / hreflang / sitemap."""
    root = site_root()
    return {lang: root + path for lang, path in STATIC_URLS.items()}


_asset_cache: dict = {}


def asset(path: str) -> str:
    """
    Gan van ban theo noi dung file: "/static/css/style.css" -> ".../style.css?v=1a2b3c4d".

    Nho vay tai nguyen tinh moi cache duoc 1 nam ma sua file la trinh duyet
    van lay ban moi ngay, vi URL doi theo.
    """
    if not path:
        return path

    file_path = BASE_DIR / path.lstrip("/")
    try:
        stat = file_path.stat()
    except OSError:
        return path  # thieu file thi tra nguyen path, de fallback phia client lo

    # Khoa cache theo thoi diem sua + kich thuoc, de luc dev sua file la hash doi ngay
    key = (path, stat.st_mtime_ns, stat.st_size)
    cached = _asset_cache.get(key)
    if cached:
        return cached

    digest = hashlib.sha1(file_path.read_bytes()).hexdigest()[:8]
    result = f"{path}?v={digest}"
    _asset_cache[key] = result
    return result


def build_context(lang: str, urls: dict) -> dict:
    """Dung toan bo context cho template index.html."""
    other_lang = "vi" if lang == "en" else "en"
    alternates = absolute_urls()

    return {
        "lang": lang,
        "other_lang": other_lang,
        "ui": UI[lang],
        "urls": urls,
        "asset": asset,
        "canonical": alternates[lang],
        "alternates": alternates,
        "profile": localize(C.PROFILE, lang),
        "stats": localize(C.STATS, lang),
        "skills": localize(C.SKILLS, lang),
        "experience": localize(C.EXPERIENCE, lang),
        "education": localize(C.EDUCATION, lang),
        "projects": localize(C.PROJECTS, lang),
    }


def robots_txt() -> str:
    return f"User-agent: *\nAllow: /\nSitemap: {site_root()}/sitemap.xml\n"


def sitemap_xml() -> str:
    alternates = absolute_urls()
    entries = []
    for lang in C.LANGS:
        priority = "1.0" if lang == C.DEFAULT_LANG else "0.9"
        links = "".join(
            f'<xhtml:link rel="alternate" hreflang="{other}" href="{href}"/>'
            for other, href in alternates.items()
        )
        entries.append(
            f"<url><loc>{alternates[lang]}</loc>{links}"
            f"<changefreq>monthly</changefreq><priority>{priority}</priority></url>"
        )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">'
        + "".join(entries)
        + "</urlset>"
    )

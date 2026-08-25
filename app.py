# -*- coding: utf-8 -*-
"""
Portfolio - Lê Hiếu Kỳ
FastAPI + Jinja2, mot trang, song ngu EN/VI.

Noi dung: sua trong content.py
Nhan giao dien: sua trong ui.py
Giao dien: static/css/style.css, static/js/main.js
"""

import os

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import content as C
from ui import UI

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

LANG_COOKIE = "lang"
COOKIE_MAX_AGE = 60 * 60 * 24 * 365  # 1 nam

app = FastAPI(title="Lê Hiếu Kỳ - Portfolio", docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATES_DIR)


# --------------------------------------------------------------------------
# Ngon ngu
# --------------------------------------------------------------------------
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


def resolve_lang(request: Request) -> str:
    """Uu tien ?lang= tren URL, sau do la cookie, cuoi cung la Accept-Language."""
    q = (request.query_params.get("lang") or "").lower()
    if q in C.LANGS:
        return q

    cookie = (request.cookies.get(LANG_COOKIE) or "").lower()
    if cookie in C.LANGS:
        return cookie

    accept = (request.headers.get("accept-language") or "").lower()
    if accept.startswith("vi") or ",vi" in accept:
        return "vi"

    return C.DEFAULT_LANG


# --------------------------------------------------------------------------
# Routes
# --------------------------------------------------------------------------
@app.get("/")
async def home(request: Request):
    lang = resolve_lang(request)
    ui = UI[lang]
    other_lang = "vi" if lang == "en" else "en"

    ctx = {
        "lang": lang,
        "other_lang": other_lang,
        "ui": ui,
        "profile": localize(C.PROFILE, lang),
        "stats": localize(C.STATS, lang),
        "skills": localize(C.SKILLS, lang),
        "experience": localize(C.EXPERIENCE, lang),
        "education": localize(C.EDUCATION, lang),
        "projects": localize(C.PROJECTS, lang),
    }

    response = templates.TemplateResponse(request=request, name="index.html", context=ctx)

    # Nho lua chon ngon ngu khi nguoi dung bam nut chuyen
    if request.query_params.get("lang", "").lower() in C.LANGS:
        response.set_cookie(
            LANG_COOKIE, lang, max_age=COOKIE_MAX_AGE, httponly=False, samesite="lax"
        )
    return response


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/cv")
async def cv():
    """Chuyen huong toi file CV neu da khai bao cv_url trong content.py."""
    url = C.PROFILE.get("cv_url")
    if url:
        return RedirectResponse(url)
    return RedirectResponse("/#contact")


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return RedirectResponse("/static/img/favicon.svg", status_code=301)


@app.get("/robots.txt", response_class=PlainTextResponse)
async def robots():
    site = C.PROFILE.get("website", "").rstrip("/")
    return f"User-agent: *\nAllow: /\nSitemap: {site}/sitemap.xml\n"


@app.get("/sitemap.xml")
async def sitemap():
    site = C.PROFILE.get("website", "").rstrip("/")
    urls = "".join(
        f"<url><loc>{site}/?lang={lang}</loc><changefreq>monthly</changefreq></url>"
        for lang in C.LANGS
    )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"<url><loc>{site}/</loc><changefreq>monthly</changefreq><priority>1.0</priority></url>"
        f"{urls}</urlset>"
    )
    return PlainTextResponse(xml, media_type="application/xml")


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)

# -*- coding: utf-8 -*-
"""
Portfolio - Lê Hiếu Kỳ — server dev.

Trang that chay o dang HTML tinh tren Cloudflare Pages (xem build.py).
File nay chi dung khi lam viec o may: co reload, co ?lang=, co cookie.

Noi dung: sua trong content.py
Nhan giao dien: sua trong ui.py
"""

import os

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import content as C
import sitegen as S

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

LANG_COOKIE = "lang"
COOKIE_MAX_AGE = 60 * 60 * 24 * 365  # 1 nam

app = FastAPI(title="Lê Hiếu Kỳ - Portfolio", docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATES_DIR)


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


def render(request: Request, lang: str):
    ctx = S.build_context(lang, S.DEV_URLS)
    return templates.TemplateResponse(request=request, name="index.html", context=ctx)


@app.get("/")
async def home(request: Request):
    lang = resolve_lang(request)
    response = render(request, lang)

    # Nho lua chon ngon ngu khi nguoi dung bam nut chuyen
    if request.query_params.get("lang", "").lower() in C.LANGS:
        response.set_cookie(
            LANG_COOKIE, lang, max_age=COOKIE_MAX_AGE, httponly=False, samesite="lax"
        )
    return response


@app.get("/vi/")
async def home_vi(request: Request):
    """Khop voi duong dan cua ban tinh de link /vi/ khong bi 404 luc dev."""
    return render(request, "vi")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/cv")
async def cv():
    """Chuyen huong toi file CV neu da khai bao cv_url trong content.py."""
    return RedirectResponse(C.PROFILE.get("cv_url") or "/#contact")


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return RedirectResponse("/static/img/favicon.svg", status_code=301)


@app.get("/robots.txt", response_class=PlainTextResponse)
async def robots():
    return S.robots_txt()


@app.get("/sitemap.xml")
async def sitemap():
    return PlainTextResponse(S.sitemap_xml(), media_type="application/xml")


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)

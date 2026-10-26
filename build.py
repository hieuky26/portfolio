# -*- coding: utf-8 -*-
"""
Xuat trang ra HTML tinh vao thu muc dist/.

    python build.py

Ket qua:
    dist/index.html         ban tieng Anh
    dist/vi/index.html      ban tieng Viet
    dist/static/...         css, js, anh
    dist/robots.txt
    dist/sitemap.xml
    dist/_headers           quy tac cache (Netlify doc file nay)

Deploy: Netlify doc netlify.toml, build command "python build.py",
output directory "dist".
"""

import shutil
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

import content as C
import sitegen as S

BASE_DIR = Path(__file__).resolve().parent
DIST = BASE_DIR / "dist"
STATIC_SRC = BASE_DIR / "static"
TEMPLATES = BASE_DIR / "templates"

# Cache: tai nguyen tinh giu 1 nam, HTML luon kiem tra lai de sua noi dung la thay ngay
HEADERS = """\
/static/*
  Cache-Control: public, max-age=31536000, immutable

/*.html
  Cache-Control: public, max-age=0, must-revalidate

/
  Cache-Control: public, max-age=0, must-revalidate
"""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    size = len(text.encode("utf-8"))
    print(f"  {path.relative_to(DIST).as_posix():<24} {size:>8,} B")


def main() -> int:
    if not TEMPLATES.is_dir():
        print(f"Khong tim thay thu muc templates: {TEMPLATES}", file=sys.stderr)
        return 1

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES)),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=False,
        lstrip_blocks=False,
    )
    template = env.get_template("index.html")

    print(f"Build -> {DIST}")

    # 1. Trang cho tung ngon ngu
    for lang in C.LANGS:
        ctx = S.build_context(lang, S.STATIC_URLS)
        html = template.render(**ctx)
        out = DIST / "index.html" if lang == C.DEFAULT_LANG else DIST / lang / "index.html"
        write(out, html)

    # 2. Tai nguyen tinh
    shutil.copytree(STATIC_SRC, DIST / "static")
    files = sum(1 for _ in (DIST / "static").rglob("*") if _.is_file())
    total = sum(f.stat().st_size for f in (DIST / "static").rglob("*") if f.is_file())
    print(f"  {'static/':<24} {total:>8,} B  ({files} file)")

    # 3. SEO + cache
    write(DIST / "robots.txt", S.robots_txt())
    write(DIST / "sitemap.xml", S.sitemap_xml())
    write(DIST / "_headers", HEADERS)

    print("Xong.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

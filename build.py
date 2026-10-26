import os
from jinja2 import Environment, FileSystemLoader
import content as C
from ui import UIimport os
import shutil
from jinja2 import Environment, FileSystemLoader
import content as C
from ui import UI
from app import localize

os.makedirs("static", exist_ok=True)
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("index.html")

lang = C.DEFAULT_LANG
ui_data = UI[lang]
other_lang = "en" if lang == "vi" else "vi"

ctx = {
    "lang": lang,
    "other_lang": other_lang,
    "ui": ui_data,
    "profile": localize(C.PROFILE, lang),
    "stats": localize(C.STATS, lang),
    "skills": localize(C.SKILLS, lang),
    "experience": localize(C.EXPERIENCE, lang),
    "education": localize(C.EDUCATION, lang),
    "projects": localize(C.PROJECTS, lang),
}

html = template.render(**ctx)
with open("static/index.html", "w", encoding="utf-8") as f:
    f.write(html)

static_nested_dir = os.path.join("static", "static")
os.makedirs(static_nested_dir, exist_ok=True)

for item in os.listdir("static"):
    if item == "static":
        continue
    src_path = os.path.join("static", item)
    dst_path = os.path.join(static_nested_dir, item)
    if os.path.isdir(src_path):
        if os.path.exists(dst_path):
            shutil.rmtree(dst_path)
        shutil.copytree(src_path, dst_path)
    else:
        shutil.copy2(src_path, dst_path)

from app import localize

os.makedirs("static", exist_ok=True)
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("index.html")

lang = C.DEFAULT_LANG
ui_data = UI[lang]
other_lang = "en" if lang == "vi" else "vi"

ctx = {
    "lang": lang,
    "other_lang": other_lang,
    "ui": ui_data,
    "profile": localize(C.PROFILE, lang),
    "stats": localize(C.STATS, lang),
    "skills": localize(C.SKILLS, lang),
    "experience": localize(C.EXPERIENCE, lang),
    "education": localize(C.EDUCATION, lang),
    "projects": localize(C.PROJECTS, lang)
}

html = template.render(**ctx)
with open("static/index.html", "w", encoding="utf-8") as f:
    f.write(html)

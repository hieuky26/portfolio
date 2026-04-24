import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

# 🔥 Lấy path tuyệt đối (QUAN TRỌNG cho Render)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 🔥 Static folder
static_path = os.path.join(BASE_DIR, "static")
if not os.path.exists(static_path):
    print("❌ static folder NOT FOUND:", static_path)

app.mount("/static", StaticFiles(directory=static_path), name="static")

# 🔥 Templates folder
templates_path = os.path.join(BASE_DIR, "templates")
if not os.path.exists(templates_path):
    print("❌ templates folder NOT FOUND:", templates_path)

templates = Jinja2Templates(directory=templates_path)


# ✅ ROUTE TEST (check backend)
@app.get("/test")
async def test():
    return {"status": "ok"}


# 🔥 ROUTE CHÍNH
@app.get("/")
async def home(request: Request):
    print("🔥 HOME FUNCTION CALLED")

    user = {
        "name": "Lê Hiếu Kỳ",
        "title": "Data Analyst Fresher | Web Developer",
        "email": "lehieuky26@gmail.com",
        "phone": "0929331521",
        "location": "Ho Chi Minh City",
        "about": "Fresher Data Analyst with experience in AI and data visualization.",

        "skills": [
            {"name": "Python", "details": "Advanced programming with data processing, automation, and web frameworks"},
            {"name": "SQL", "details": "Database design, complex queries, and data manipulation"},
            {"name": "FastAPI", "details": "Building high-performance REST APIs with async support"},
            {"name": "MongoDB", "details": "NoSQL database design, document modeling, and aggregation"},
            {"name": "Data Analysis", "details": "Statistical analysis, data cleaning, and insights extraction"},
            {"name": "Machine Learning", "details": "Supervised/unsupervised learning, model training, and evaluation"},
            {"name": "HTML/CSS", "details": "Responsive web design, animations, and modern UI frameworks"}
        ],

        "experience": [
            {
                "company": "NewAI",
                "role": "Data Analyst Intern",
                "time": "07/2023 - 01/2024",
                "desc": "Analyzed datasets and built visualization system."
            }
        ],

        "education": "Ton Duc Thang University - Computer Science (2019-2024)",

        "projects": [
            {
                "name": "Hate Speech Detection AI",
                "desc": "AI system using NLP & ML."
            },
            {
                "name": "Data Visualization Website",
                "desc": "Compare ML models visually."
            }
        ]
    }

    print("USER DATA:", user)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "user": user
        }
    )


# 🔥 RUN LOCAL / RENDER
if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("app:app", host="0.0.0.0", port=port)

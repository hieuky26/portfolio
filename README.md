# Portfolio — Lê Hiếu Kỳ

Trang portfolio một trang, song ngữ EN/VI, dựng bằng FastAPI + Jinja2.
Giao diện theo hệ màu thương hiệu Zyxel (primary `#288719`, accent `#6CBE45`, font Inter / Noto Sans).

Live: https://hieuky.is-a.dev

## Sửa nội dung

Toàn bộ nội dung nằm ở hai file Python, **không cần đụng vào HTML/CSS**:

| File | Chứa gì |
|---|---|
| `content.py` | Thông tin cá nhân, kỹ năng, kinh nghiệm, học vấn, dự án, số liệu hero |
| `ui.py` | Nhãn giao diện: menu, tiêu đề mục, nút bấm, mô tả SEO |

Chỗ nào cần song ngữ thì viết dạng `{"en": "...", "vi": "..."}`; chỗ nào dùng chung
(tên riêng, năm, tên công nghệ) thì để chuỗi thường.

Tìm `TODO` trong `content.py` để thấy các mục cần điền/kiểm tra lại.

## Chạy ở máy

```bash
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt
.venv/Scripts/python.exe -m uvicorn app:app --reload --port 8000
```

Mở http://localhost:8000

Trên macOS/Linux thay `.venv/Scripts/python.exe` bằng `.venv/bin/python`.

## Cấu trúc

```
app.py                  FastAPI: route, chọn ngôn ngữ, SEO
content.py              Dữ liệu nội dung
ui.py                   Nhãn giao diện theo ngôn ngữ
templates/index.html    Trang chính
templates/_icons.html   Macro icon SVG
static/css/style.css    Design tokens + toàn bộ giao diện
static/js/main.js       Nav, reveal khi cuộn, panel kỹ năng, nút copy
static/img/favicon.svg  Favicon
render.yaml             Cấu hình deploy Render
```

## Ngôn ngữ

Thứ tự ưu tiên: `?lang=` trên URL → cookie `lang` → header `Accept-Language` → mặc định `en`.
Nút EN/VI trên thanh nav trỏ tới `?lang=...` và ghi cookie nhớ 1 năm.

## Route

| Route | Mô tả |
|---|---|
| `/` | Trang chính |
| `/?lang=en` `/?lang=vi` | Chọn ngôn ngữ |
| `/health` | Health check cho Render |
| `/cv` | Chuyển hướng tới `PROFILE["cv_url"]`, chưa có thì về `#contact` |
| `/robots.txt`, `/sitemap.xml` | SEO |

## Deploy

Render đọc `render.yaml`: build bằng `pip install -r requirements.txt`,
chạy `uvicorn app:app --host 0.0.0.0 --port $PORT`, health check ở `/health`.
Push lên nhánh chính là Render tự deploy.

## Ghi chú giao diện

- In / xuất PDF: `Ctrl+P` đã có style riêng, ẩn nav, nút và phần trang trí — dùng làm CV nhanh được.
- Tôn trọng `prefers-reduced-motion`: tắt animation nếu người dùng bật giảm chuyển động.
- Không phụ thuộc thư viện JS ngoài; chỉ tải font từ Google Fonts.

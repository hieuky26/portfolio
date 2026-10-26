# Portfolio — Lê Hiếu Kỳ

Trang portfolio một trang, song ngữ EN/VI.
Giao diện theo hệ màu thương hiệu Zyxel (primary `#288719`, accent `#6CBE45`, font Inter / Noto Sans).

Live: https://hieuky.is-a.dev

Nội dung viết bằng Jinja2, nhưng **trang chạy thật là HTML tĩnh** dựng sẵn bằng `build.py`
rồi phục vụ từ CDN. Không có server nào phải khởi động khi có người vào — không còn cold start.

## Sửa nội dung

Toàn bộ nội dung nằm ở hai file Python, **không cần đụng vào HTML/CSS**:

| File | Chứa gì |
|---|---|
| `content.py` | Thông tin cá nhân, kỹ năng, kinh nghiệm, học vấn, dự án, logo, số liệu hero |
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

Mở http://localhost:8000 — có reload, đổi ngôn ngữ bằng `?lang=en` / `?lang=vi`, nhớ bằng cookie.

Trên macOS/Linux thay `.venv/Scripts/python.exe` bằng `.venv/bin/python`.

## Build bản tĩnh

```bash
.venv/Scripts/python.exe build.py
```

Kết quả vào `dist/` (thư mục này nằm trong `.gitignore`, không commit):

```
dist/index.html       bản tiếng Anh
dist/vi/index.html    bản tiếng Việt
dist/static/...       css, js, ảnh
dist/robots.txt
dist/sitemap.xml
dist/_headers         quy tắc cache (Netlify đọc file này)
```

Xem thử bản tĩnh trước khi deploy:

```bash
.venv/Scripts/python.exe -m http.server 8001 --directory dist
```

## Deploy — Netlify

Cấu hình nằm sẵn trong `netlify.toml` (build `pip install -r requirements.txt && python build.py`,
publish `dist`, Python 3.12). Trên Netlify chỉ cần Add new site → Import from Git → chọn repo này;
các ô Build command / Publish directory để trống, Netlify sẽ đọc từ `netlify.toml`.
Mỗi lần push lên `main` là Netlify build lại và deploy.

Netlify chỉ phục vụ file tĩnh — Netlify Functions không chạy Python, nên **không** đưa FastAPI
(`app.py`) lên Netlify. `app.py` chỉ dùng để chạy dev ở máy.

Gắn domain: Site configuration → Domain management → thêm `hieuky.is-a.dev`, rồi sửa bản ghi
trong repo [is-a-dev/register](https://github.com/is-a-dev/register) trỏ CNAME về
hostname `*.netlify.app` mà Netlify cấp.

`render.yaml` vẫn còn trong repo để Render chạy song song trong lúc chuyển DNS.
Chuyển xong thì xoá file đó và tắt service bên Render.

## Ngôn ngữ

| Chế độ | URL |
|---|---|
| Bản tĩnh | `/` (EN) và `/vi/` (VI) |
| Server dev | `/?lang=en` và `/?lang=vi`, thêm `/vi/` cho khớp bản tĩnh |

Bản tĩnh không có cookie phía server nên dùng `localStorage` để nhớ lựa chọn:
một đoạn script nhỏ trong `<head>` chỉ đẩy từ `/` sang `/vi/`, không bao giờ đẩy ngược,
nên không thể lặp vô tận. Script này cũng đỡ các link cũ dạng `/?lang=vi`.

## Cấu trúc

```
app.py                  Server dev: route, cookie, ?lang=
build.py                Xuất HTML tĩnh ra dist/
sitegen.py              Logic dùng chung cho app.py và build.py
content.py              Dữ liệu nội dung
ui.py                   Nhãn giao diện theo ngôn ngữ
templates/index.html    Trang chính
templates/_icons.html   Macro icon SVG
static/css/style.css    Design tokens + toàn bộ giao diện
static/js/main.js       Nav, reveal khi cuộn, panel kỹ năng, nút copy, nhớ ngôn ngữ
static/img/             favicon + logo
```

> Không đặt tên file là `site.py` — trùng với module chuẩn của Python và sẽ che mất nó.

## Ghi chú giao diện

- In / xuất PDF: `Ctrl+P` đã có style riêng, ẩn nav, nút và phần trang trí — dùng làm CV nhanh được.
- Tôn trọng `prefers-reduced-motion`: tắt animation nếu người dùng bật giảm chuyển động.
- Không phụ thuộc thư viện JS ngoài; chỉ tải font từ Google Fonts.
- Thiếu file logo thì nav tự quay về ô vuông chữ cái, không để lại ảnh vỡ.

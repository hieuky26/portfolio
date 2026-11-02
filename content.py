# -*- coding: utf-8 -*-
"""
Toan bo noi dung cua portfolio nam o file nay.
Muon sua thong tin -> chi can sua file nay, khong can dung vao app.py / template.

Quy uoc:
  - PROFILE / SKILLS / EXPERIENCE / PROJECTS / EDUCATION: du lieu dung chung,
    phan chu nao can song ngu thi viet dang {"en": "...", "vi": "..."}.
  - UI (trong file ui.py): nhan giao dien theo tung ngon ngu.

Cac dong danh dau "TODO" la cho can kiem tra lai cho khop thuc te.
"""

LANGS = ("en", "vi")
DEFAULT_LANG = "en"


def t(value, lang):
    """Lay chuoi theo ngon ngu. Nhan ca str thuong lan dict {'en':.., 'vi':..}."""
    if isinstance(value, dict):
        return value.get(lang) or value.get(DEFAULT_LANG) or ""
    return value


# --------------------------------------------------------------------------
# 1. THONG TIN CA NHAN
# --------------------------------------------------------------------------
PROFILE = {
    "name": "Lê Hiếu Kỳ",
    "initials": "HK",
    # Logo o thanh nav. De "" -> quay ve dau hieu chu cai (initials).
    # Neu file khong ton tai thi trang tu dong quay ve initials, khong bi vo layout.
    # Logo Zyxel Networks dang SVG: ban chu den cho nen sang, ban chu trang cho dark mode
    # (guideline cho phep ca hai, chon ban tuong phan nhat voi nen). X luon xanh #3C9F00.
    "logo": "/static/img/zyxel-networks.svg",
    "logo_dark": "/static/img/zyxel-networks-white.svg",
    "logo_alt": "Zyxel Networks",
    "role": {
        "en": "System Integration Engineer",
        "vi": "Kỹ sư Tích hợp Hệ thống",
    },
    "company": "Zyxel Networks Việt Nam",
    "company_url": "https://www.zyxel.com/vn",
    "tagline": {
        "en": "I integrate networking hardware with back-end systems, and automate the parts that repeat.",
        "vi": "Tôi tích hợp thiết bị mạng với hệ thống back-end, và tự động hoá những phần lặp đi lặp lại.",
    },
    "about": {
        "en": (
            "I work where networking meets software: bringing access points, switches and firewalls "
            "together with the Linux server stacks, RADIUS and captive-portal services that sit behind "
            "them. A large part of the job is making that integration repeatable: I write Python tooling that "
            "turns hundreds of manual device configurations into a reviewed, logged, one-click run. "
            "I started out in data analysis, so I still reach for Python, SQL and a clear chart "
            "whenever a system needs to explain itself."
        ),
        "vi": (
            "Tôi làm ở phần giao giữa hạ tầng mạng và phần mềm: ghép access point, switch, firewall "
            "với các stack server Linux, dịch vụ RADIUS và captive portal phía sau. Phần lớn công việc "
            "là làm cho việc tích hợp đó lặp lại được. Tôi viết công cụ Python biến hàng trăm thao tác "
            "cấu hình thủ công thành một lần chạy có kiểm duyệt và có log. Xuất phát từ mảng phân tích "
            "dữ liệu, tôi vẫn quen dùng Python, SQL và một biểu đồ rõ ràng để hệ thống tự nói lên "
            "vấn đề của nó."
        ),
    },
    "email": "lehieuky26@gmail.com",
    "work_email": "Ky.Le@zyxel.ai.vn",                 # de "" neu khong muon hien email cong ty
    "phone": "0929 331 521",
    "phone_href": "+84929331521",
    "location": {"en": "Ho Chi Minh City, Vietnam", "vi": "TP. Hồ Chí Minh, Việt Nam"},
    "github": "https://github.com/hieuky26",
    "linkedin": "",                                    # TODO: dan link LinkedIn neu co
    "website": "https://hieuky.is-a.dev",
    "cv_url": "",                                      # TODO: link CV PDF -> se hien nut "Download CV"
}

# So lieu noi bat o hero. Dang de trong -> khoi so lieu khong hien.
# Muon bat lai thi dien so THAT vao, vi du:
#   {"value": "100+", "label": {"en": "Devices managed",  "vi": "Thiết bị quản trị"}},
#   {"value": "10+",  "label": {"en": "Systems deployed", "vi": "Hệ thống triển khai"}},
# Tranh dung "so nam kinh nghiem" vi se lech voi moc 06/2026 o phan Kinh nghiem.
STATS = []


# Khung terminal trang tri o hero: mo phong mot lan chay dry-run cua cong cu SSH hang loat.
# Moi dong: [kieu, chu]. Kieu: "cmd" lenh go vao, "info" dong xam, "ok" dong co dau tick xanh,
# "done" dong ket qua. Giu moi dong duoi ~38 ky tu de khong tran tren dien thoai.
HERO_TERMINAL = {
    "title": "ssh-bulk: dry-run",
    "lines": [
        ["cmd", "ssh-bulk run vlan.j2 --dry-run"],
        ["info", "sites.csv · 128 devices · 8 workers"],
        ["ok", "AP-HCM-01     3 cmds   ok"],
        ["ok", "AP-HCM-02     3 cmds   ok"],
        ["ok", "SW-CORE-01    5 cmds   ok"],
        ["info", "… 125 more"],
        ["done", {"en": "passed · 0 blocked · log saved", "vi": "đạt · 0 lệnh bị chặn · đã lưu log"}],
    ],
    # Nhan nho o goc khung
    "stack": ["Ubuntu", "FreeRADIUS", "Nginx", "MongoDB"],
}


# --------------------------------------------------------------------------
# 2. KY NANG
# --------------------------------------------------------------------------
SKILLS = [
    {
        "group": {"en": "Networking & Infrastructure", "vi": "Hạ tầng & Mạng"},
        "icon": "network",
        "items": [
            {"name": "Zyxel AP / Switch / Firewall",
             "detail": {"en": "Provisioning, radio profiles, VLAN and firmware operations across fleets of devices.",
                        "vi": "Cấu hình, radio profile, VLAN và nâng cấp firmware cho số lượng lớn thiết bị."}},
            {"name": "SSH Automation",
             "detail": {"en": "Template-driven bulk configuration with dry-run, parallel execution and per-device transcripts.",
                        "vi": "Chạy lệnh hàng loạt theo template, có dry-run, chạy song song và log transcript từng thiết bị."}},
            {"name": "FreeRADIUS",
             "detail": {"en": "802.1X and captive-portal authentication backed by MySQL.",
                        "vi": "Xác thực 802.1X và captive portal, lưu tài khoản trên MySQL."}},
            {"name": "Nginx",
             "detail": {"en": "Reverse proxy, TLS termination and static serving for production stacks.",
                        "vi": "Reverse proxy, TLS và phục vụ static cho hệ thống production."}},
            {"name": "Linux / Ubuntu",
             "detail": {"en": "Server provisioning, systemd services, log triage and performance tuning.",
                        "vi": "Dựng server, viết service systemd, đọc log và tối ưu hiệu năng."}},
        ],
    },
    {
        "group": {"en": "Back-end & Data Stores", "vi": "Back-end & Cơ sở dữ liệu"},
        "icon": "server",
        "items": [
            {"name": "Python",
             "detail": {"en": "Automation scripts, data pipelines and web services.",
                        "vi": "Script tự động hoá, pipeline dữ liệu và dịch vụ web."}},
            {"name": "FastAPI",
             "detail": {"en": "Async REST APIs, background tasks and server-rendered pages.",
                        "vi": "REST API bất đồng bộ, background task và render trang phía server."}},
            {"name": "MongoDB",
             "detail": {"en": "Document modelling, indexes and aggregation pipelines.",
                        "vi": "Thiết kế document, đánh index và aggregation pipeline."}},
            {"name": "MySQL / SQL",
             "detail": {"en": "Schema design, joins and query tuning for reporting workloads.",
                        "vi": "Thiết kế schema, truy vấn phức tạp và tối ưu query cho báo cáo."}},
            {"name": "Redis",
             "detail": {"en": "Caching and session storage for high-traffic endpoints.",
                        "vi": "Cache và lưu session cho các endpoint tải cao."}},
            {"name": "Elasticsearch",
             "detail": {"en": "Log and event indexing for search and dashboards.",
                        "vi": "Đánh index log và sự kiện phục vụ tìm kiếm, dashboard."}},
        ],
    },
    {
        "group": {"en": "Data & AI", "vi": "Dữ liệu & AI"},
        "icon": "chart",
        "items": [
            {"name": "Data Analysis",
             "detail": {"en": "Cleaning, statistical summaries and turning raw logs into decisions.",
                        "vi": "Làm sạch dữ liệu, thống kê và biến log thô thành thông tin ra quyết định."}},
            {"name": "Pandas / NumPy",
             "detail": {"en": "Tabular transformation and batch processing.",
                        "vi": "Xử lý và biến đổi dữ liệu dạng bảng theo lô."}},
            {"name": "Machine Learning",
             "detail": {"en": "Supervised and unsupervised models, training and evaluation.",
                        "vi": "Mô hình có giám sát và không giám sát, huấn luyện và đánh giá."}},
            {"name": "NLP",
             "detail": {"en": "Vietnamese text classification, preprocessing and embeddings.",
                        "vi": "Phân loại văn bản tiếng Việt, tiền xử lý và embedding."}},
            {"name": "Data Visualization",
             "detail": {"en": "Dashboards and comparison charts that non-technical readers can use.",
                        "vi": "Dashboard và biểu đồ so sánh mà người không rành kỹ thuật vẫn đọc được."}},
        ],
    },
    {
        "group": {"en": "Web & Tooling", "vi": "Web & Công cụ"},
        "icon": "code",
        "items": [
            {"name": "HTML / CSS",
             "detail": {"en": "Responsive layouts, design tokens and accessible components.",
                        "vi": "Layout responsive, design token và component dễ tiếp cận."}},
            {"name": "JavaScript",
             "detail": {"en": "Vanilla DOM work, fetch-based UIs and small interactive widgets.",
                        "vi": "Thao tác DOM thuần, UI dùng fetch và các widget tương tác nhỏ."}},
            {"name": "Git / GitHub",
             "detail": {"en": "Branching, review workflow and CI-friendly repositories.",
                        "vi": "Quản lý nhánh, quy trình review và repo thân thiện với CI."}},
            {"name": "Docker",
             "detail": {"en": "Containerised services and reproducible local environments.",
                        "vi": "Đóng gói dịch vụ và dựng môi trường local tái lập được."}},
            {"name": "PM2",
             "detail": {"en": "Process management, clustering and log rotation for Node services.",
                        "vi": "Quản lý tiến trình, cluster và xoay log cho dịch vụ Node."}},
        ],
    },
]


# --------------------------------------------------------------------------
# 3. KINH NGHIEM
# --------------------------------------------------------------------------
EXPERIENCE = [
    {
        "company": "Zyxel Networks Việt Nam",
        "role": {"en": "System Integration Engineer", "vi": "Kỹ sư Tích hợp Hệ thống"},
        "time": {"en": "Jun 2026 - Present", "vi": "06/2026 - Nay"},
        "current": True,
        "location": {"en": "Ho Chi Minh City", "vi": "TP. Hồ Chí Minh"},
        "points": [
            {"en": "Integrate Zyxel access points, switches and firewalls with the Linux back-end services behind them, from client association through to the database.",
             "vi": "Tích hợp access point, switch, firewall Zyxel với các dịch vụ back-end trên Linux phía sau, từ lúc client kết nối tới tận cơ sở dữ liệu."},
            {"en": "Deploy and operate the Wi-Fi advertising stack (MongoDB, Redis, Elasticsearch, MySQL, FreeRADIUS, Nginx) on Ubuntu servers.",
             "vi": "Triển khai và vận hành stack quảng cáo Wi-Fi (MongoDB, Redis, Elasticsearch, MySQL, FreeRADIUS, Nginx) trên server Ubuntu."},
            {"en": "Built an internal tool that pushes CLI templates to hundreds of access points and switches over SSH, with mandatory dry-run and per-device logs.",
             "vi": "Xây công cụ nội bộ đẩy template lệnh CLI xuống hàng trăm access point và switch qua SSH, bắt buộc dry-run và ghi log từng thiết bị."},
            {"en": "Handle captive-portal and RADIUS authentication issues end to end, from client association to the SQL backend.",
             "vi": "Xử lý trọn vẹn sự cố captive portal và xác thực RADIUS, từ lúc client kết nối tới backend SQL."},
            {"en": "Built the Zyxel Helpdesk (GLPI) and the Shipment Calculator to replace the Excel files used for demo stock, RMA and shipments.",
             "vi": "Xây Zyxel Helpdesk (GLPI) và Shipment Calculator thay các file Excel theo dõi kho demo, RMA và tính shipment."},
            {"en": "Set up Bitrix24 workflows and integrations: real-time attendance sync, devices by serial, approvals and auto-generated CO/CQ.",
             "vi": "Dựng quy trình và tích hợp trên Bitrix24: đồng bộ chấm công tức thời, thiết bị theo serial, quy trình duyệt và tự sinh CO/CQ."},
            {"en": "Automate recurring reporting so weekly status decks are generated from task notes instead of assembled by hand.",
             "vi": "Tự động hoá báo cáo định kỳ: slide báo cáo tuần được sinh từ ghi chú công việc thay vì làm thủ công."},
        ],
        "tech": ["Ubuntu", "Python", "SSH", "FreeRADIUS", "MongoDB", "Nginx", "MySQL", "GLPI", "Docker", "Bitrix24"],
    },
    {
        "company": "NewAI",
        "role": {"en": "Data Analyst Intern", "vi": "Thực tập sinh Phân tích Dữ liệu"},
        "time": {"en": "Jul 2023 - Jan 2024", "vi": "07/2023 - 01/2024"},
        "current": False,
        "location": {"en": "Ho Chi Minh City", "vi": "TP. Hồ Chí Minh"},
        "points": [
            {"en": "Cleaned and analysed production datasets, then built the visualisation layer the team used for reviews.",
             "vi": "Làm sạch và phân tích dữ liệu thực tế, xây lớp trực quan hoá cho team dùng khi review."},
            {"en": "Wrote Python pipelines to replace manual spreadsheet steps in the reporting flow.",
             "vi": "Viết pipeline Python thay thế các bước thao tác Excel thủ công trong quy trình báo cáo."},
        ],
        "tech": ["Python", "Pandas", "SQL", "Matplotlib"],
    },
]


# --------------------------------------------------------------------------
# 4. HOC VAN
# --------------------------------------------------------------------------
EDUCATION = [
    {
        "school": {"en": "Ton Duc Thang University", "vi": "Trường Đại học Tôn Đức Thắng"},
        "degree": {"en": "B.Sc. Computer Science", "vi": "Cử nhân Khoa học Máy tính"},
        "time": "2019 - 2024",
        "note": {"en": "Focus on data processing, machine learning and web systems.",
                 "vi": "Tập trung vào xử lý dữ liệu, học máy và hệ thống web."},
    },
]


# --------------------------------------------------------------------------
# 4b. CONG CU TAI ZYXEL (lay tu slide "Digitalizing daily operations at Zyxel Vietnam", 11/2026)
#     Chi dua noi dung cong khai duoc: KHONG dua so lieu kho/RMA noi bo, IP, may chu,
#     tinh trang bao mat hay anh man hinh noi bo len day.
# --------------------------------------------------------------------------
ZYXEL_TOOLS = {
    "intro": {
        "en": "Many daily processes at the Vietnam office still ran on Excel files. "
              "These are the tools I built to replace them.",
        "vi": "Nhiều quy trình hằng ngày ở văn phòng Việt Nam vẫn chạy trên file Excel. "
              "Đây là những công cụ tôi xây để thay thế chúng.",
    },
    "cases": [
        {
            "name": "Zyxel Helpdesk",
            "kind": {"en": "Web · support, demo loans and RMA", "vi": "Web · hỗ trợ, mượn demo và RMA"},
            "summary": {
                "en": "One system for customers, engineers and the warehouse, replacing the Excel "
                      "trackers for demo stock and RMA units.",
                "vi": "Một hệ thống chung cho khách hàng, kỹ sư và kho, thay cho các file Excel "
                      "theo dõi kho demo và thiết bị RMA.",
            },
            "image": "/static/img/work/helpdesk-portal.webp",
            "image_w": 1280, "image_h": 915,
            "image_alt": {"en": "Zyxel Helpdesk public portal", "vi": "Cổng hỗ trợ công khai của Zyxel Helpdesk"},
            "link": "https://support.zyxel.net.vn",
            "link_label": "support.zyxel.net.vn",
            "points": [
                {"en": "Customers send support, demo-loan or RMA requests without logging in, then follow "
                       "them with a tracking code.",
                 "vi": "Khách hàng gửi yêu cầu hỗ trợ, mượn demo hoặc bảo hành mà không cần đăng nhập, "
                       "rồi theo dõi bằng mã tracking."},
                {"en": "Staff work tickets with SLA (support 4 h, RMA 1 day), one record per serial, "
                       "a loan workflow and a read-only status log.",
                 "vi": "Nhân viên xử lý ticket có SLA (hỗ trợ 4 giờ, RMA 1 ngày), quản lý theo serial, "
                       "cho mượn và nhật ký trạng thái không sửa được."},
                {"en": "RMA units are tracked step by step to and from HQ; any list exports to PDF or "
                       "Excel in the Zyxel template.",
                 "vi": "Thiết bị RMA được theo dõi từng bước đi và về từ HQ; mọi danh sách xuất PDF, "
                       "Excel theo mẫu Zyxel."},
                {"en": "Built on GLPI 12 with no core changes: all customisation lives in 3 custom plugins, "
                       "behind an Nginx gateway, with MySQL in Docker.",
                 "vi": "Nền GLPI 12, không sửa lõi: toàn bộ tuỳ biến nằm trong 3 plugin tự viết, "
                       "chạy sau Nginx, MySQL trong Docker."},
            ],
            "metrics": [
                {"value": "3", "label": {"en": "custom plugins", "vi": "plugin tự viết"}},
                {"value": "~7.8k", "label": {"en": "lines of code", "vi": "dòng code"}},
                {"value": "36", "label": {"en": "FAQ articles in Vietnamese", "vi": "bài FAQ tiếng Việt"}},
                {"value": {"en": "~2 wks", "vi": "~2 tuần"}, "label": {"en": "to build", "vi": "để xây dựng"}},
            ],
            "status": {"en": "Stock and RMA data live · ticketing in pilot",
                       "vi": "Dữ liệu kho, RMA đang dùng thật · ticket đang thử nghiệm"},
            "tech": ["GLPI 12", "PHP plugins", "Nginx", "MySQL 8.4", "Docker"],
        },
        {
            "name": "Zyxel Shipment Calculator",
            "kind": {"en": "Windows app + web", "vi": "Ứng dụng Windows + bản web"},
            "summary": {
                "en": "Weight and volume for multi-list shipments, replacing the \"TÍNH SHIPMENT\" "
                      "Excel sheet. Type or paste a list and the totals are ready.",
                "vi": "Tính khối lượng và thể tích cho lô hàng nhiều list, thay sheet Excel "
                      "\"TÍNH SHIPMENT\". Gõ hoặc dán danh sách là có kết quả ngay.",
            },
            "image": "/static/img/work/shipment-calculator.webp",
            "image_w": 1400, "image_h": 840,
            "image_alt": {"en": "Shipment Calculator result screen", "vi": "Màn hình kết quả của Shipment Calculator"},
            "link": "",
            "points": [
                {"en": "Type a model with suggestions or paste a whole order, instead of picking each SKU "
                       "from a ~636-item dropdown.",
                 "vi": "Gõ model có gợi ý hoặc dán cả đơn hàng, thay vì chọn từng SKU trong khoảng 636 mã."},
                {"en": "Add shipping lists freely; totals and the Excel export keep the same layout as the old sheet.",
                 "vi": "Thêm shipping list tuỳ ý; tổng và file Excel xuất ra giữ đúng mẫu cũ."},
                {"en": "Known unit errors in the source data (600 kg instead of 0.6 kg) are fixed automatically.",
                 "vi": "Tự sửa lỗi đơn vị trong DATA nguồn (600 kg thay vì 0,6 kg)."},
                {"en": "SKUs with missing data are flagged red and kept out of the totals instead of being miscounted.",
                 "vi": "Mã thiếu dữ liệu được báo đỏ và không cộng vào tổng, thay vì bị cộng nhầm."},
            ],
            "metrics": [
                {"value": "636", "label": {"en": "SKUs · 288 models", "vi": "SKU · 288 model"}},
                {"value": "11/11", "label": {"en": "automated tests pass", "vi": "test tự động đạt"}},
                {"value": "3", "label": {"en": "data errors auto-fixed", "vi": "lỗi DATA tự sửa"}},
                {"value": {"en": "1 step", "vi": "1 bước"}, "label": {"en": "install · offline", "vi": "cài đặt · chạy offline"}},
            ],
            "status": {"en": "v2.0.0 delivered to first users", "vi": "Bản 2.0.0 đã đến tay người dùng đầu tiên"},
            "tech": ["Windows", "Web", "Excel export", "Automated tests"],
        },
    ],
    # Viec tren Bitrix24 (CRM va mang noi bo cua cong ty)
    "bitrix": {
        "name": "Bitrix24",
        "kind": {"en": "CRM · workflows and integrations", "vi": "CRM · quy trình và tích hợp"},
        "summary": {
            "en": "Workflows, integrations and user guides on the company's CRM and intranet.",
            "vi": "Quy trình, tích hợp và tài liệu hướng dẫn trên CRM và mạng nội bộ của công ty.",
        },
        "items": [
            {"title": {"en": "Attendance sync", "vi": "Đồng bộ chấm công"},
             "text": {"en": "ZKTeco device → Cloudflare free tier → Bitrix24, one row per person per day. "
                            "Live since 01/07/2026, no office PC running 24/7.",
                      "vi": "Máy ZKTeco → Cloudflare (gói miễn phí) → Bitrix24, mỗi người mỗi ngày một dòng. "
                            "Chạy từ 01/07/2026, bỏ hẳn máy tính bật 24/7."}},
            {"title": {"en": "Devices by serial", "vi": "Thiết bị theo serial"},
             "text": {"en": "Devices and warranty in Smart Processes with 8 automation rules.",
                      "vi": "Thiết bị và bảo hành bằng Smart Process, 8 quy tắc tự động."}},
            {"title": {"en": "Approval workflows", "vi": "Quy trình duyệt"},
             "text": {"en": "Demo loans, warranty swaps and contracts.",
                      "vi": "Mượn demo, đổi bảo hành và hợp đồng."}},
            {"title": {"en": "Auto documents", "vi": "Tự sinh văn bản"},
             "text": {"en": "CO/CQ certificates generated from Zyxel templates.",
                      "vi": "CO/CQ sinh tự động theo mẫu Zyxel."}},
            {"title": {"en": "Project P&L", "vi": "Lãi lỗ dự án"},
             "text": {"en": "Profit and loss per project on Bitrix24 instead of Excel.",
                      "vi": "Lãi lỗ từng dự án trên Bitrix24 thay file Excel."}},
            {"title": {"en": "Sell-out import", "vi": "Nhập Sell-out"},
             "text": {"en": "Excel helper links serials, tax codes and sales, then builds a ready-to-import CSV.",
                      "vi": "File Excel công cụ tự nối serial, mã số thuế, sale và tạo sẵn CSV để import."}},
        ],
        "note": {"en": "Plus 5 step-by-step user guides with 90 annotated screenshots.",
                 "vi": "Kèm 5 tài liệu hướng dẫn từng bước, 90 ảnh minh hoạ."},
        "tech": ["Bitrix24", "Smart Processes", "Cloudflare", "ZKTeco"],
    },
    # Ke hoach tiep theo
    "next": {
        "label": {"en": "Next", "vi": "Tiếp theo"},
        "title": {"en": "On-premise monitoring with LibreNMS",
                  "vi": "Giám sát thiết bị Zyxel on-premise bằng LibreNMS"},
        "text": {"en": "One self-hosted dashboard for the health of our Zyxel devices: SNMP auto-discovery, "
                       "status and traffic graphs, alerts when a device goes down. No licence cost.",
                 "vi": "Một màn hình tự host theo dõi tình trạng các thiết bị Zyxel: tự tìm thiết bị qua SNMP, "
                       "biểu đồ trạng thái và băng thông, cảnh báo khi thiết bị mất kết nối. Không tốn bản quyền."},
        "status": {"en": "Planning", "vi": "Đang lên kế hoạch"},
    },
}


# --------------------------------------------------------------------------
# 5. DU AN
# --------------------------------------------------------------------------
PROJECTS = [
    {
        "name": {"en": "Bulk SSH Config Tool", "vi": "Công cụ cấu hình SSH hàng loạt"},
        "kind": {"en": "Internal tool", "vi": "Công cụ nội bộ"},
        "desc": {
            "en": "Web interface that runs a CLI command template against a CSV list of network devices. "
                  "Dry-run is mandatory before anything is applied, dangerous commands are blocked, "
                  "devices run in parallel and every session is saved as a transcript.",
            "vi": "Giao diện web chạy template lệnh CLI lên danh sách thiết bị mạng trong file CSV. "
                  "Bắt buộc dry-run trước khi áp dụng, chặn lệnh nguy hiểm, chạy song song nhiều thiết bị "
                  "và lưu transcript cho từng phiên.",
        },
        "tech": ["Python", "Paramiko", "FastAPI", "CSV"],
        "link": "",
        "featured": True,
    },
    {
        "name": {"en": "Wi-Fi Ads Platform Deployment", "vi": "Triển khai nền tảng Wi-Fi Ads"},
        "kind": {"en": "Infrastructure", "vi": "Hạ tầng"},
        "desc": {
            "en": "Scripted install of a full advertising and authentication stack onto a fresh Ubuntu server: "
                  "MongoDB, Redis, Elasticsearch, MySQL with FreeRADIUS, Nginx and PM2-managed Node services, "
                  "reproducible from a single command.",
            "vi": "Script cài trọn bộ stack quảng cáo và xác thực lên server Ubuntu mới: "
                  "MongoDB, Redis, Elasticsearch, MySQL kèm FreeRADIUS, Nginx và các service Node chạy bằng PM2, "
                  "dựng lại được chỉ bằng một lệnh.",
        },
        "tech": ["Ubuntu", "Bash", "FreeRADIUS", "MongoDB", "Nginx", "PM2"],
        "link": "",
        "featured": True,
    },
    {
        "name": {"en": "Hate Speech Detection", "vi": "Phát hiện phát ngôn thù ghét"},
        "kind": {"en": "Machine learning", "vi": "Học máy"},
        "desc": {
            "en": "NLP model that classifies Vietnamese social-media comments, covering preprocessing, "
                  "feature extraction and a comparison of several classifiers.",
            "vi": "Mô hình NLP phân loại bình luận mạng xã hội tiếng Việt, gồm tiền xử lý, "
                  "trích xuất đặc trưng và so sánh nhiều bộ phân loại.",
        },
        "tech": ["Python", "scikit-learn", "NLP"],
        "link": "",
        "featured": False,
    },
    {
        "name": {"en": "ML Model Comparison Dashboard", "vi": "Dashboard so sánh mô hình ML"},
        "kind": {"en": "Data visualization", "vi": "Trực quan hoá dữ liệu"},
        "desc": {
            "en": "Web app that trains several models on the same dataset and puts their metrics side by "
                  "side, so the trade-offs are visible instead of buried in a notebook.",
            "vi": "Web app huấn luyện nhiều mô hình trên cùng bộ dữ liệu và đặt các chỉ số cạnh nhau "
                  "để thấy rõ đánh đổi, thay vì phải lục trong notebook.",
        },
        "tech": ["Python", "Flask", "Chart.js"],
        "link": "",
        "featured": False,
    },
    {
        "name": {"en": "This Portfolio", "vi": "Trang portfolio này"},
        "kind": {"en": "Web", "vi": "Web"},
        "desc": {
            "en": "Bilingual single-page site rendered from Jinja2 templates to static HTML, with all content "
                  "driven from one Python file and deployed on Netlify.",
            "vi": "Trang đơn song ngữ dựng từ template Jinja2 ra HTML tĩnh, toàn bộ nội dung nằm trong một file "
                  "Python duy nhất, deploy trên Netlify.",
        },
        "tech": ["Python", "Jinja2", "CSS", "Netlify"],
        "link": "https://github.com/hieuky26/portfolio",
        "link_label": {"en": "Source on GitHub", "vi": "Mã nguồn trên GitHub"},
        "featured": False,
    },
]

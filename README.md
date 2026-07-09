# Clinic Patient Queue Management

Hệ thống quản lý hàng đợi khám bệnh cho phòng khám — gồm frontend Vue 3 và backend FastAPI.

## Cấu trúc dự án

```
backend/    FastAPI + SQLAlchemy + SQLite (mặc định)
frontend/   Vue 3 + Vite + Pinia + Bootstrap
database/   Tài liệu tham khảo schema
docs/       Tài liệu thiết kế (ERD, UseCase, API...)
```

## Chạy backend

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8080
```

Backend sẽ tự tạo database SQLite (`clinic.db`) và seed sẵn 1 tài khoản Admin:

- Email: `admin@gmail.com`
- Mật khẩu: `admin123`

Swagger UI: http://localhost:8080/docs

Cấu hình trong `backend/.env`:

```
DATABASE_URL=sqlite:///./clinic.db
SECRET_KEY=change-this-secret-key-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440
CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

> Muốn dùng PostgreSQL/MySQL: đổi `DATABASE_URL` (ví dụ `postgresql://user:pass@localhost/clinic`) và cài thêm driver tương ứng (`psycopg2-binary`, `pymysql`...).

## Chạy frontend

```bash
cd frontend
npm install
npm run dev
```

Cấu hình trong `frontend/.env`:

```
VITE_API_BASE_URL=http://localhost:8080/api
```

Mặc định chạy tại http://localhost:5173

## Chạy bằng Docker Compose

```bash
docker compose up --build
```

## Tính năng đã hoàn thành

- **Auth**: đăng ký, đăng nhập (JWT), đổi mật khẩu, đăng xuất, route guard bảo vệ khu vực Admin
- **Quản lý người dùng**: CRUD tài khoản (chỉ Admin)
- **Quản lý bác sĩ / bệnh nhân / lịch khám / hàng đợi khám bệnh**: CRUD đầy đủ, dữ liệu lấy trực tiếp từ API
- **Dashboard**: số liệu thống kê và bảng dữ liệu lấy từ API thật

## Chưa hoàn thành / hướng phát triển tiếp theo

- Hồ sơ bệnh án (`medical_records`) — mới có khung API, chưa có giao diện và service tương ứng
- Liên kết quan hệ (foreign key) giữa bác sĩ/bệnh nhân với lịch khám và hàng đợi (hiện lưu dạng chuỗi tên để khớp với giao diện hiện tại)
- Phân trang, lọc nâng cao cho các bảng dữ liệu

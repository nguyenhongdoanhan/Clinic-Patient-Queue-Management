# 🏥 Clinic Patient Queue Management System

## 📋 Yêu cầu Hệ thống

- Docker & Docker Compose
- Python 3.11+ (nếu chạy local)
- Node.js 16+ (cho Frontend)

## 🚀 Cách Chạy Hệ Thống

### Option 1: Chạy với Docker (Khuyến nghị)

```bash
# 1. Đứng ở thư mục root project
cd Clinic-Patient-Queue-Management-feature-frontend-auth-admin

# 2. Khởi động SQL Server + Backend
docker-compose up -d

# 3. Chờ khoảng 30 giây cho SQL Server khởi động

# 4. Khởi tạo database
docker-compose exec backend python init_db.py

# 5. Chạy Frontend (trong terminal mới)
cd frontend
npm install
npm run dev
```

### Option 2: Chạy Local (không dùng Docker)

#### Bước 1: Khởi động SQL Server

```bash
# Cài đặt SQL Server Express hoặc dùng Docker
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=MyPassword@123" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2022-latest
```

#### Bước 2: Khởi tạo Backend

```bash
cd backend

# Cài đặt dependencies
pip install -r requirements.txt

# Cài ODBC Driver 17 for SQL Server
# Windows: Tải từ https://www.microsoft.com/en-us/download/details.aspx?id=56567
# macOS: brew install msodbcsql17 mssql-tools
# Linux (Ubuntu): sudo apt-get install odbc-mssql

# Khởi tạo database
python init_db.py

# Chạy backend
python run.py
```

#### Bước 3: Chạy Frontend

```bash
cd frontend
npm install
npm run dev
```

## 📚 API Endpoints

### Authentication (Xác thực)
- `POST /api/auth/login` - Đăng nhập
  ```json
  {
    "email": "admin@clinic.com",
    "password": "admin123"
  }
  ```
  **Response:**
  ```json
  {
    "access_token": "eyJhbGc...",
    "token_type": "bearer",
    "user": {
      "id": 1,
      "username": "admin",
      "email": "admin@clinic.com",
      "role": "ADMIN"
    }
  }
  ```

- `POST /api/auth/register` - Đăng ký tài khoản mới
  ```json
  {
    "username": "doctor1",
    "email": "doctor@clinic.com",
    "password": "password123"
  }
  ```

- `GET /api/users/me` - Lấy thông tin người dùng hiện tại (yêu cầu token)

### Patients (Bệnh nhân)
- `GET /api/patients` - Lấy danh sách bệnh nhân
- `GET /api/patients/{id}` - Lấy thông tin bệnh nhân
- `POST /api/patients` - Thêm bệnh nhân mới
- `PUT /api/patients/{id}` - Cập nhật thông tin bệnh nhân
- `DELETE /api/patients/{id}` - Xóa bệnh nhân

### Doctors (Bác sĩ)
- `GET /api/doctor` - Lấy danh sách bác sĩ
- `GET /api/doctor/{id}` - Lấy thông tin bác sĩ
- `POST /api/doctor` - Thêm bác sĩ mới
- `PUT /api/doctor/{id}` - Cập nhật thông tin bác sĩ
- `DELETE /api/doctor/{id}` - Xóa bác sĩ

### Appointments (Lịch hẹn)
- `GET /api/appointments` - Lấy danh sách lịch hẹn
- `GET /api/appointments/{id}` - Lấy thông tin lịch hẹn
- `POST /api/appointments` - Tạo lịch hẹn mới
- `PUT /api/appointments/{id}` - Cập nhật lịch hẹn
- `DELETE /api/appointments/{id}` - Xóa lịch hẹn

### Queues (Hàng chờ)
- `GET /api/queues` - Lấy danh sách hàng chờ
- `GET /api/queues/{id}` - Lấy thông tin hàng chờ
- `POST /api/queues` - Tạo hàng chờ mới
- `PUT /api/queues/{id}` - Cập nhật hàng chờ
- `DELETE /api/queues/{id}` - Xóa hàng chờ

### Medical Records (Hồ sơ y tế)
- `GET /api/medical_records` - Lấy danh sách hồ sơ
- `GET /api/medical_records/{id}` - Lấy thông tin hồ sơ
- `POST /api/medical_records` - Tạo hồ sơ mới
- `PUT /api/medical_records/{id}` - Cập nhật hồ sơ
- `DELETE /api/medical_records/{id}` - Xóa hồ sơ

## 🔐 Thông tin Đăng nhập Mặc định

```
Email: admin@clinic.com
Password: admin123
```

⚠️ **Lưu ý:** Tài khoản admin được tạo tự động khi backend khởi động.

## 📁 Cấu trúc Thư mục

```
.
├── backend/          # FastAPI Backend
│   ├── app/
│   │   ├── api/      # API Routes
│   │   ├── models/   # SQLAlchemy Models
│   │   ├── schemas/  # Pydantic Schemas
│   │   ├── core/     # Core configs
│   │   └── services/ # Business logic
│   ├── requirements.txt
│   └── run.py
│
├── frontend/         # Vue.js Frontend
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/  # API Services
│   │   ├── stores/    # Pinia stores
│   │   └── router/
│   └── package.json
│
└── docker-compose.yml
```

## � JWT Authentication

Sau khi đăng nhập thành công, token sẽ được lưu trong localStorage với key `access_token`.

**Để gửi request yêu cầu authentication:**
```
Authorization: Bearer {access_token}
```

Frontend tự động thêm token vào header cho tất cả các request API.

## �🛠️ Troubleshooting
```
Error: "Access denied for user 'sa'"
```
**Giải pháp**: Đảm bảo SQL Server đã khởi động, kiểm tra password trong .env

### ODBC Driver Not Found
```
Error: "Can't open lib 'ODBC Driver 17 for SQL Server'"
```
**Giải pháp**: Cài đặt ODBC Driver 17 for SQL Server từ Microsoft

### Port 1433 đã được sử dụng
```
docker-compose: Cannot start service mssql
```
**Giải pháp**: Thay đổi port trong docker-compose.yml: `"1434:1433"`

## 📞 Hỗ trợ

Nếu gặp vấn đề, vui lòng kiểm tra:
1. Docker services đang chạy
2. Database connection trong .env
3. Port không bị conflict

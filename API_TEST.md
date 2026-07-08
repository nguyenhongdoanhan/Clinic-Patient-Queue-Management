# 🧪 API Testing Guide

## Login Flow (Quy trình Đăng nhập)

### 1. Đăng nhập
```bash
curl -X POST http://localhost:8080/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@clinic.com",
    "password": "admin123"
  }'
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "username": "admin",
    "email": "admin@clinic.com",
    "role": "ADMIN"
  }
}
```

### 2. Lấy thông tin người dùng hiện tại (yêu cầu token)
```bash
curl -X GET http://localhost:8080/api/users/me \
  -H "Authorization: Bearer {access_token}"
```

## Patients API

### Lấy danh sách bệnh nhân
```bash
curl -X GET http://localhost:8080/api/patients \
  -H "Authorization: Bearer {access_token}"
```

### Thêm bệnh nhân mới
```bash
curl -X POST http://localhost:8080/api/patients \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {access_token}" \
  -d '{
    "full_name": "Nguyễn Văn A",
    "gender": "Nam",
    "birthday": "1990-01-01",
    "phone": "0123456789",
    "address": "Hà Nội"
  }'
```

### Cập nhật bệnh nhân
```bash
curl -X PUT http://localhost:8080/api/patients/1 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {access_token}" \
  -d '{
    "full_name": "Nguyễn Văn B",
    "gender": "Nam",
    "birthday": "1990-01-01",
    "phone": "0123456789",
    "address": "Hà Nội"
  }'
```

### Xóa bệnh nhân
```bash
curl -X DELETE http://localhost:8080/api/patients/1 \
  -H "Authorization: Bearer {access_token}"
```

## Doctors API

### Lấy danh sách bác sĩ
```bash
curl -X GET http://localhost:8080/api/doctor \
  -H "Authorization: Bearer {access_token}"
```

### Thêm bác sĩ mới
```bash
curl -X POST http://localhost:8080/api/doctor \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {access_token}" \
  -d '{
    "full_name": "Bác sĩ Trần X",
    "specialty": "Tim mạch",
    "phone": "0987654321",
    "email": "doctor@clinic.com"
  }'
```

## Appointments API

### Lấy danh sách lịch hẹn
```bash
curl -X GET http://localhost:8080/api/appointments \
  -H "Authorization: Bearer {access_token}"
```

### Tạo lịch hẹn mới
```bash
curl -X POST http://localhost:8080/api/appointments \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {access_token}" \
  -d '{
    "patient_id": 1,
    "doctor_id": 1,
    "appointment_date": "2024-12-25",
    "appointment_time": "10:30:00"
  }'
```

## Testing với Postman

1. **Environment Variable:** Lưu `access_token` vào environment variable
   ```
   {{access_token}}
   ```

2. **Pre-request Script:** Tự động refresh token nếu hết hạn
   ```javascript
   if (pm.environment.get("access_token_expires") < new Date().getTime()) {
       // Gửi request login để lấy token mới
   }
   ```

3. **Authorization Header:** Sử dụng
   ```
   Authorization: Bearer {{access_token}}
   ```

## Frontend Login Test

1. Mở http://localhost:5173
2. Nhập email: `admin@clinic.com`
3. Nhập password: `admin123`
4. Nhấn "Đăng nhập"
5. Kiểm tra localStorage trong DevTools → Application → localStorage
   - `access_token`: JWT token
   - `user`: JSON user object

## JWT Token Structure

JWT token gồm 3 phần: `header.payload.signature`

**Payload bao gồm:**
- `sub`: User ID
- `id`: User ID (thêm cho compatibility)
- `email`: Email người dùng
- `role`: Vai trò (ADMIN, USER, DOCTOR)
- `exp`: Expiration time (1440 minutes = 24 hours)

**Decode token online:** https://jwt.io

## Common Errors

| Error | Giải pháp |
|-------|----------|
| "Could not validate credentials" | Token không hợp lệ hoặc hết hạn, đăng nhập lại |
| "Access denied for user" | Email/password sai hoặc không được phép truy cập |
| "Email already exists" | Email đã tồn tại, sử dụng email khác |
| 401 Unauthorized | Token missing hoặc không được include trong Authorization header |
| 403 Forbidden | User không có quyền truy cập endpoint này |

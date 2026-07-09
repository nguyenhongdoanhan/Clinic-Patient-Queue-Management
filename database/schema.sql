-- Schema tham khảo (SQLAlchemy tự tạo bảng tương đương khi backend khởi động).
-- Cú pháp dưới đây tương thích PostgreSQL/MySQL, chỉnh lại AUTOINCREMENT/SERIAL tuỳ hệ quản trị.

CREATE TABLE users (
    id            SERIAL PRIMARY KEY,
    name          VARCHAR(150) NOT NULL,
    email         VARCHAR(150) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role          VARCHAR(30)  NOT NULL DEFAULT 'Bệnh nhân', -- Admin | Bác sĩ | Lễ tân | Bệnh nhân
    status        VARCHAR(30)  NOT NULL DEFAULT 'Hoạt động', -- Hoạt động | Khóa
    phone         VARCHAR(30),
    address       VARCHAR(255)
);

CREATE TABLE doctors (
    id        SERIAL PRIMARY KEY,
    name      VARCHAR(150) NOT NULL,
    specialty VARCHAR(150) NOT NULL,
    phone     VARCHAR(30)  NOT NULL,
    email     VARCHAR(150) NOT NULL,
    status    VARCHAR(30)  NOT NULL DEFAULT 'Đang làm việc' -- Đang làm việc | Nghỉ
);

CREATE TABLE patients (
    id       SERIAL PRIMARY KEY,
    name     VARCHAR(150) NOT NULL,
    gender   VARCHAR(10)  NOT NULL DEFAULT 'Nam', -- Nam | Nữ
    birthday VARCHAR(20),
    phone    VARCHAR(30)  NOT NULL,
    address  VARCHAR(255)
);

CREATE TABLE appointments (
    id      SERIAL PRIMARY KEY,
    patient VARCHAR(150) NOT NULL,
    doctor  VARCHAR(150) NOT NULL,
    date    VARCHAR(20)  NOT NULL,
    time    VARCHAR(10)  NOT NULL,
    status  VARCHAR(30)  NOT NULL DEFAULT 'Đã đặt' -- Đã đặt | Đã khám | Đã hủy
);

CREATE TABLE queues (
    id      SERIAL PRIMARY KEY,
    number  VARCHAR(20)  NOT NULL,
    patient VARCHAR(150) NOT NULL,
    doctor  VARCHAR(150) NOT NULL,
    room    VARCHAR(30)  NOT NULL,
    status  VARCHAR(30)  NOT NULL DEFAULT 'Đang chờ' -- Đang chờ | Đang khám | Đã hoàn thành
);

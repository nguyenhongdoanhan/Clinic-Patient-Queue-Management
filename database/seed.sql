-- Dữ liệu mẫu tham khảo (backend tự seed tài khoản Admin khi khởi động lần đầu).

INSERT INTO users (name, email, password_hash, role, status)
VALUES ('Quản trị viên', 'admin@gmail.com', '<bcrypt-hash-của-admin123>', 'Admin', 'Hoạt động');

INSERT INTO doctors (name, specialty, phone, email, status) VALUES
('Nguyễn Văn A', 'Tim mạch', '0912345678', 'a@gmail.com', 'Đang làm việc'),
('Trần Thị B', 'Da liễu', '0988888888', 'b@gmail.com', 'Đang làm việc');

INSERT INTO patients (name, gender, birthday, phone, address) VALUES
('Nguyễn Văn A', 'Nam', '2000-10-12', '0912345678', 'Hà Nội'),
('Trần Thị B', 'Nữ', '1999-08-20', '0988888888', 'Đà Nẵng');

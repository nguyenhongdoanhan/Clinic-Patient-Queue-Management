import api from "./api";

const authService = {

    // Đăng nhập
    login(data) {
        return api.post("/auth/login", data);
    },

    // Đăng ký
    register(data) {
        return api.post("/auth/register", data);
    },

    // Lấy thông tin người dùng
    getProfile() {
        return api.get("/auth/profile");
    },

    // Đổi mật khẩu
    changePassword(data) {
        return api.put("/auth/change-password", data);
    },

    // Đăng xuất (nếu backend có API)
    logout() {
        return api.post("/auth/logout");
    }

};

export default authService;
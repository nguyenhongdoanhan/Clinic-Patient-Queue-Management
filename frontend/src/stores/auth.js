import { defineStore } from "pinia";
import { ref, computed } from "vue";
import authService from "../services/authService";

export const useAuthStore = defineStore("auth", () => {
    // Khởi tạo lại phiên đăng nhập từ localStorage (nếu có) khi tải lại trang
    const token = ref(localStorage.getItem("token") || null);
    const user = ref(safeParse(localStorage.getItem("user")));

    const loading = ref(false);
    const error = ref(null);

    const isAuthenticated = computed(() => !!token.value);
    const isAdmin = computed(() => user.value?.role === "admin");

    function safeParse(raw) {
        try {
            return raw ? JSON.parse(raw) : null;
        } catch {
            return null;
        }
    }

    function setSession({ access_token, token: altToken, user: userData } = {}) {
        token.value = access_token || altToken || null;
        user.value = userData || null;

        if (token.value) {
            localStorage.setItem("token", token.value);
        }
        if (user.value) {
            localStorage.setItem("user", JSON.stringify(user.value));
        }
    }

    function clearSession() {
        token.value = null;
        user.value = null;
        localStorage.removeItem("token");
        localStorage.removeItem("user");
    }

    async function login(credentials) {
        loading.value = true;
        error.value = null;

        try {
            const res = await authService.login(credentials);
            setSession(res.data);
            return res.data;
        } catch (err) {
            error.value =
                err.response?.data?.detail ||
                "Đăng nhập thất bại. Vui lòng kiểm tra lại email/mật khẩu.";
            throw err;
        } finally {
            loading.value = false;
        }
    }

    async function register(payload) {
        loading.value = true;
        error.value = null;

        try {
            const res = await authService.register(payload);
            return res.data;
        } catch (err) {
            error.value =
                err.response?.data?.detail ||
                "Đăng ký thất bại. Vui lòng kiểm tra lại thông tin.";
            throw err;
        } finally {
            loading.value = false;
        }
    }

    async function fetchProfile() {
        try {
            const res = await authService.getProfile();
            user.value = res.data;
            localStorage.setItem("user", JSON.stringify(user.value));
            return res.data;
        } catch (err) {
            clearSession();
            throw err;
        }
    }

    function logout() {
        // Gọi API logout nếu backend có hỗ trợ, nhưng vẫn xoá phiên cục bộ dù API lỗi
        authService.logout().catch(() => {});
        clearSession();
    }

    return {
        token,
        user,
        loading,
        error,
        isAuthenticated,
        isAdmin,
        login,
        register,
        fetchProfile,
        logout,
        clearSession
    };
});

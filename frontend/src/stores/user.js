import { defineStore } from "pinia";
import { ref } from "vue";
import userService from "../services/userService";

// Store quản lý danh sách tài khoản người dùng (trang Quản lý người dùng - Admin).
// Khác với stores/auth.js: store đó quản lý phiên đăng nhập của người dùng hiện tại.
export const useUserStore = defineStore("user", () => {
    const users = ref([]);
    const loading = ref(false);
    const error = ref(null);

    async function fetchUsers(params) {
        loading.value = true;
        error.value = null;
        try {
            const res = await userService.getAll(params);
            users.value = res.data;
        } catch (err) {
            error.value = "Không thể tải danh sách người dùng. Vui lòng kiểm tra kết nối máy chủ.";
            throw err;
        } finally {
            loading.value = false;
        }
    }

    async function saveUser(user) {
        error.value = null;
        try {
            if (user.id) {
                const res = await userService.update(user.id, user);
                const index = users.value.findIndex((item) => item.id === user.id);
                if (index !== -1) users.value[index] = res.data;
                return res.data;
            } else {
                const res = await userService.create(user);
                users.value.push(res.data);
                return res.data;
            }
        } catch (err) {
            error.value = "Không thể lưu thông tin người dùng. Vui lòng thử lại.";
            throw err;
        }
    }

    async function deleteUser(id) {
        error.value = null;
        try {
            await userService.remove(id);
            users.value = users.value.filter((item) => item.id !== id);
        } catch (err) {
            error.value = "Không thể xoá người dùng. Vui lòng thử lại.";
            throw err;
        }
    }

    return { users, loading, error, fetchUsers, saveUser, deleteUser };
});

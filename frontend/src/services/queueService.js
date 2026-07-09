import api from "./api";

const queueService = {

    // Lấy danh sách hàng đợi (có thể truyền query params để tìm kiếm/lọc)
    getAll(params) {
        return api.get("/queues", { params });
    },

    // Lấy chi tiết 1 hàng đợi
    getById(id) {
        return api.get(`/queues/${id}`);
    },

    // Tạo mới hàng đợi
    create(data) {
        return api.post("/queues", data);
    },

    // Cập nhật hàng đợi
    update(id, data) {
        return api.put(`/queues/${id}`, data);
    },

    // Cập nhật riêng trạng thái (Đang chờ / Đang khám / Đã hoàn thành)
    updateStatus(id, status) {
        return api.patch(`/queues/${id}/status`, { status });
    },

    // Xoá hàng đợi
    remove(id) {
        return api.delete(`/queues/${id}`);
    }

};

export default queueService;

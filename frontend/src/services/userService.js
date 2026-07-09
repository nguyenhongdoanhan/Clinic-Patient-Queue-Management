import api from "./api";

const userService = {
    getAll(params) {
        return api.get("/users", { params });
    },
    create(data) {
        return api.post("/users", data);
    },
    update(id, data) {
        return api.put(`/users/${id}`, data);
    },
    remove(id) {
        return api.delete(`/users/${id}`);
    }
};

export default userService;

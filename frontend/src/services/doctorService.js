import api from "./api";

const doctorService = {
    getAll(params) {
        return api.get("/doctors", { params });
    },
    create(data) {
        return api.post("/doctors", data);
    },
    update(id, data) {
        return api.put(`/doctors/${id}`, data);
    },
    remove(id) {
        return api.delete(`/doctors/${id}`);
    }
};

export default doctorService;

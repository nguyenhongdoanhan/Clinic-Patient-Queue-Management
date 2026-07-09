import api from "./api";

const appointmentService = {
    getAll(params) {
        return api.get("/appointments", { params });
    },
    create(data) {
        return api.post("/appointments", data);
    },
    update(id, data) {
        return api.put(`/appointments/${id}`, data);
    },
    remove(id) {
        return api.delete(`/appointments/${id}`);
    }
};

export default appointmentService;

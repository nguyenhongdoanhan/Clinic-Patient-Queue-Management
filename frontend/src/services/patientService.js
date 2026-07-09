import api from "./api";

const patientService = {
    getAll(params) {
        return api.get("/patients", { params });
    },
    create(data) {
        return api.post("/patients", data);
    },
    update(id, data) {
        return api.put(`/patients/${id}`, data);
    },
    remove(id) {
        return api.delete(`/patients/${id}`);
    }
};

export default patientService;

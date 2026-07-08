import api from "./api";

export const getAllDoctors = () => {
    return api.get("/doctor");
};

export const getDoctorById = (id) => {
    return api.get(`/doctor/${id}`);
};

export const createDoctor = (data) => {
    return api.post("/doctor", data);
};

export const updateDoctor = (id, data) => {
    return api.put(`/doctor/${id}`, data);
};

export const deleteDoctor = (id) => {
    return api.delete(`/doctor/${id}`);
};

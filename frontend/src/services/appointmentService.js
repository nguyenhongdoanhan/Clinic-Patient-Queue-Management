import api from "./api";

export const getAllAppointments = () => {
    return api.get("/appointments");
};

export const getAppointmentById = (id) => {
    return api.get(`/appointments/${id}`);
};

export const createAppointment = (data) => {
    return api.post("/appointments", data);
};

export const updateAppointment = (id, data) => {
    return api.put(`/appointments/${id}`, data);
};

export const deleteAppointment = (id) => {
    return api.delete(`/appointments/${id}`);
};

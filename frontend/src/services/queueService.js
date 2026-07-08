import api from "./api";

export const getAllQueues = () => {
    return api.get("/api/queues");
};

export const getQueueById = (id) => {
    return api.get(`/api/queues/${id}`);
};

export const createQueue = (data) => {
    return api.post("/api/queues", data);
};

export const updateQueue = (id, data) => {
    return api.put(`/api/queues/${id}`, data);
};

export const deleteQueue = (id) => {
    return api.delete(`/api/queues/${id}`);
};

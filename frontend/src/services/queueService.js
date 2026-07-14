import api from "./api";

export const getAllQueues = () => {
    return api.get("/queues");
};

export const getQueueById = (id) => {
    return api.get(`/queues/${id}`);
};

export const createQueue = (data) => {
    return api.post("/queues", data);
};

export const updateQueue = (id, data) => {
    return api.put(`/queues/${id}`, data);
};

export const deleteQueue = (id) => {
    return api.delete(`/queues/${id}`);
};

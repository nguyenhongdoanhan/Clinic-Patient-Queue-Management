import api from "./api";

export const getAppointments = () => {
  return api.get("/appointments");
};

export const getQueue = () => {
  return api.get("/queues");
};
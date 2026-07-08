import api from "./api";

export const getPatients = () => {
  return api.get("/patients");
};

export const addPatient = (data) => {
  return api.post("/patients", data);
};

export const updatePatient = (id, data) => {
  return api.put(`/patients/${id}`, data);
};

export const deletePatient = (id) => {
  return api.delete(`/patients/${id}`);
};
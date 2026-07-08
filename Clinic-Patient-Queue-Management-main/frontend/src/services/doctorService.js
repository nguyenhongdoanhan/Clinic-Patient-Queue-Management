import api from "./api";

export const getDoctors = () => {
  return api.get("/doctors");
};

export const saveDiagnosis = (data) => {
  return api.post("/diagnosis", data);
};

export const savePrescription = (data) => {
  return api.post("/prescriptions", data);
};
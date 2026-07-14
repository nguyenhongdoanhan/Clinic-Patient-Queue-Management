import api from "./api";

/**
 * Lấy danh sách tất cả bệnh nhân
 * GET /patients
 */
export const getPatients = () => {
  return api.get("/patients");
};

/**
 * Lấy thông tin một bệnh nhân theo ID
 * GET /patients/{id}
 */
export const getPatientById = (id) => {
  return api.get(`/patients/${id}`);
};

/**
 * Thêm bệnh nhân mới
 * POST /patients
 */
export const addPatient = (data) => {
  return api.post("/patients", data);
};

/**
 * Cập nhật thông tin bệnh nhân
 * PUT /patients/{id}
 */
export const updatePatient = (id, data) => {
  return api.put(`/patients/${id}`, data);
};

/**
 * Xóa bệnh nhân
 * DELETE /patients/{id}
 */
export const deletePatient = (id) => {
  return api.delete(`/patients/${id}`);
};
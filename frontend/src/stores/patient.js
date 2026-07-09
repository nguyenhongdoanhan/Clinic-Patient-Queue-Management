import { defineStore } from "pinia";
import { ref } from "vue";
import patientService from "../services/patientService";

export const usePatientStore = defineStore("patient", () => {
    const patients = ref([]);
    const loading = ref(false);
    const error = ref(null);

    async function fetchPatients(params) {
        loading.value = true;
        error.value = null;
        try {
            const res = await patientService.getAll(params);
            patients.value = res.data;
        } catch (err) {
            error.value = "Không thể tải danh sách bệnh nhân. Vui lòng kiểm tra kết nối máy chủ.";
            throw err;
        } finally {
            loading.value = false;
        }
    }

    async function savePatient(patient) {
        error.value = null;
        try {
            if (patient.id) {
                const res = await patientService.update(patient.id, patient);
                const index = patients.value.findIndex((item) => item.id === patient.id);
                if (index !== -1) patients.value[index] = res.data;
                return res.data;
            } else {
                const res = await patientService.create(patient);
                patients.value.push(res.data);
                return res.data;
            }
        } catch (err) {
            error.value = "Không thể lưu thông tin bệnh nhân. Vui lòng thử lại.";
            throw err;
        }
    }

    async function deletePatient(patient) {
        error.value = null;
        try {
            await patientService.remove(patient.id);
            patients.value = patients.value.filter((item) => item.id !== patient.id);
        } catch (err) {
            error.value = "Không thể xoá bệnh nhân. Vui lòng thử lại.";
            throw err;
        }
    }

    return { patients, loading, error, fetchPatients, savePatient, deletePatient };
});

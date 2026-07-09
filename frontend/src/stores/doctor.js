import { defineStore } from "pinia";
import { ref } from "vue";
import doctorService from "../services/doctorService";

export const useDoctorStore = defineStore("doctor", () => {
    const doctors = ref([]);
    const loading = ref(false);
    const error = ref(null);

    async function fetchDoctors(params) {
        loading.value = true;
        error.value = null;
        try {
            const res = await doctorService.getAll(params);
            doctors.value = res.data;
        } catch (err) {
            error.value = "Không thể tải danh sách bác sĩ. Vui lòng kiểm tra kết nối máy chủ.";
            throw err;
        } finally {
            loading.value = false;
        }
    }

    async function saveDoctor(doctor) {
        error.value = null;
        try {
            if (doctor.id) {
                const res = await doctorService.update(doctor.id, doctor);
                const index = doctors.value.findIndex((item) => item.id === doctor.id);
                if (index !== -1) doctors.value[index] = res.data;
                return res.data;
            } else {
                const res = await doctorService.create(doctor);
                doctors.value.push(res.data);
                return res.data;
            }
        } catch (err) {
            error.value = "Không thể lưu thông tin bác sĩ. Vui lòng thử lại.";
            throw err;
        }
    }

    async function deleteDoctor(doctor) {
        error.value = null;
        try {
            await doctorService.remove(doctor.id);
            doctors.value = doctors.value.filter((item) => item.id !== doctor.id);
        } catch (err) {
            error.value = "Không thể xoá bác sĩ. Vui lòng thử lại.";
            throw err;
        }
    }

    return { doctors, loading, error, fetchDoctors, saveDoctor, deleteDoctor };
});

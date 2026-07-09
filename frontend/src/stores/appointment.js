import { defineStore } from "pinia";
import { ref } from "vue";
import appointmentService from "../services/appointmentService";

export const useAppointmentStore = defineStore("appointment", () => {
    const appointments = ref([]);
    const loading = ref(false);
    const error = ref(null);

    async function fetchAppointments(params) {
        loading.value = true;
        error.value = null;
        try {
            const res = await appointmentService.getAll(params);
            appointments.value = res.data;
        } catch (err) {
            error.value = "Không thể tải danh sách lịch khám. Vui lòng kiểm tra kết nối máy chủ.";
            throw err;
        } finally {
            loading.value = false;
        }
    }

    async function saveAppointment(appointment) {
        error.value = null;
        try {
            if (appointment.id) {
                const res = await appointmentService.update(appointment.id, appointment);
                const index = appointments.value.findIndex((item) => item.id === appointment.id);
                if (index !== -1) appointments.value[index] = res.data;
                return res.data;
            } else {
                const res = await appointmentService.create(appointment);
                appointments.value.push(res.data);
                return res.data;
            }
        } catch (err) {
            error.value = "Không thể lưu lịch khám. Vui lòng thử lại.";
            throw err;
        }
    }

    async function deleteAppointment(appointment) {
        error.value = null;
        try {
            await appointmentService.remove(appointment.id);
            appointments.value = appointments.value.filter((item) => item.id !== appointment.id);
        } catch (err) {
            error.value = "Không thể xoá lịch khám. Vui lòng thử lại.";
            throw err;
        }
    }

    return { appointments, loading, error, fetchAppointments, saveAppointment, deleteAppointment };
});

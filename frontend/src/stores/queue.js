import { defineStore } from "pinia";
import { ref } from "vue";
import queueService from "../services/queueService";

export const useQueueStore = defineStore("queue", () => {
    const queues = ref([]);
    const loading = ref(false);
    const error = ref(null);

    async function fetchQueues(params) {
        loading.value = true;
        error.value = null;

        try {
            const res = await queueService.getAll(params);
            queues.value = res.data;
        } catch (err) {
            error.value =
                "Không thể tải danh sách hàng đợi. Vui lòng kiểm tra kết nối máy chủ.";
            throw err;
        } finally {
            loading.value = false;
        }
    }

    async function saveQueue(queue) {
        error.value = null;

        try {
            if (queue.id) {
                const res = await queueService.update(queue.id, queue);
                const index = queues.value.findIndex((item) => item.id === queue.id);
                if (index !== -1) {
                    queues.value[index] = res.data;
                }
                return res.data;
            } else {
                const res = await queueService.create(queue);
                queues.value.push(res.data);
                return res.data;
            }
        } catch (err) {
            error.value = "Không thể lưu hàng đợi. Vui lòng thử lại.";
            throw err;
        }
    }

    async function deleteQueue(queue) {
        error.value = null;

        try {
            await queueService.remove(queue.id);
            queues.value = queues.value.filter((item) => item.id !== queue.id);
        } catch (err) {
            error.value = "Không thể xoá hàng đợi. Vui lòng thử lại.";
            throw err;
        }
    }

    return { queues, loading, error, fetchQueues, saveQueue, deleteQueue };
});

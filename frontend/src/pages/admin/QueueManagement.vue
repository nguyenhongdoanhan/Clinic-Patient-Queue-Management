<template>

  <AdminSidebar />
  <AdminNavbar />

  <div class="content">

    <!-- Header -->

    <div class="d-flex justify-content-between align-items-center mb-4">

      <div>

        <h2 class="fw-bold text-primary">

          Quản lý hàng đợi

        </h2>

        <p class="text-secondary">

          Quản lý thứ tự khám bệnh

        </p>

      </div>

      <button
        class="btn btn-primary"
        @click="openAddQueue"
      >

        <i class="bi bi-plus-circle me-2"></i>

        Thêm hàng đợi

      </button>

    </div>

    <!-- Thông báo lỗi -->

    <div
      v-if="queueStore.error"
      class="alert alert-danger"
      role="alert"
    >
      {{ queueStore.error }}
    </div>

    <!-- Search -->

    <div class="card shadow-sm mb-4">

      <div class="card-body">

        <input

          class="form-control"

          placeholder="Tìm theo bệnh nhân hoặc bác sĩ..."

          v-model="search"

        >

      </div>

    </div>

    <!-- Đang tải -->

    <div v-if="queueStore.loading" class="text-center py-5">
      <div class="spinner-border text-primary"></div>
    </div>

    <!-- Table -->

    <div v-else class="card shadow-sm">

      <div class="card-body p-0">

        <table class="table table-hover mb-0">

          <thead class="table-primary">

            <tr>

              <th>STT</th>

              <th>Bệnh nhân</th>

              <th>Bác sĩ</th>

              <th>Phòng</th>

              <th>Trạng thái</th>

              <th class="text-center">

                Thao tác

              </th>

            </tr>

          </thead>

          <tbody>

            <tr

              v-for="queue in filteredQueues"

              :key="queue.id"

            >

              <td>

                {{ queue.number }}

              </td>

              <td>

                {{ queue.patient }}

              </td>

              <td>

                {{ queue.doctor }}

              </td>

              <td>

                {{ queue.room }}

              </td>

              <td>

                <span

                  class="badge"

                  :class="{

                    'bg-warning text-dark':queue.status==='Đang chờ',

                    'bg-primary':queue.status==='Đang khám',

                    'bg-success':queue.status==='Đã hoàn thành'

                  }"

                >

                  {{ queue.status }}

                </span>

              </td>

              <td class="text-center">

                <button

                  class="btn btn-warning btn-sm me-2"

                  @click="openEditQueue(queue)"

                >

                  <i class="bi bi-pencil"></i>

                </button>

                <button

                  class="btn btn-danger btn-sm"

                  @click="openDeleteQueue(queue)"

                >

                  <i class="bi bi-trash"></i>

                </button>

              </td>

            </tr>

          </tbody>

        </table>

      </div>

    </div>

    <!-- Popup -->

    <QueueForm

      v-if="showForm"

      :queue="selectedQueue"

      @save="saveQueue"

      @close="showForm=false"

    />

    <DeleteQueueModal

      v-if="showDelete"

      :queue="selectedQueue"

      @delete="deleteQueue"

      @close="showDelete=false"

    />

  </div>

</template>
<script setup>

import { ref, computed, onMounted } from "vue"

import AdminSidebar from "../../components/layout/AdminSidebar.vue"
import AdminNavbar from "../../components/layout/AdminNavbar.vue"

import QueueForm from "../../components/queue/QueueForm.vue"
import DeleteQueueModal from "../../components/queue/DeleteQueueModal.vue"

import { useQueueStore } from "../../stores/queue"

const queueStore = useQueueStore()

// =========================
// Tìm kiếm
// =========================

const search = ref("")

// =========================
// Tải danh sách hàng đợi từ API khi vào trang
// =========================

onMounted(() => {
    queueStore.fetchQueues().catch(() => {
        // Lỗi đã được lưu trong queueStore.error để hiển thị lên giao diện
    })
})

// =========================
// Popup
// =========================

const showForm = ref(false)

const showDelete = ref(false)

const selectedQueue = ref(null)

// =========================
// Lọc dữ liệu
// =========================

const filteredQueues = computed(() => {

    return queueStore.queues.filter(queue =>

        queue.patient?.toLowerCase().includes(search.value.toLowerCase())

        ||

        queue.doctor?.toLowerCase().includes(search.value.toLowerCase())

    )

})

// =========================
// Thêm
// =========================

function openAddQueue(){

    selectedQueue.value = null

    showForm.value = true

}

// =========================
// Sửa
// =========================

function openEditQueue(queue){

    selectedQueue.value = { ...queue }

    showForm.value = true

}

// =========================
// Xóa
// =========================

function openDeleteQueue(queue){

    selectedQueue.value = queue

    showDelete.value = true

}

// =========================
// Lưu (gọi API tạo mới / cập nhật)
// =========================

async function saveQueue(queue){

    try {
        await queueStore.saveQueue(queue)
    } catch (err) {
        // Lỗi đã được lưu trong queueStore.error để hiển thị lên giao diện
    }

}

// =========================
// Xóa (gọi API xoá)
// =========================

async function deleteQueue(queue){

    try {
        await queueStore.deleteQueue(queue)
    } catch (err) {
        // Lỗi đã được lưu trong queueStore.error để hiển thị lên giao diện
    }

}

</script>
<style scoped>

.content{

    margin-left:260px;

    margin-top:75px;

    padding:30px;

    background:#f4f6f9;

    min-height:100vh;

}

.card{

    border:none;

    border-radius:15px;

    overflow:hidden;

}

.card-body{

    padding:20px;

}

.card-body.p-0{

    padding:0 !important;

}

.table{

    margin:0;

}

.table th{

    vertical-align:middle;

    text-align:center;

    font-weight:600;

}

.table td{

    vertical-align:middle;

}

.table tbody tr{

    transition:.3s;

}

.table tbody tr:hover{

    background:#f8f9fa;

}

.badge{

    padding:8px 14px;

    font-size:13px;

    border-radius:20px;

}

.btn{

    border-radius:8px;

}

.btn-warning,

.btn-danger{

    width:38px;

    height:38px;

}

.form-control{

    border-radius:10px;

}

.form-control:focus{

    border-color:#0d6efd;

    box-shadow:none;

}

h2{

    margin-bottom:5px;

}

.text-secondary{

    margin-bottom:0;

}

@media(max-width:992px){

.content{

margin-left:0;

padding:20px;

}

.table{

font-size:14px;

}

}

</style>
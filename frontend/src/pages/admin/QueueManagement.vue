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

    <!-- Table -->

    <div class="card shadow-sm">

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

import { ref, computed } from "vue"

import AdminSidebar from "../../components/layout/AdminSidebar.vue"
import AdminNavbar from "../../components/layout/AdminNavbar.vue"

import QueueForm from "../../components/queue/QueueForm.vue"
import DeleteQueueModal from "../../components/queue/DeleteQueueModal.vue"

// =========================
// Tìm kiếm
// =========================

const search = ref("")

// =========================
// Danh sách hàng đợi
// =========================

const queues = ref([

    {
        id: 1,
        number: "Q001",
        patient: "Nguyễn Văn A",
        doctor: "BS Trần Văn Bình",
        room: "P101",
        status: "Đang chờ"
    },

    {
        id: 2,
        number: "Q002",
        patient: "Trần Thị B",
        doctor: "BS Nguyễn Văn Minh",
        room: "P102",
        status: "Đang khám"
    },

    {
        id: 3,
        number: "Q003",
        patient: "Lê Văn C",
        doctor: "BS Phạm Thị Lan",
        room: "P201",
        status: "Đã hoàn thành"
    }

])

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

    return queues.value.filter(queue =>

        queue.patient.toLowerCase().includes(search.value.toLowerCase())

        ||

        queue.doctor.toLowerCase().includes(search.value.toLowerCase())

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
// Lưu
// =========================

function saveQueue(queue){

    if(queue.id){

        const index = queues.value.findIndex(

            item => item.id === queue.id

        )

        if(index !== -1){

            queues.value[index] = { ...queue }

        }

    }else{

        queue.id = queues.value.length
            ? Math.max(...queues.value.map(item => item.id)) + 1
            : 1

        queue.number = "Q" + String(queue.id).padStart(3,"0")

        queues.value.push({ ...queue })

    }

}

// =========================
// Xóa
// =========================

function deleteQueue(queue){

    queues.value = queues.value.filter(

        item => item.id !== queue.id

    )

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
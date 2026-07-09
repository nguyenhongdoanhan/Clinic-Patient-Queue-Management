<template>

  <AdminSidebar />
  <AdminNavbar />

  <div class="content">

    <!-- Header -->

    <div class="d-flex justify-content-between align-items-center mb-4">

      <div>

        <h2 class="fw-bold text-primary">

          Quản lý lịch khám

        </h2>

        <p class="text-secondary">

          Quản lý lịch hẹn khám bệnh

        </p>

      </div>

      <button
        class="btn btn-primary"
        @click="openAddAppointment"
      >

        <i class="bi bi-plus-circle me-2"></i>

        Đặt lịch

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

              <th>ID</th>

              <th>Bệnh nhân</th>

              <th>Bác sĩ</th>

              <th>Ngày khám</th>

              <th>Giờ</th>

              <th>Trạng thái</th>

              <th class="text-center">

                Thao tác

              </th>

            </tr>

          </thead>

          <tbody>

            <tr
              v-for="appointment in filteredAppointments"
              :key="appointment.id"
            >

              <td>

                {{ appointment.id }}

              </td>

              <td>

                {{ appointment.patient }}

              </td>

              <td>

                {{ appointment.doctor }}

              </td>

              <td>

                {{ appointment.date }}

              </td>

              <td>

                {{ appointment.time }}

              </td>

              <td>

                <span

                  class="badge"

                  :class="{

                  'bg-success':appointment.status==='Đã đặt',

                  'bg-primary':appointment.status==='Đã khám',

                  'bg-danger':appointment.status==='Đã hủy'

                  }"

                >

                  {{ appointment.status }}

                </span>

              </td>

              <td class="text-center">

                <button

                  class="btn btn-warning btn-sm me-2"

                  @click="openEditAppointment(appointment)"

                >

                  <i class="bi bi-pencil"></i>

                </button>

                <button

                  class="btn btn-danger btn-sm"

                  @click="openDeleteAppointment(appointment)"

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

    <AppointmentForm

      v-if="showForm"

      :appointment="selectedAppointment"

      @save="saveAppointment"

      @close="showForm=false"

    />

    <DeleteAppointmentModal

      v-if="showDelete"

      :appointment="selectedAppointment"

      @delete="deleteAppointment"

      @close="showDelete=false"

    />

  </div>

</template>
<script setup>

import { ref, computed } from "vue"

import AdminSidebar from "../../components/layout/AdminSidebar.vue"
import AdminNavbar from "../../components/layout/AdminNavbar.vue"

import AppointmentForm from "../../components/appointment/AppointmentForm.vue"
import DeleteAppointmentModal from "../../components/appointment/DeleteAppointmentModal.vue"

// =========================
// Tìm kiếm
// =========================

const search = ref("")

// =========================
// Danh sách lịch khám
// =========================

const appointments = ref([
//template
  {
    id: 1,
    patient: "Nguyễn Văn A",
    doctor: "BS Trần Văn Bình",
    date: "2026-07-10",
    time: "08:00",
    status: "Đã đặt"
  },

  {
    id: 2,
    patient: "Trần Thị B",
    doctor: "BS Nguyễn Văn Minh",
    date: "2026-07-10",
    time: "09:00",
    status: "Đã khám"
  },

  {
    id: 3,
    patient: "Lê Văn C",
    doctor: "BS Phạm Thị Lan",
    date: "2026-07-11",
    time: "14:00",
    status: "Đã hủy"
  }

])

// =========================
// Popup
// =========================

const showForm = ref(false)

const showDelete = ref(false)

const selectedAppointment = ref(null)

// =========================
// Lọc dữ liệu
// =========================

const filteredAppointments = computed(() => {

  return appointments.value.filter(item =>

    item.patient.toLowerCase().includes(search.value.toLowerCase())

    ||

    item.doctor.toLowerCase().includes(search.value.toLowerCase())

  )

})

// =========================
// Thêm
// =========================

const openAddAppointment = () => {

  selectedAppointment.value = null

  showForm.value = true

}

// =========================
// Sửa
// =========================

const openEditAppointment = (appointment) => {

  selectedAppointment.value = { ...appointment }

  showForm.value = true

}

// =========================
// Xóa
// =========================

const openDeleteAppointment = (appointment) => {

  selectedAppointment.value = appointment

  showDelete.value = true

}

// =========================
// Lưu
// =========================

const saveAppointment = (appointment) => {

  if (appointment.id) {

    const index = appointments.value.findIndex(

      item => item.id === appointment.id

    )

    if (index !== -1) {

      appointments.value[index] = { ...appointment }

    }

  } else {

    appointment.id = appointments.value.length

      ? Math.max(...appointments.value.map(i => i.id)) + 1

      : 1

    appointments.value.push({ ...appointment })

  }

}

// =========================
// Xóa
// =========================

const deleteAppointment = (appointment) => {

  appointments.value = appointments.value.filter(

    item => item.id !== appointment.id

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

    text-align:center;

    vertical-align:middle;

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

    padding:8px 12px;

    font-size:13px;

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

}

</style>
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

    <!-- Thông báo lỗi -->

    <div v-if="appointmentStore.error" class="alert alert-danger" role="alert">
      {{ appointmentStore.error }}
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

    <div v-if="appointmentStore.loading" class="text-center py-5">
      <div class="spinner-border text-primary"></div>
    </div>

    <!-- Table -->

    <div v-else class="card shadow-sm">

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

import { ref, computed, onMounted } from "vue"

import AdminSidebar from "../../components/layout/AdminSidebar.vue"
import AdminNavbar from "../../components/layout/AdminNavbar.vue"

import AppointmentForm from "../../components/appointment/AppointmentForm.vue"
import DeleteAppointmentModal from "../../components/appointment/DeleteAppointmentModal.vue"

import { useAppointmentStore } from "../../stores/appointment"

const appointmentStore = useAppointmentStore()

// =========================
// Tìm kiếm
// =========================

const search = ref("")

onMounted(() => {
  appointmentStore.fetchAppointments().catch(() => {})
})

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

  return appointmentStore.appointments.filter(item =>

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
// Lưu (gọi API thật)
// =========================

const saveAppointment = async (appointment) => {

  try {
    await appointmentStore.saveAppointment(appointment)
  } catch (err) {
    // Lỗi đã được lưu trong appointmentStore.error
  }

}

// =========================
// Xóa (gọi API thật)
// =========================

const deleteAppointment = async (appointment) => {

  try {
    await appointmentStore.deleteAppointment(appointment)
  } catch (err) {
    // Lỗi đã được lưu trong appointmentStore.error
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
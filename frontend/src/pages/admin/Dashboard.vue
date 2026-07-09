<template>

  <!-- Sidebar -->
  <AdminSidebar />

  <!-- Navbar -->
  <AdminNavbar />

  <!-- Nội dung -->
  <div class="content">

    <!-- Tiêu đề -->
    <div class="mb-4">

      <h2 class="fw-bold">
        Dashboard
      </h2>

      <p class="text-secondary">
        Chào mừng bạn đến với Hệ thống Quản lý Bệnh viện.
      </p>

    </div>

    <!-- Thống kê -->
    <div class="row">

      <div class="col-lg-3 col-md-6 mb-4">

        <StatCard
          title="Bác sĩ"
          :value="doctorStore.doctors.length"
          icon="bi bi-person-badge-fill"
          color="#0d6efd"
        />

      </div>

      <div class="col-lg-3 col-md-6 mb-4">

        <StatCard
          title="Bệnh nhân"
          :value="patientStore.patients.length"
          icon="bi bi-people-fill"
          color="#198754"
        />

      </div>

      <div class="col-lg-3 col-md-6 mb-4">

        <StatCard
          title="Lịch khám"
          :value="appointmentStore.appointments.length"
          icon="bi bi-calendar-check-fill"
          color="#ffc107"
        />

      </div>

      <div class="col-lg-3 col-md-6 mb-4">

        <StatCard
          title="Đang chờ"
          :value="queueStore.queues.filter(q => q.status === 'Đang chờ').length"
          icon="bi bi-clock-history"
          color="#dc3545"
        />

      </div>

    </div>

    <!-- Bảng dữ liệu -->
    <div class="row">

      <!-- Bệnh nhân mới -->
      <div class="col-lg-6 mb-4">

        <div class="card shadow-sm border-0">

          <div class="card-header fw-bold bg-white">

            Bệnh nhân mới

          </div>

          <table class="table table-hover mb-0">

            <thead>

              <tr>

                <th>STT</th>

                <th>Họ tên</th>

                <th>SĐT</th>

              </tr>

            </thead>

            <tbody>

              <tr v-if="patientStore.patients.length === 0">
                <td colspan="3" class="text-center text-secondary py-3">
                  Chưa có dữ liệu
                </td>
              </tr>

              <tr
                v-for="(patient, index) in recentPatients"
                :key="patient.id"
              >

                <td>{{ index + 1 }}</td>

                <td>{{ patient.name }}</td>

                <td>{{ patient.phone }}</td>

              </tr>

            </tbody>

          </table>

        </div>

      </div>

      <!-- Lịch khám hôm nay -->
      <div class="col-lg-6 mb-4">

        <div class="card shadow-sm border-0">

          <div class="card-header fw-bold bg-white">

            Lịch khám gần đây

          </div>

          <table class="table table-hover mb-0">

            <thead>

              <tr>

                <th>Giờ</th>

                <th>Bác sĩ</th>

                <th>Ngày</th>

              </tr>

            </thead>

            <tbody>

              <tr v-if="appointmentStore.appointments.length === 0">
                <td colspan="3" class="text-center text-secondary py-3">
                  Chưa có dữ liệu
                </td>
              </tr>

              <tr
                v-for="appointment in recentAppointments"
                :key="appointment.id"
              >

                <td>{{ appointment.time }}</td>

                <td>{{ appointment.doctor }}</td>

                <td>{{ appointment.date }}</td>

              </tr>

            </tbody>

          </table>

        </div>

      </div>

    </div>

  </div>

</template>

<script setup>

import { onMounted, computed } from "vue"

import AdminSidebar from "../../components/layout/AdminSidebar.vue"
import AdminNavbar from "../../components/layout/AdminNavbar.vue"
import StatCard from "../../components/dashboard/StatCard.vue"

import { useDoctorStore } from "../../stores/doctor"
import { usePatientStore } from "../../stores/patient"
import { useAppointmentStore } from "../../stores/appointment"
import { useQueueStore } from "../../stores/queue"

const doctorStore = useDoctorStore()
const patientStore = usePatientStore()
const appointmentStore = useAppointmentStore()
const queueStore = useQueueStore()

onMounted(() => {
  doctorStore.fetchDoctors().catch(() => {})
  patientStore.fetchPatients().catch(() => {})
  appointmentStore.fetchAppointments().catch(() => {})
  queueStore.fetchQueues().catch(() => {})
})

const recentPatients = computed(() => patientStore.patients.slice(-5).reverse())
const recentAppointments = computed(() => appointmentStore.appointments.slice(-5).reverse())

</script>

<style scoped>

.content{

    margin-left:260px;
    margin-top:75px;
    padding:30px;
    background:#f4f6f9;
    min-height:calc(100vh - 75px);

}

.card{

    border-radius:15px;

}

.card-header{

    font-size:18px;

}

.table{

    margin-bottom:0;

}

thead{

    background:#f8f9fa;

}

</style>
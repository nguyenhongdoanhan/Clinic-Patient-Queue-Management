<template>

  <AdminSidebar />
  <AdminNavbar />

  <div class="content">

    <!-- Tiêu đề -->

    <div class="d-flex justify-content-between align-items-center mb-4">

      <div>

        <h2 class="fw-bold text-primary">
          Quản lý bệnh nhân
        </h2>

        <p class="text-secondary">
          Quản lý thông tin bệnh nhân trong hệ thống
        </p>

      </div>

      <button
        class="btn btn-primary"
        @click="openAddPatient"
      >

        <i class="bi bi-plus-circle me-2"></i>

        Thêm bệnh nhân

      </button>

    </div>

    <!-- Tìm kiếm -->

    <div class="card shadow-sm mb-4">

      <div class="card-body">

        <input
          v-model="search"
          type="text"
          class="form-control"
          placeholder="Tìm theo tên hoặc số điện thoại..."
        >

      </div>

    </div>

    <!-- Bảng -->

    <div class="card shadow-sm">

      <div class="card-body p-0">

        <table class="table table-hover mb-0">

          <thead class="table-primary">

            <tr>

              <th>ID</th>

              <th>Họ tên</th>

              <th>Giới tính</th>

              <th>Ngày sinh</th>

              <th>SĐT</th>

              <th>Địa chỉ</th>

              <th class="text-center">
                Thao tác
              </th>

            </tr>

          </thead>

          <tbody>

            <tr
              v-for="patient in filteredPatients"
              :key="patient.id"
            >

              <td>{{ patient.id }}</td>

              <td>{{ patient.name }}</td>

              <td>{{ patient.gender }}</td>

              <td>{{ patient.birthday }}</td>

              <td>{{ patient.phone }}</td>

              <td>{{ patient.address }}</td>

              <td class="text-center">

                <button
                  class="btn btn-warning btn-sm me-2"
                  @click="openEditPatient(patient)"
                >

                  <i class="bi bi-pencil"></i>

                </button>

                <button
                  class="btn btn-danger btn-sm"
                  @click="openDeletePatient(patient)"
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

    <PatientForm
      v-if="showForm"
      :patient="selectedPatient"
      @save="savePatient"
      @close="showForm=false"
    />

    <DeletePatientModal
      v-if="showDelete"
      :patient="selectedPatient"
      @delete="deletePatient"
      @close="showDelete=false"
    />

  </div>

</template>
<script setup>

import { ref, computed, onMounted } from "vue"

import AdminSidebar from "../../components/layout/AdminSidebar.vue"
import AdminNavbar from "../../components/layout/AdminNavbar.vue"

import PatientForm from "../../components/patient/PatientForm.vue"
import DeletePatientModal from "../../components/patient/DeletePatientModal.vue"

// =========================
// Data bệnh nhân
// =========================

import * as patientService from "../../services/patientService"

const search = ref("")

const patients = ref([])

// Load patients from backend on mount
onMounted(async () => {
  try {
    const res = await patientService.getPatients()
    // map backend `full_name` -> frontend `name`
    patients.value = res.data.map(p => ({
      id: p.id,
      name: p.full_name,
      gender: p.gender,
      birthday: p.birthday,
      phone: p.phone,
      address: p.address,
      email: p.email,
    }))
  } catch (err) {
    console.error("Failed to load patients", err)
  }
})

// =========================
// Modal state
// =========================

const showForm = ref(false)
const showDelete = ref(false)
const selectedPatient = ref(null)

// =========================
// Search filter
// =========================

const filteredPatients = computed(() => {
    return patients.value.filter(p =>
        p.name.toLowerCase().includes(search.value.toLowerCase()) ||
        p.phone.includes(search.value)
    )
})

// =========================
// Open add
// =========================

function openAddPatient() {
    selectedPatient.value = null
    showForm.value = true
}

// =========================
// Open edit
// =========================

function openEditPatient(patient) {
    selectedPatient.value = { ...patient }
    showForm.value = true
}

// =========================
// Open delete
// =========================

function openDeletePatient(patient) {
    selectedPatient.value = patient
    showDelete.value = true
}

// =========================
// Save (add + edit)
// =========================

function savePatient(data) {
  // Map frontend fields to backend payload
  const payload = {
    full_name: data.name,
    gender: data.gender,
    birthday: data.birthday,
    phone: data.phone,
    email: data.email || null,
    address: data.address,
  }

  if (data.id) {
    // Update on backend
    patientService.updatePatient(data.id, payload)
      .then(res => {
        const index = patients.value.findIndex(p => p.id === data.id)
        if (index !== -1) {
          patients.value[index] = { ...patients.value[index], ...{
            name: res.data.full_name,
            gender: res.data.gender,
            birthday: res.data.birthday,
            phone: res.data.phone,
            address: res.data.address,
            email: res.data.email,
          }}
        }
      })
      .catch(err => console.error("Failed to update patient", err))
  } else {
    // Create on backend
    patientService.addPatient(payload)
      .then(res => {
        const p = res.data
        patients.value.push({
          id: p.id,
          name: p.full_name,
          gender: p.gender,
          birthday: p.birthday,
          phone: p.phone,
          address: p.address,
          email: p.email,
        })
      })
      .catch(err => console.error("Failed to create patient", err))
  }

}

// =========================
// Delete
// =========================

function deletePatient(patient) {
  patientService.deletePatient(patient.id)
    .then(() => {
      patients.value = patients.value.filter(p => p.id !== patient.id)
    })
    .catch(err => console.error("Failed to delete patient", err))
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

    transition:.25s;

}

.table tbody tr:hover{

    background:#f8f9fa;

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

    box-shadow:none;

    border-color:#0d6efd;

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
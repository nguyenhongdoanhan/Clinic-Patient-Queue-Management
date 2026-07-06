<template>
  <AdminSidebar />
  <AdminNavbar />

  <div class="content">

    <!-- Tiêu đề -->
    <div class="d-flex justify-content-between align-items-center mb-4">

      <div>
        <h2 class="fw-bold text-primary">
          Quản lý bác sĩ
        </h2>

        <p class="text-secondary">
          Quản lý thông tin bác sĩ trong hệ thống
        </p>
      </div>

      <button
        class="btn btn-primary"
        @click="openAddDoctor"
      >
        <i class="bi bi-plus-circle me-2"></i>
        Thêm bác sĩ
      </button>

    </div>

    <!-- Tìm kiếm -->
    <div class="card shadow-sm mb-4">

      <div class="card-body">

        <input
          type="text"
          class="form-control"
          placeholder="Tìm theo tên hoặc chuyên khoa..."
          v-model="search"
        >

      </div>

    </div>

    <!-- Danh sách -->
    <div class="card shadow-sm">

      <div class="card-body p-0">

        <table class="table table-hover mb-0">

          <thead class="table-primary">

            <tr>

              <th>ID</th>

              <th>Họ tên</th>

              <th>Chuyên khoa</th>

              <th>SĐT</th>

              <th>Email</th>

              <th>Trạng thái</th>

              <th class="text-center">
                Thao tác
              </th>

            </tr>

          </thead>

          <tbody>

            <tr
              v-for="doctor in filteredDoctors"
              :key="doctor.id"
            >

              <td>{{ doctor.id }}</td>

              <td>{{ doctor.name }}</td>

              <td>{{ doctor.specialty }}</td>

              <td>{{ doctor.phone }}</td>

              <td>{{ doctor.email }}</td>

              <td>

                <span
                  class="badge"
                  :class="doctor.status === 'Đang làm việc'
                    ? 'bg-success'
                    : 'bg-secondary'"
                >
                  {{ doctor.status }}
                </span>

              </td>

              <td class="text-center">

                <button
                  class="btn btn-warning btn-sm me-2"
                  @click="openEditDoctor(doctor)"
                >
                  <i class="bi bi-pencil"></i>
                </button>

                <button
                  class="btn btn-danger btn-sm"
                  @click="openDeleteDoctor(doctor)"
                >
                  <i class="bi bi-trash"></i>
                </button>

              </td>

            </tr>

          </tbody>

        </table>

      </div>

    </div>

    <!-- Popup Thêm / Sửa -->
    <DoctorForm
      v-if="showForm"
      :doctor="selectedDoctor"
      @close="showForm = false"
      @save="saveDoctor"
    />

    <!-- Popup Xóa -->
    <DeleteDoctorModal
      v-if="showDelete"
      :doctor="selectedDoctor"
      @close="showDelete = false"
      @delete="deleteDoctor"
    />

  </div>
</template>
<script setup>

import { ref, computed } from "vue"

import AdminSidebar from "../../components/layout/AdminSidebar.vue"
import AdminNavbar from "../../components/layout/AdminNavbar.vue"

import DoctorForm from "../../components/doctor/DoctorForm.vue"
import DeleteDoctorModal from "../../components/doctor/DeleteDoctorModal.vue"

// =========================
// Dữ liệu
// =========================

const search = ref("")

const doctors = ref([

  {
    id: 1,
    name: "Nguyễn Văn A",
    specialty: "Tim mạch",
    phone: "0912345678",
    email: "a@gmail.com",
    status: "Đang làm việc"
  },

  {
    id: 2,
    name: "Trần Thị B",
    specialty: "Da liễu",
    phone: "0988888888",
    email: "b@gmail.com",
    status: "Đang làm việc"
  },

  {
    id: 3,
    name: "Lê Văn C",
    specialty: "Nội tổng quát",
    phone: "0977777777",
    email: "c@gmail.com",
    status: "Nghỉ"
  },

  {
    id: 4,
    name: "Phạm Văn D",
    specialty: "Tai Mũi Họng",
    phone: "0966666666",
    email: "d@gmail.com",
    status: "Đang làm việc"
  }

])

// =========================
// Popup
// =========================

const showForm = ref(false)

const showDelete = ref(false)

const selectedDoctor = ref(null)

// =========================
// Tìm kiếm
// =========================

const filteredDoctors = computed(() => {

  return doctors.value.filter(item =>

    item.name.toLowerCase().includes(search.value.toLowerCase())

    ||

    item.specialty.toLowerCase().includes(search.value.toLowerCase())

  )

})

// =========================
// Thêm
// =========================

const openAddDoctor = () => {

  selectedDoctor.value = null

  showForm.value = true

}

// =========================
// Sửa
// =========================

const openEditDoctor = (doctor) => {

  selectedDoctor.value = { ...doctor }

  showForm.value = true

}

// =========================
// Xóa
// =========================

const openDeleteDoctor = (doctor) => {

  selectedDoctor.value = doctor

  showDelete.value = true

}

// =========================
// Lưu
// =========================

const saveDoctor = (doctor) => {

  if (doctor.id) {

    const index = doctors.value.findIndex(

      d => d.id === doctor.id

    )

    if (index !== -1) {

      doctors.value[index] = { ...doctor }

    }

  } else {

    doctor.id = doctors.value.length

      ? Math.max(...doctors.value.map(d => d.id)) + 1

      : 1

    doctors.value.push({ ...doctor })

  }

}

// =========================
// Xóa
// =========================

const deleteDoctor = (doctor) => {

  doctors.value = doctors.value.filter(

    d => d.id !== doctor.id

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

.btn{
    border-radius:8px;
}

.badge{
    padding:8px 12px;
    font-size:13px;
}

.form-control{
    border-radius:10px;
}

.form-control:focus{
    box-shadow:none;
    border-color:#0d6efd;
}

.table tbody tr{
    transition:0.2s;
}

.table tbody tr:hover{
    background:#f8f9fa;
}

.card-body{
    padding:20px;
}

.card-body.p-0{
    padding:0 !important;
}

h2{
    margin-bottom:5px;
}

.text-secondary{
    margin-bottom:0;
}

.btn-primary{
    padding:10px 18px;
}

.btn-warning,
.btn-danger{
    width:38px;
    height:38px;
}

@media(max-width:992px){

.content{

margin-left:0;

padding:20px;

}

}

</style>
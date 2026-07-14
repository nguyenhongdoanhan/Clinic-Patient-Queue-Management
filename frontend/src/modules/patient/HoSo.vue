<template>
  <div class="container">

    <div class="header">

      <div>
        <h1>👤 Hồ sơ cá nhân</h1>
        <p>Thông tin cá nhân và hồ sơ bệnh nhân.</p>
      </div>

      <RouterLink to="/benh-nhan/cap-nhat-ho-so">
        <button class="edit-btn">
          ✏ Cập nhật hồ sơ
        </button>
      </RouterLink>

    </div>

    <div v-if="error" class="alert error-alert">
      {{ error }}
    </div>

    <div v-if="message" class="alert info-alert">
      {{ message }}
    </div>

    <div class="profile-card" v-if="patient || loading">

      <div class="avatar-section">

        <img
          src="https://via.placeholder.com/180"
          class="avatar"
        >

        <h2>{{ patient?.full_name || authStore.user?.username || 'Bệnh nhân' }}</h2>

        <span class="badge">
          Bệnh nhân
        </span>

      </div>

      <div class="info">

        <div class="row">
          <span>Mã bệnh nhân</span>
          <strong>{{ patient ? `BN${patient.id}` : '---' }}</strong>
        </div>

        <div class="row">
          <span>Ngày sinh</span>
          <strong>{{ formatDate(patient?.birthday) || '---' }}</strong>
        </div>

        <div class="row">
          <span>Giới tính</span>
          <strong>{{ patient?.gender || '---' }}</strong>
        </div>

        <div class="row">
          <span>Số điện thoại</span>
          <strong>{{ patient?.phone || '---' }}</strong>
        </div>

        <div class="row">
          <span>Email</span>
          <strong>{{ patient?.email || authStore.user?.email || '---' }}</strong>
        </div>

        <div class="row">
          <span>Địa chỉ</span>
          <strong>{{ patient?.address || '---' }}</strong>
        </div>

      </div>

    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import * as patientService from "../../services/patientService";
import { useAuthStore } from "../../stores/auth";

const authStore = useAuthStore();
const patient = ref(null);
const loading = ref(false);
const error = ref("");
const message = ref("");

const loadPatient = async () => {
  if (!authStore.user?.email) {
    error.value = "Vui lòng đăng nhập để xem hồ sơ.";
    return;
  }

  loading.value = true;
  error.value = "";
  message.value = "";

  try {
    const res = await patientService.getPatients();
    patient.value = res.data.find((item) => item.email === authStore.user.email) || null;
    if (!patient.value) {
      message.value = "Chưa có hồ sơ bệnh nhân. Vui lòng cập nhật hồ sơ.";
    }
  } catch (err) {
    console.error("Load patient failed", err);
    error.value = "Không tải được hồ sơ bệnh nhân.";
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  loadPatient();
});

const formatDate = (d) => {
  if (!d) return '';
  try {
    const s = String(d);
    const datePart = s.includes('T') ? s.slice(0,10) : s;
    return datePart;
  } catch (e) {
    return '';
  }
};
</script>

<style scoped>

.container{
    padding:30px;
    background:#f5f7fb;
    min-height:100vh;
}

.header{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:30px;
}

.header h1{
    color:#1565c0;
}

.header p{
    color:#666;
    margin-top:8px;
}

.edit-btn{
    background:#1565c0;
    color:white;
    border:none;
    padding:12px 22px;
    border-radius:8px;
    cursor:pointer;
    transition:.3s;
}

.edit-btn:hover{
    background:#1976d2;
}

.profile-card{
    background:white;
    border-radius:15px;
    box-shadow:0 5px 15px rgba(0,0,0,.08);
    padding:35px;
}

.avatar-section{
    text-align:center;
    margin-bottom:35px;
}

.avatar{
    width:180px;
    height:180px;
    border-radius:50%;
    object-fit:cover;
    border:6px solid #e3f2fd;
}

.avatar-section h2{
    margin-top:20px;
    color:#1565c0;
}

.badge{
    display:inline-block;
    margin-top:10px;
    background:#43a047;
    color:white;
    padding:8px 18px;
    border-radius:20px;
    font-size:14px;
}

.info{
    background:#fafafa;
    border-radius:10px;
    padding:20px;
}
.row{
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:16px 5px;
    border-bottom:1px solid #e5e5e5;
}

.row:last-child{
    border-bottom:none;
}

.row span{
    color:#666;
}

.row strong{
    color:#1565c0;
}

</style>
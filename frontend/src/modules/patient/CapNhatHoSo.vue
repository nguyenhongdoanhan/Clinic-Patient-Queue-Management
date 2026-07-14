<template>
  <div class="container">

    <div class="header">

      <div>
        <h1>✏ Cập nhật hồ sơ</h1>
        <p>Chỉnh sửa thông tin cá nhân của bạn.</p>
      </div>

    </div>

    <div class="form-card">

      <div class="avatar-box">

        <img
          src="https://via.placeholder.com/150"
          class="avatar"
        >

        <button class="change-avatar">
          Đổi ảnh đại diện
        </button>

      </div>

      <form @submit.prevent="handleSubmit">

        <div class="row">

          <div class="group">
            <label>Họ và tên</label>
            <input
              type="text"
              v-model="fullName"
              placeholder="Nhập họ và tên"
              required
            >
          </div>

          <div class="group">
            <label>Ngày sinh</label>
            <input
              type="date"
              v-model="birthday"
              required
            >
          </div>

        </div>

        <div class="row">

          <div class="group">
            <label>Giới tính</label>

            <select v-model="gender" required>
              <option value="Nam">Nam</option>
              <option value="Nữ">Nữ</option>
            </select>

          </div>

          <div class="group">
            <label>Số điện thoại</label>

            <input
              type="text"
              v-model="phone"
              placeholder="Nhập số điện thoại"
              required
            >
          </div>

        </div>

        <div class="group">
          <label>Email</label>

          <input
            type="email"
            v-model="email"
            placeholder="Nhập email"
            required
          >
        </div>

        <div class="group">
          <label>Địa chỉ</label>

          <textarea
            rows="4"
            v-model="address"
            placeholder="Nhập địa chỉ"
            required
          ></textarea>
        </div>

        <div class="message-group">
          <p v-if="message" class="success-message">{{ message }}</p>
          <p v-if="error" class="error-message">{{ error }}</p>
        </div>

        <div class="button-group">

          <RouterLink to="/benh-nhan/ho-so">
            <button
              type="button"
              class="cancel"
            >
              Hủy
            </button>
          </RouterLink>

          <button
            type="submit"
            class="save"
            :disabled="loading"
          >
            {{ loading ? 'Đang lưu...' : '💾 Lưu thông tin' }}
          </button>

        </div>

      </form>

    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import * as patientService from "../../services/patientService";
import { useAuthStore } from "../../stores/auth";

const authStore = useAuthStore();
const patientId = ref(null);
const fullName = ref("");
const birthday = ref("");
const gender = ref("Nam");
const phone = ref("");
const email = ref("");
const address = ref("");
const loading = ref(false);
const message = ref("");
const error = ref("");

const loadPatient = async () => {
  if (!authStore.user?.email) {
    return;
  }

  try {
    loading.value = true;
    const res = await patientService.getPatients();
    const patient = res.data.find((item) => item.email === authStore.user.email);

    if (patient) {
      patientId.value = patient.id;
      fullName.value = patient.full_name || "";
      birthday.value = patient.birthday || "";
      gender.value = patient.gender || "Nam";
      phone.value = patient.phone || "";
      email.value = patient.email || authStore.user.email;
      address.value = patient.address || "";
    } else {
      email.value = authStore.user.email;
    }
  } catch (err) {
    console.error("Load patient failed", err);
    error.value = "Không tải được thông tin bệnh nhân.";
  } finally {
    loading.value = false;
  }
};

const handleSubmit = async () => {
  error.value = "";
  message.value = "";
  loading.value = true;

  const payload = {
    full_name: fullName.value,
    gender: gender.value,
    birthday: birthday.value,
    phone: phone.value,
    email: email.value,
    address: address.value,
  };

  try {
    let res;
    if (patientId.value) {
      res = await patientService.updatePatient(patientId.value, payload);
      message.value = "Cập nhật hồ sơ thành công.";
    } else {
      res = await patientService.addPatient(payload);
      patientId.value = res.data.id;
      message.value = "Đã tạo hồ sơ bệnh nhân mới.";
    }

    // Nếu API trả về object patient, cập nhật ngay các field từ response
    if (res?.data) {
      const p = res.data;
      patientId.value = p.id;
      fullName.value = p.full_name || fullName.value;
      // đảm bảo birthday ở định dạng YYYY-MM-DD cho input[type=date]
      if (p.birthday) {
        const b = String(p.birthday);
        birthday.value = b.includes("T") ? b.slice(0, 10) : b;
      }
      gender.value = p.gender || gender.value;
      phone.value = p.phone || phone.value;
      email.value = p.email || email.value;
      address.value = p.address || address.value;
    }

    // reload nhẹ nhàng để đảm bảo đồng bộ nếu cần
    // await loadPatient();
  } catch (err) {
    console.error("Save patient failed", err);
    error.value = err.response?.data?.detail || "Lưu thông tin thất bại.";
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  loadPatient();
});
</script>

<style scoped>

.container{
    padding:30px;
    background:#f5f7fb;
    min-height:100vh;
}

.header{
    margin-bottom:30px;
}

.header h1{
    color:#1565c0;
}

.header p{
    color:#666;
    margin-top:8px;
}

.form-card{
    background:white;
    border-radius:15px;
    box-shadow:0 5px 15px rgba(0,0,0,.08);
    padding:35px;
}

.avatar-box{
    text-align:center;
    margin-bottom:35px;
}

.avatar{
    width:150px;
    height:150px;
    border-radius:50%;
    object-fit:cover;
    border:5px solid #e3f2fd;
}

.change-avatar{
    display:block;
    margin:20px auto 0;
    background:#43a047;
    color:white;
    border:none;
    padding:10px 20px;
    border-radius:8px;
    cursor:pointer;
}

.row{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:20px;
}

.group{
    display:flex;
    flex-direction:column;
    margin-bottom:22px;
}

label{
    margin-bottom:8px;
    font-weight:600;
}

input,
select,
textarea{
    padding:12px;
    border:1px solid #ccc;
    border-radius:8px;
    font-size:15px;
    transition:.3s;
}

input:focus,
select:focus,
textarea:focus{
    outline:none;
    border-color:#1976d2;
    box-shadow:0 0 8px rgba(25,118,210,.2);
}

.button-group{
    display:flex;
    justify-content:flex-end;
    gap:15px;
    margin-top:15px;
}

button{
    padding:12px 25px;
    border:none;
    border-radius:8px;
    cursor:pointer;
    font-size:15px;
}

.cancel{
    background:#9e9e9e;
    color:white;
}
.cancel:hover{
    background:#757575;
}

.save{
    background:#1565c0;
    color:white;
}

.save:hover{
    background:#1976d2;
}

.message-group{
    margin-top:10px;
}

.success-message{
    color:#2e7d32;
    margin-bottom:0;
}

.error-message{
    color:#d32f2f;
    margin-bottom:0;
}

a{
    text-decoration:none;
}

</style>
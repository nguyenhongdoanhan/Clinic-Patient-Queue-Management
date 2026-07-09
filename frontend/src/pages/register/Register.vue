<template>
  <div class="register-page">
    <div class="row g-0 vh-100">

      <!-- Left Side -->
      <div class="col-lg-7 d-none d-lg-flex left-panel">
        <div class="overlay">
          <div class="content">

            <i class="bi bi-heart-pulse-fill display-1"></i>

            <h1 class="fw-bold mt-3">
              Hệ thống Quản lý
            </h1>

            <h2 class="hospital-name">
              Bệnh Viện
            </h2>

            <p class="slogan">
              Nhanh chóng • Đơn giản • Tiện ích
            </p>

          </div>
        </div>
      </div>

      <!-- Right Side -->
      <div class="col-lg-5 d-flex justify-content-center align-items-center">

        <div class="register-card">

          <div class="text-center mb-4">

            <i class="bi bi-person-plus-fill logo"></i>

            <h2 class="fw-bold mt-3">
              Tạo tài khoản
            </h2>

            <p class="text-secondary">
              Đăng ký để sử dụng hệ thống
            </p>

          </div>

          <div
            v-if="authStore.error"
            class="alert alert-danger py-2"
            role="alert"
          >
            {{ authStore.error }}
          </div>

          <form @submit.prevent="register">

            <!-- Họ tên -->
            <div class="mb-3">

              <label class="form-label">
                Họ và tên
              </label>

              <input
                v-model="form.fullName"
                type="text"
                class="form-control"
                placeholder="Nhập họ và tên"
                required
              />

            </div>

            <!-- Email -->
            <div class="mb-3">

              <label class="form-label">
                Địa chỉ Email
              </label>

              <input
                v-model="form.email"
                type="email"
                class="form-control"
                placeholder="Nhập email"
                required
              />

              <small
                class="text-danger"
                v-if="emailError"
              >
                {{ emailError }}
              </small>

            </div>

            <!-- Điện thoại -->
            <div class="mb-3">

              <label class="form-label">
                Số điện thoại
              </label>

              <input
                v-model="form.phone"
                type="text"
                class="form-control"
                placeholder="Nhập số điện thoại"
                required
              />

            </div>

            <!-- Địa chỉ -->
            <div class="mb-3">

              <label class="form-label">
                Địa chỉ
              </label>

              <textarea
                v-model="form.address"
                rows="2"
                class="form-control"
                placeholder="Nhập địa chỉ"
              ></textarea>

            </div>

            <!-- Mật khẩu -->
            <div class="mb-3">

              <label class="form-label">
                Mật khẩu
              </label>

              <div class="input-group">

                <span class="input-group-text">
                  <i class="bi bi-lock"></i>
                </span>

                <input
                  :type="showPassword ? 'text' : 'password'"
                  v-model="form.password"
                  class="form-control"
                  placeholder="Nhập mật khẩu"
                  required
                />

                <button
                  type="button"
                  class="btn btn-outline-secondary"
                  @click="showPassword=!showPassword"
                >

                  <i
                    :class="showPassword
                    ? 'bi bi-eye-slash'
                    : 'bi bi-eye'"
                  ></i>

                </button>

              </div>

            </div>

            <!-- Xác nhận mật khẩu -->
            <div class="mb-3">

              <label class="form-label">
                Xác nhận mật khẩu
              </label>

              <input
                type="password"
                v-model="confirmPassword"
                class="form-control"
                placeholder="Nhập lại mật khẩu"
                required
              />

              <small
                class="text-danger"
                v-if="passwordError"
              >
                {{ passwordError }}
              </small>

            </div>

            <!-- Điều khoản -->

            <div class="form-check mb-4">

              <input
                class="form-check-input"
                type="checkbox"
                v-model="accept"
              />

              <label class="form-check-label">

                Tôi đồng ý với các điều khoản sử dụng

              </label>

            </div>

            <!-- Button -->

            <div class="d-grid">

              <button
                class="btn btn-primary btn-lg"
                type="submit"
                :disabled="authStore.loading"
              >

                <span
                  v-if="authStore.loading"
                  class="spinner-border spinner-border-sm me-2"
                ></span>
                <i v-else class="bi bi-person-plus-fill"></i>

                {{ authStore.loading ? "Đang đăng ký..." : "Đăng ký" }}

              </button>

            </div>

          </form>

          <hr>

          <div class="text-center">

            Đã có tài khoản?

            <router-link to="/login">

              Đăng nhập

            </router-link>

          </div>

        </div>

      </div>

    </div>

  </div>
</template>

<script setup>
import { reactive, ref } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "../../stores/auth";

const router = useRouter();
const authStore = useAuthStore();

const showPassword = ref(false);

const confirmPassword = ref("");

const accept = ref(false);

const emailError = ref("");

const passwordError = ref("");

const form = reactive({

  fullName: "",

  email: "",

  phone: "",

  address: "",

  password: ""

});

const register = async () => {

  emailError.value = "";
  passwordError.value = "";

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (!emailRegex.test(form.email)) {
    emailError.value = "Email không hợp lệ";
    return;
  }

  if (form.password !== confirmPassword.value) {
    passwordError.value = "Mật khẩu xác nhận không khớp";
    return;
  }

  if (!accept.value) {
    alert("Bạn cần đồng ý điều khoản.");
    return;
  }

  try {

    const payload = {
      name: form.fullName,
      email: form.email,
      password: form.password,
      phone: form.phone,
      address: form.address,
      role: "Bệnh nhân",
      status: "Hoạt động"
    };

    console.log(payload);

    await authStore.register(payload);

    alert("Đăng ký thành công!");

    router.push("/login");

  } catch (error) {

    console.error(error);

  }

};
</script><style scoped>

.register-page{
    background:#f4f6f9;
}

.left-panel{
    background:linear-gradient(135deg,#0d6efd,#3b82f6);
    color:white;
}

.overlay{
    width:100%;
    height:100%;
    display:flex;
    justify-content:center;
    align-items:center;
}

.content{
    text-align:center;
}

.hospital-name{
    font-size:40px;
    font-weight:700;
    margin-top:10px;
    margin-bottom:20px;
}

.slogan{
    font-size:24px;
    font-weight:500;
    letter-spacing:1px;
}

.register-card{
    width:460px;
    background:white;
    padding:40px;
    border-radius:20px;
    box-shadow:0 10px 30px rgba(0,0,0,.15);
    transition:.3s;
}

.register-card:hover{
    transform:translateY(-5px);
    box-shadow:0 18px 40px rgba(0,0,0,.18);
}

.logo{
    font-size:70px;
    color:#0d6efd;
}

.form-label{
    font-weight:600;
    margin-bottom:8px;
}

.form-control{
    height:50px;
    font-size:16px;
}

textarea.form-control{
    height:auto;
    resize:none;
}

.form-control::placeholder{
    color:#999;
}

.input-group-text{
    width:50px;
    justify-content:center;
}

.form-check-label{
    font-size:15px;
}

.text-secondary{
    font-size:17px;
}

.btn-lg{
    height:52px;
    font-size:20px;
    font-weight:600;
    border-radius:10px;
    transition:.3s;
}

.btn-lg:hover{
    transform:translateY(-2px);
}

.text-decoration-none{
    font-weight:500;
}

a{
    text-decoration:none;
    font-weight:600;
}

a:hover{
    text-decoration:underline;
}

.display-1{
    font-size:90px;
}

@media(max-width:991px){

    .register-card{
        width:90%;
        padding:30px;
    }

    .hospital-name{
        font-size:32px;
    }

    .slogan{
        font-size:18px;
    }

}

</style>
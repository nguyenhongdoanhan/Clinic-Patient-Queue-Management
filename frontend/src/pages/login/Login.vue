<template>
  <div class="login-page">
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

        <div class="login-card">

          <div class="text-center mb-4">

            <i class="bi bi-person-circle logo"></i>

            <h2 class="fw-bold mt-3">
              Chào mừng
            </h2>

            <p class="text-secondary">
              Đăng nhập để tiếp tục
            </p>

          </div>

          <div
            v-if="authStore.error"
            class="alert alert-danger py-2"
            role="alert"
          >
            {{ authStore.error }}
          </div>

          <form @submit.prevent="login">

            <!-- Email -->
            <div class="mb-3">

              <label class="form-label">
                Địa chỉ Email
              </label>

              <div class="input-group">

                <span class="input-group-text">
                  <i class="bi bi-envelope"></i>
                </span>

                <input
                  v-model="email"
                  type="email"
                  class="form-control"
                  placeholder="Nhập địa chỉ email"
                  required
                />

              </div>

            </div>

            <!-- Password -->
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
                  v-model="password"
                  class="form-control"
                  placeholder="Nhập mật khẩu"
                  required
                />

                <button
                  type="button"
                  class="btn btn-outline-secondary"
                  @click="showPassword = !showPassword"
                >
                  <i
                    :class="
                      showPassword
                        ? 'bi bi-eye-slash'
                        : 'bi bi-eye'
                    "
                  ></i>
                </button>

              </div>

            </div>

            <!-- Remember -->
            <div
              class="d-flex justify-content-between align-items-center mb-4"
            >

              <div class="form-check">

                <input
                  class="form-check-input"
                  type="checkbox"
                  v-model="remember"
                />

                <label class="form-check-label">
                  Ghi nhớ đăng nhập
                </label>

              </div>

              <a href="#" class="text-decoration-none">
                Quên mật khẩu?
              </a>

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
                <i v-else class="bi bi-box-arrow-in-right"></i>

                {{ authStore.loading ? "Đang đăng nhập..." : "Đăng nhập" }}

              </button>

            </div>

          </form>

          <hr>

          <div class="text-center">

            Chưa có tài khoản?

            <router-link to="/register">

              Đăng ký

            </router-link>

          </div>

        </div>

      </div>

    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter, useRoute } from "vue-router";
import { useAuthStore } from "../../stores/auth";

const router = useRouter();
const route = useRoute();
const authStore = useAuthStore();

const email = ref("");
const password = ref("");
const remember = ref(false);
const showPassword = ref(false);

const login = async () => {
  try {
    await authStore.login({
      email: email.value,
      password: password.value,
    });

    // Nếu bị điều hướng từ 1 trang admin cụ thể thì quay lại đúng trang đó
    router.push(route.query.redirect || "/admin/dashboard");
  } catch (err) {
    // Lỗi đã được lưu trong authStore.error để hiển thị lên giao diện
  }
};
</script>

<style scoped>

.login-page{
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

.login-card{

    width:450px;
    background:white;
    padding:40px;
    border-radius:20px;
    box-shadow:0 10px 30px rgba(0,0,0,.15);
    transition:.3s;

}

.login-card:hover{

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

.form-control::placeholder{

    color:#999;

}

.input-group-text{

    width:50px;
    justify-content:center;

}

.form-check-label{

    font-size:16px;

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

@media(max-width:991px){

.login-card{

width:90%;

}

}

</style>
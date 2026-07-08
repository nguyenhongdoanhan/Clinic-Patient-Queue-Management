<template>
  <div class="login-page">
    <!-- LEFT -->
    <div class="left-panel">
      <div class="overlay">
        <div class="content">
          <div class="logo">🏥</div>

          <h1>Clinic Management</h1>

          <p>
            Hệ thống quản lý phòng khám & hàng đợi khám bệnh
          </p>
//
          <ul>
            <li>✔ Quản lý bệnh nhân</li>
            <li>✔ Quản lý bác sĩ</li>
            <li>✔ Đặt lịch khám</li>
            <li>✔ Hàng đợi khám bệnh</li>
            <li>✔ Hồ sơ bệnh án</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- RIGHT -->
    <div class="right-panel">
      <div class="login-card">

        <h2>Đăng nhập Admin</h2>

        <p class="subtitle">
          Đăng nhập để quản lý hệ thống
        </p>

        <form @submit.prevent="handleLogin">

          <div class="form-group">
            <label>Tên đăng nhập</label>

            <input
              type="text"
              v-model="username"
              placeholder="Nhập tên đăng nhập"
            >
          </div>

          <div class="form-group">
            <label>Mật khẩu</label>

            <input
              :type="showPassword ? 'text' : 'password'"
              v-model="password"
              placeholder="Nhập mật khẩu"
            >
          </div>

          <div class="options">

            <label>

              <input
                type="checkbox"
                v-model="remember"
              >

              Ghi nhớ đăng nhập

            </label>

            <a href="#">
              Quên mật khẩu?
            </a>

          </div>

          <button type="submit">
            Đăng nhập
          </button>

        </form>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const username = ref("");
const password = ref("");
const remember = ref(false);
const showPassword = ref(false);

const handleLogin = () => {

  console.log({
    username: username.value,
    password: password.value,
    remember: remember.value,
  });

  // TODO:
  // axios.post("/login", {...})

};
</script>

<style scoped>

*{
  margin:0;
  padding:0;
  box-sizing:border-box;
  font-family:Arial, Helvetica, sans-serif;
}

.login-page{
  display:flex;
  height:100vh;
}

/* LEFT */

.left-panel{
  width:55%;
  background:linear-gradient(135deg,#0f766e,#14b8a6);
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
  width:70%;
}

.logo{
  font-size:80px;
  margin-bottom:20px;
}

.content h1{
  font-size:45px;
  margin-bottom:20px;
}

.content p{
  font-size:20px;
  line-height:35px;
  margin-bottom:40px;
}

.content ul{
  list-style:none;
}

.content li{
  margin:15px 0;
  font-size:18px;
}

/* RIGHT */

.right-panel{
  width:45%;
  background:#f4f7fb;
  display:flex;
  justify-content:center;
  align-items:center;
}

.login-card{

  width:420px;

  background:white;

  border-radius:18px;

  padding:40px;

  box-shadow:0 15px 40px rgba(0,0,0,.15);

}

.login-card h2{

  font-size:32px;

  margin-bottom:10px;

}

.subtitle{

  color:#777;

  margin-bottom:30px;

}

.form-group{

  display:flex;

  flex-direction:column;

  margin-bottom:20px;

}

.form-group label{

  margin-bottom:8px;

  font-weight:bold;

}

.form-group input{

  padding:14px;

  border-radius:8px;

  border:1px solid #ddd;

  outline:none;

  transition:.3s;

}

.form-group input:focus{

  border-color:#14b8a6;

}

.options{

  display:flex;

  justify-content:space-between;

  align-items:center;

  margin-bottom:25px;

  font-size:14px;

}

.options a{

  text-decoration:none;

  color:#14b8a6;

}

button{

  width:100%;

  padding:15px;

  background:#14b8a6;

  color:white;

  border:none;

  border-radius:8px;

  cursor:pointer;

  font-size:17px;

  transition:.3s;

}

button:hover{

  background:#0f766e;

}

@media(max-width:900px){

.left-panel{

display:none;

}

.right-panel{

width:100%;

}

.login-card{

width:90%;

}

}

</style>
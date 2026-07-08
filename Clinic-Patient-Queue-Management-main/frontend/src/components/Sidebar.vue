<template>
  <aside class="sidebar">

    <h2 class="logo">🏥 Clinic</h2>

    <RouterLink to="/" class="item">
      🏠 Trang chủ
    </RouterLink>

    <RouterLink to="/benh-nhan" class="item">
      👤 Bệnh nhân
    </RouterLink>

    <RouterLink to="/le-tan" class="item">
      🧑‍💼 Lễ tân
    </RouterLink>

    <RouterLink to="/bac-si" class="item">
      👨‍⚕️ Bác sĩ
    </RouterLink>

    <!-- Nút đăng xuất -->
    <button class="logout-btn" @click="logout">
      🚪 Đăng xuất
    </button>

  </aside>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

const logout = () => {
  // Xóa dữ liệu đăng nhập (để sau này dùng)
  localStorage.clear();

  // Quay về trang chủ
  router.push("/");
};
</script>

<style scoped>

.sidebar{
    width:240px;
    height:100vh;
    background:#1565c0;
    display:flex;
    flex-direction:column;
    padding:25px;
    position:fixed;
    left:0;
    top:0;
}

.logo{
    color:white;
    margin-bottom:40px;
    text-align:center;
}

.item{
    color:white;
    padding:15px;
    margin-bottom:10px;
    border-radius:8px;
    transition:.3s;
    text-decoration:none;
}

.item:hover{
    background:rgba(255,255,255,.2);
}

.router-link-active{
    background:white;
    color:#1565c0;
    font-weight:bold;
}

/* Đẩy nút xuống cuối */
.logout-btn{
    margin-top:auto;
    padding:15px;
    border:none;
    border-radius:8px;
    background:#e53935;
    color:white;
    font-size:15px;
    cursor:pointer;
    transition:.3s;
}

.logout-btn:hover{
    background:#c62828;
}

</style>
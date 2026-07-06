<template>
  <div class="sidebar">

    <!-- Logo -->
    <div class="logo">
      <i class="bi bi-hospital-fill"></i>
      <h4>Quản trị</h4>
    </div>

    <!-- Menu -->
    <div class="menu">

      <router-link
        to="/admin/dashboard"
        class="menu-item"
        active-class="active"
      >
        <i class="bi bi-speedometer2"></i>
        <span>Dashboard</span>
      </router-link>

      <router-link
        to="/admin/users"
        class="menu-item"
        active-class="active"
      >
        <i class="bi bi-people-fill"></i>
        <span>Quản lý người dùng</span>
      </router-link>

      <router-link
        to="/admin/doctors"
        class="menu-item"
        active-class="active"
      >
        <i class="bi bi-person-badge-fill"></i>
        <span>Quản lý bác sĩ</span>
      </router-link>

      <router-link
        to="/admin/patients"
        class="menu-item"
        active-class="active"
      >
        <i class="bi bi-person-heart"></i>
        <span>Quản lý bệnh nhân</span>
      </router-link>

      <router-link
        to="/admin/appointments"
        class="menu-item"
        active-class="active"
      >
        <i class="bi bi-calendar-check"></i>
        <span>Lịch khám</span>
      </router-link>

      <router-link
        to="/admin/queue"
        class="menu-item"
        active-class="active"
      >
        <i class="bi bi-list-task"></i>
        <span>Hàng đợi</span>
      </router-link>

      

    </div>

    <!-- Logout -->

    <div class="logout" @click="logout">

      <i class="bi bi-box-arrow-right"></i>

      <span>Đăng xuất</span>

    </div>

  </div>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

function logout() {

  if (confirm("Bạn có chắc muốn đăng xuất?")) {

    localStorage.removeItem("token");
    localStorage.removeItem("user");

    router.push("/login");

  }

}
</script>

<style scoped>

.sidebar{

    width:260px;
    height:100vh;
    background:#0d6efd;
    position:fixed;
    left:0;
    top:0;
    display:flex;
    flex-direction:column;
    color:white;
    box-shadow:3px 0 12px rgba(0,0,0,.15);

}

.logo{

    padding:35px 20px;
    text-align:center;
    border-bottom:1px solid rgba(255,255,255,.2);

}

.logo i{

    font-size:70px;

}

.logo h4{

    margin-top:15px;
    font-size:20px;
    font-weight:bold;

}

.menu{

    flex:1;
    display:flex;
    flex-direction:column;
    padding-top:15px;

}

.menu-item{

    color:white;
    text-decoration:none;
    padding:17px 25px;
    display:flex;
    align-items:center;
    gap:15px;
    transition:.3s;
    font-size:18px;

}

.menu-item i{

    width:22px;
    font-size:20px;

}

.menu-item:hover{

    background:rgba(255,255,255,.15);

}

.active{

    background:white;
    color:#0d6efd !important;
    border-left:5px solid #ffc107;
    font-weight:600;

}

.logout{

    padding:18px 25px;
    display:flex;
    align-items:center;
    gap:15px;
    cursor:pointer;
    border-top:1px solid rgba(255,255,255,.2);
    transition:.3s;
    font-size:18px;

}

.logout:hover{

    background:#084298;

}

.logout i{

    width:22px;
    font-size:22px;

}

</style>
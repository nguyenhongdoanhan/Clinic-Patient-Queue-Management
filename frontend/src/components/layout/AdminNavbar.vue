<template>
  <nav class="navbar">

    <div class="left">

      <h3>🏥 Hệ thống Quản lý Bệnh viện</h3>

    </div>

    <div class="right">

      <button class="notification">

        <i class="bi bi-bell-fill"></i>

      </button>

      <div class="admin">

        <img
          src="https://ui-avatars.com/api/?name=Admin&background=0d6efd&color=fff"
          alt="admin"
        />

        <div>

          <strong>Quản trị viên</strong>

          <br>

          <small>Administrator</small>

        </div>

      </div>

    </div>

  </nav>
</template>

<style scoped>

.navbar{

margin-left:260px;

height:75px;

background:white;

display:flex;

justify-content:space-between;

align-items:center;

padding:0 30px;

box-shadow:0 2px 10px rgba(0,0,0,.08);

}

.left h3{

margin:0;

font-weight:bold;

color:#0d6efd;

}

.right{

display:flex;

align-items:center;

gap:25px;

}

.notification{

border:none;

background:#f5f5f5;

width:45px;

height:45px;

border-radius:50%;

cursor:pointer;

font-size:20px;

}

.notification:hover{

background:#0d6efd;

color:white;

}

.admin{

display:flex;

align-items:center;

gap:10px;

}

.admin img{

width:45px;

height:45px;

border-radius:50%;

}

</style>
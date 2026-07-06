<template>
  <div class="home fade">

    <div class="hero">

      <h1>🏥 HỆ THỐNG QUẢN LÝ PHÒNG KHÁM</h1>

      <p>
        Clinic Patient Queue Management System
      </p>

    </div>

    <div class="card-container">

      <!-- Patient -->
      <RouterLink to="/benh-nhan" class="home-card">

        <div class="icon">👤</div>

        <h2>Bệnh nhân</h2>

        <p>
          Quản lý hồ sơ cá nhân, đặt lịch khám,
          theo dõi hàng đợi và lịch sử khám bệnh.
        </p>

        <button class="btn">
          Vào hệ thống →
        </button>

      </RouterLink>

      <!-- Receptionist -->
      <RouterLink to="/le-tan" class="home-card">

        <div class="icon">🧑‍💼</div>

        <h2>Lễ tân</h2>

        <p>
          Quản lý thông tin bệnh nhân,
          lịch khám và hàng đợi khám.
        </p>

        <button class="btn">
          Vào hệ thống →
        </button>

      </RouterLink>

      <!-- Doctor -->
      <RouterLink to="/bac-si" class="home-card">

        <div class="icon">👨‍⚕️</div>

        <h2>Bác sĩ</h2>

        <p>
          Khám bệnh, chẩn đoán,
          kê đơn thuốc và hoàn thành ca khám.
        </p>

        <button class="btn">
          Vào hệ thống →
        </button>

      </RouterLink>

    </div>

  </div>
</template>

<style scoped>

.home{

    min-height:100vh;

    padding:60px;

    background:linear-gradient(135deg,#eef4ff,#ffffff);

}

.hero{

    text-align:center;

    margin-bottom:60px;

}

.hero h1{

    font-size:42px;

    color:#1565c0;

    margin-bottom:15px;

}

.hero p{

    color:#666;

    font-size:18px;

}

.card-container{

    display:grid;

    grid-template-columns:repeat(auto-fit,minmax(320px,1fr));

    gap:35px;

}

.home-card{

    background:white;

    border-radius:20px;

    padding:40px 30px;

    text-align:center;

    color:#333;

    border-top:8px solid #1976d2;

    box-shadow:0 10px 30px rgba(0,0,0,.08);

    transition:.35s;

}

.home-card:hover{

    transform:translateY(-10px);

    box-shadow:0 20px 40px rgba(25,118,210,.18);

}

.icon{

    font-size:75px;

    margin-bottom:20px;

}

.home-card h2{

    color:#1565c0;

    margin-bottom:18px;

}

.home-card p{

    color:#666;

    line-height:1.8;

    margin-bottom:30px;

    min-height:90px;

}

.btn{

    width:100%;

}

</style>
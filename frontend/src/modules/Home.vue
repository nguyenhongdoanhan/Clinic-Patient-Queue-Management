<template>
  <div class="home fade">

    <div class="hero">
      <h1>🏥 HỆ THỐNG QUẢN LÝ PHÒNG KHÁM</h1>
      <p>Clinic Patient Queue Management System</p>
    </div>

    <div class="card-container">

      <!-- Bệnh nhân -->
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

      <!-- Lễ tân -->
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

      <!-- Bác sĩ -->
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

.home {
  min-height: 100vh;
  padding: 60px;
  position: relative;
  overflow: hidden;
  background:
    linear-gradient(
      rgba(240,248,255,0.85),
      rgba(240,248,255,0.9)
    ),
    url("https://images.unsplash.com/photo-1586773860418-d37222d8fce3");
  background-size: cover;
  background-position: center;
}

.home::before {
  content: "";
  position: absolute;
  width: 500px;
  height: 500px;
  background: rgba(33,150,243,.12);
  border-radius: 50%;
  top: -200px;
  left: -150px;
}

.home::after {
  content: "";
  position: absolute;
  width: 400px;
  height: 400px;
  background: rgba(25,118,210,.1);
  border-radius: 50%;
  bottom: -150px;
  right: -100px;
}

.hero {
  text-align: center;
  margin-bottom: 70px;
  position: relative;
  z-index: 1;
}

.hero h1 {
  font-size: 50px;
  color: #1565c0;
  margin-bottom: 20px;
  font-weight: bold;
  text-shadow: 2px 2px 10px rgba(0,0,0,.1);
}

.hero p {
  font-size: 22px;
  color: #555;
}

.card-container {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(330px,1fr));
  gap: 35px;
  position: relative;
  z-index: 1;
}

.home-card {
  background: rgba(255,255,255,.75);
  backdrop-filter: blur(15px);
  border-radius: 30px;
  padding: 45px 35px;
  text-align: center;
  color: #333;
  text-decoration: none;
  border: 1px solid rgba(255,255,255,.6);
  box-shadow: 0 10px 40px rgba(0,0,0,.1);
  transition: .4s;
}

.home-card:hover {
  transform: translateY(-15px) scale(1.03);
  box-shadow: 0 20px 50px rgba(25,118,210,.25);
}

.icon {
  font-size: 80px;
  margin-bottom: 25px;
  animation: float 3s infinite ease-in-out;
}

.home-card h2 {
  color: #1565c0;
  margin-bottom: 20px;
  font-size: 34px;
}

.home-card p {
  color: #666;
  line-height: 1.8;
  margin-bottom: 35px;
  min-height: 100px;
}

.btn {
  width: 100%;
  border: none;
  padding: 15px;
  border-radius: 14px;
  background: linear-gradient(
    90deg,
    #1565c0,
    #42a5f5
  );
  color: white;
  font-size: 18px;
  font-weight: bold;
  cursor: pointer;
  transition: .3s;
}

.btn:hover {
  transform: scale(1.05);
}

@keyframes float {
  0% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-12px);
  }
  100% {
    transform: translateY(0);
  }
}

</style>



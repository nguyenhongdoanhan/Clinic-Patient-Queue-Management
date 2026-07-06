<template>
  <div class="container fade">

    <h1 class="page-title">👨‍⚕️ Bảng điều khiển Bác sĩ</h1>

    <p style="color:#666;margin-bottom:30px;">
      Theo dõi tình trạng khám bệnh và quản lý bệnh nhân trong ngày.
    </p>

    <!-- Thống kê -->
    <div class="dashboard-grid">

      <div class="dashboard-card">
        <div class="icon">🧑‍🤝‍🧑</div>
        <p>Bệnh nhân hôm nay</p>
        <h2>18</h2>
      </div>

      <div class="dashboard-card">
        <div class="icon">🩺</div>
        <p>Đang khám</p>
        <h2>03</h2>
      </div>

      <div class="dashboard-card">
        <div class="icon">✅</div>
        <p>Đã hoàn thành</p>
        <h2>15</h2>
      </div>

      <div class="dashboard-card">
        <div class="icon">📅</div>
        <p>Lịch khám hôm nay</p>
        <h2>18</h2>
      </div>

    </div>

    <br><br>

    <!-- Chức năng nhanh -->
    <div style="display:flex;gap:20px;flex-wrap:wrap;">

      <RouterLink to="/bac-si/danh-sach">
        <button class="btn">
          👥 Danh sách bệnh nhân
        </button>
      </RouterLink>

      <RouterLink to="/bac-si/ho-so">
        <button class="btn">
          📋 Hồ sơ bệnh nhân
        </button>
      </RouterLink>

      <RouterLink to="/bac-si/chan-doan">
        <button class="btn">
          🩺 Chẩn đoán
        </button>
      </RouterLink>

      <RouterLink to="/bac-si/ket-qua">
        <button class="btn">
          📄 Kết quả khám
        </button>
      </RouterLink>

      <RouterLink to="/bac-si/ke-don">
        <button class="btn">
          💊 Kê đơn thuốc
        </button>
      </RouterLink>

      <RouterLink to="/bac-si/hoan-thanh">
        <button class="btn">
          ✔ Hoàn thành ca khám
        </button>
      </RouterLink>

    </div>

  </div>
</template>
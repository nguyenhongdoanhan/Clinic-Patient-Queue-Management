<template>
  <div class="container">

    <div class="header">

      <div>
        <h1>👤 Bảng điều khiển Bệnh nhân</h1>
        <p>Xin chào Nguyễn Văn A, chúc bạn một ngày tốt lành!</p>
      </div>

      <button class="today">
        📅 Hôm nay: 08/07/2026
      </button>

    </div>

    <div class="dashboard-grid">

      <div class="dashboard-card">
        <div class="icon">📅</div>
        <h2>02</h2>
        <p>Lịch khám sắp tới</p>
      </div>

      <div class="dashboard-card">
        <div class="icon">📄</div>
        <h2>08</h2>
        <p>Lần khám</p>
      </div>

      <div class="dashboard-card">
        <div class="icon">💊</div>
        <h2>03</h2>
        <p>Đơn thuốc</p>
      </div>

      <div class="dashboard-card">
        <div class="icon">⏳</div>
        <h2>05</h2>
        <p>Số thứ tự khám</p>
      </div>

    </div>

    <h2 class="title">
      Chức năng
    </h2>

    <div class="menu-grid">

      <RouterLink to="/benh-nhan/ho-so" class="menu-card">

        <div class="menu-icon">
          👤
        </div>

        <h3>Hồ sơ cá nhân</h3>

        <p>
          Xem thông tin và hồ sơ bệnh án.
        </p>

      </RouterLink>

      <RouterLink to="/benh-nhan/cap-nhat-ho-so" class="menu-card">

        <div class="menu-icon">
          ✏
        </div>

        <h3>Cập nhật hồ sơ</h3>

        <p>
          Chỉnh sửa thông tin cá nhân.
        </p>

      </RouterLink>

      <RouterLink to="/benh-nhan/dat-lich" class="menu-card">

        <div class="menu-icon">
          📅
        </div>

        <h3>Đặt lịch khám</h3>

        <p>
          Đăng ký lịch khám với bác sĩ.
        </p>

      </RouterLink>

      <RouterLink to="/benh-nhan/lich-kham" class="menu-card">

        <div class="menu-icon">
          🗓
        </div>

        <h3>Lịch khám</h3>

        <p>
          Xem lịch khám đã đặt.
        </p>

      </RouterLink>

      <RouterLink to="/benh-nhan/lich-su" class="menu-card">

        <div class="menu-icon">
          📋
        </div>

        <h3>Lịch sử khám</h3>

        <p>
          Xem các lần khám trước đây.
        </p>

      </RouterLink>

      <RouterLink to="/benh-nhan/hang-doi" class="menu-card">

        <div class="menu-icon">
          🔢
        </div>

        <h3>Theo dõi hàng đợi</h3>

        <p>
          Theo dõi số thứ tự khám.
        </p>

      </RouterLink>

    </div>

  </div>
</template>

<style scoped>

.container{
    padding:30px;
    background:#f5f7fb;
    min-height:100vh;
}

.header{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:35px;
}

.header h1{
    color:#1565c0;
}

.header p{
    margin-top:8px;
    color:#666;
}

.today{
    background:#1565c0;
    color:white;
    border:none;
    padding:12px 22px;
    border-radius:10px;
}

.dashboard-grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
    gap:20px;
    margin-bottom:40px;
}

.dashboard-card{
    background:white;
    padding:30px;
    border-radius:15px;
    text-align:center;
    box-shadow:0 5px 15px rgba(0,0,0,.08);
    transition:.3s;
}

.dashboard-card:hover{
    transform:translateY(-6px);
}

.icon{
    font-size:50px;
    margin-bottom:15px;
}

.dashboard-card h2{
    color:#1565c0;
    font-size:32px;
    margin-bottom:10px;
}

.dashboard-card p{
    color:#666;
}

.title{
    color:#1565c0;
    margin-bottom:20px;
}

.menu-grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
    gap:20px;
}

.menu-card{
    background:white;
    border-radius:15px;
    padding:25px;
    text-decoration:none;
    color:#333;
    box-shadow:0 5px 15px rgba(0,0,0,.08);
    transition:.3s;
}
//
.menu-card:hover{
    background:#1976d2;
    color:white;
    transform:translateY(-5px);
}

.menu-icon{
    font-size:45px;
    margin-bottom:15px;
}

.menu-card h3{
    margin-bottom:10px;
}

.menu-card p{
    line-height:1.6;
}

</style>
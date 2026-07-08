<template>
  <div class="dashboard">

    <h1>Bảng điều khiển Lễ tân</h1>
    <p>Quản lý bệnh nhân và hàng đợi khám bệnh.</p>

    <div class="cards">

      <div class="card">
        <div class="icon">👥</div>
        <h3>Bệnh nhân hôm nay</h3>
        <h2>35</h2>
      </div>

      <div class="card">
        <div class="icon">📅</div>
        <h3>Lịch khám</h3>
        <h2>28</h2>
      </div>

      <div class="card">
        <div class="icon">⏳</div>
        <h3>Đang chờ</h3>
        <h2>12</h2>
      </div>

      <div class="card">
        <div class="icon">✅</div>
        <h3>Đã hoàn thành</h3>
        <h2>16</h2>
      </div>

    </div>

    <div class="menu">

      <RouterLink to="/le-tan/benh-nhan" class="box">
        👤
        <span>Quản lý bệnh nhân</span>
      </RouterLink>

      <RouterLink to="/le-tan/them-benh-nhan" class="box">
        ➕
        <span>Thêm bệnh nhân</span>
      </RouterLink>

      <RouterLink to="/le-tan/lich-kham" class="box">
        📅
        <span>Quản lý lịch khám</span>
      </RouterLink>

      <RouterLink to="/le-tan/hang-doi" class="box">
        🔢
        <span>Quản lý hàng đợi</span>
      </RouterLink>

    </div>

  </div>
</template>

<style scoped>

.dashboard{
    padding:30px;
    background:#f4f7fb;
    min-height:100vh;
}

h1{
    color:#1565c0;
}

p{
    color:#666;
    margin-bottom:30px;
}

.cards{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:20px;
}

.card{
    background:white;
    padding:25px;
    border-radius:12px;
    text-align:center;
    box-shadow:0 2px 8px rgba(0,0,0,.1);
}

.icon{
    font-size:40px;
    margin-bottom:15px;
}

.card h2{
    color:#1565c0;
    margin-top:10px;
}

.menu{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:20px;
    margin-top:40px;
}
//
.box{
    background:white;
    border-radius:12px;
    padding:30px;
    text-align:center;
    text-decoration:none;
    color:#333;
    display:flex;
    flex-direction:column;
    gap:15px;
    font-size:20px;
    box-shadow:0 2px 8px rgba(0,0,0,.1);
    transition:.3s;
}

.box:hover{
    background:#1565c0;
    color:white;
}

</style>
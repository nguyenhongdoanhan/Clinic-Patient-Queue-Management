<template>
  <div class="container">

    <div class="header">

      <div>
        <h1>🔢 Theo dõi hàng đợi</h1>
        <p>Cập nhật tình trạng hàng đợi khám bệnh theo thời gian thực.</p>
      </div>

    </div>

    <div class="cards">

      <div class="card">
        <div class="icon">🎫</div>
        <h3>Số thứ tự của bạn</h3>
        <h1>A015</h1>
      </div>

      <div class="card">
        <div class="icon">👨‍⚕️</div>
        <h3>Đang khám</h3>
        <h1>A012</h1>
      </div>

      <div class="card">
        <div class="icon">⏳</div>
        <h3>Còn chờ</h3>
        <h1>03</h1>
      </div>

      <div class="card">
        <div class="icon">🕒</div>
        <h3>Thời gian chờ</h3>
        <h1>15 phút</h1>
      </div>

    </div>

    <div class="status-card">

      <h2>Thông báo</h2>

      <p>
        Hiện tại phòng khám đang phục vụ số <strong>A012</strong>.
      </p>

      <p>
        Dự kiến đến lượt bạn sau khoảng
        <strong>15 phút</strong>.
      </p>

      <button>
        Làm mới
      </button>

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
    margin-bottom:35px;
}

.header h1{
    color:#1565c0;
}

.header p{
    color:#666;
    margin-top:8px;
}

.cards{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:20px;
    margin-bottom:35px;
}

.card{
    background:white;
    padding:30px;
    border-radius:15px;
    text-align:center;
    box-shadow:0 5px 15px rgba(0,0,0,.08);
    transition:.3s;
}

.card:hover{
    transform:translateY(-6px);
    box-shadow:0 10px 20px rgba(0,0,0,.15);
}

.icon{
    font-size:45px;
    margin-bottom:15px;
}

.card h3{
    color:#666;
    margin-bottom:15px;
    font-weight:600;
}

.card h1{
    color:#1565c0;
    font-size:38px;
}

.status-card{
    background:white;
    padding:35px;
    border-radius:15px;
    box-shadow:0 5px 15px rgba(0,0,0,.08);
}

.status-card h2{
    color:#1565c0;
    margin-bottom:20px;
}

.status-card p{
    margin-bottom:15px;
    font-size:16px;
    color:#555;
}
button{
    margin-top:15px;
    background:#1565c0;
    color:white;
    border:none;
    padding:12px 25px;
    border-radius:8px;
    cursor:pointer;
    font-size:15px;
    transition:.3s;
}

button:hover{
    background:#1976d2;
}

</style>
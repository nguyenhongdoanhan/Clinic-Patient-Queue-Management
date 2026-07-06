<template>
  <div class="container">

    <div class="header">

      <h1>✏️ Cập nhật thông tin bệnh nhân</h1>

      <RouterLink to="/le-tan/benh-nhan">
        <button class="back-btn">← Quay lại</button>
      </RouterLink>

    </div>

    <form class="form">

      <div class="row">

        <div class="group">
          <label>Họ và tên</label>
          <input type="text" value="Nguyễn Văn A">
        </div>

        <div class="group">
          <label>Ngày sinh</label>
          <input type="date" value="2002-05-10">
        </div>

      </div>

      <div class="row">

        <div class="group">
          <label>Giới tính</label>
          <select>
            <option selected>Nam</option>
            <option>Nữ</option>
          </select>
        </div>

        <div class="group">
          <label>Số điện thoại</label>
          <input type="text" value="0912345678">
        </div>

      </div>

      <div class="group">
        <label>Địa chỉ</label>
        <input type="text" value="Đà Nẵng">
      </div>

      <div class="group">
        <label>Chuyên khoa</label>
        <select>
          <option selected>Nội tổng quát</option>
          <option>Tim mạch</option>
          <option>Nhi khoa</option>
          <option>Da liễu</option>
        </select>
      </div>

      <div class="group">
        <label>Tiền sử bệnh</label>
        <textarea rows="4">Không có</textarea>
      </div>

      <div class="button-group">

        <RouterLink to="/le-tan/benh-nhan">
          <button type="button" class="cancel">
            Hủy
          </button>
        </RouterLink>

        <button type="submit" class="save">
          💾 Lưu thay đổi
        </button>

      </div>

    </form>

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
    margin-bottom:30px;
}

h1{
    color:#1565c0;
    font-size:30px;
}

.form{
    background:white;
    padding:35px;
    border-radius:15px;
    box-shadow:0 6px 20px rgba(0,0,0,.08);
}

.row{
    display:grid;
    grid-template-columns:repeat(2,1fr);
    gap:20px;
}

.group{
    display:flex;
    flex-direction:column;
    margin-bottom:20px;
}

label{
    font-weight:600;
    margin-bottom:8px;
    color:#444;
}

input,
select,
textarea{
    padding:13px;
    border:1px solid #dcdcdc;
    border-radius:10px;
    font-size:15px;
    transition:.3s;
}

input:focus,
select:focus,
textarea:focus{
    outline:none;
    border-color:#1976d2;
    box-shadow:0 0 8px rgba(25,118,210,.2);
}

textarea{
    resize:none;
}

.button-group{
    display:flex;
    justify-content:flex-end;
    gap:15px;
    margin-top:30px;
}

button{
    border:none;
    padding:13px 28px;
    border-radius:10px;
    cursor:pointer;
    font-size:15px;
    transition:.3s;
}

.save{
    background:#1565c0;
    color:white;
}

.save:hover{
    background:#1976d2;
    transform:translateY(-2px);
}

.cancel{
    background:#9e9e9e;
    color:white;
}

.cancel:hover{
    background:#757575;
}

.back-btn{
    background:#1565c0;
    color:white;
}

.back-btn:hover{
    background:#1976d2;
}

a{
    text-decoration:none;
}

</style>
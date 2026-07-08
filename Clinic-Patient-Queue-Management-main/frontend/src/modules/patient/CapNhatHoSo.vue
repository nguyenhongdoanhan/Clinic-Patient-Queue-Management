<template>
  <div class="container">

    <div class="header">

      <div>
        <h1>✏ Cập nhật hồ sơ</h1>
        <p>Chỉnh sửa thông tin cá nhân của bạn.</p>
      </div>

    </div>

    <div class="form-card">

      <div class="avatar-box">

        <img
          src="https://via.placeholder.com/150"
          class="avatar"
        >

        <button class="change-avatar">
          Đổi ảnh đại diện
        </button>

      </div>

      <form>

        <div class="row">

          <div class="group">
            <label>Họ và tên</label>
            <input
              type="text"
              value="Nguyễn Văn A"
            >
          </div>

          <div class="group">
            <label>Ngày sinh</label>
            <input
              type="date"
              value="2003-05-15"
            >
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

            <input
              type="text"
              value="0912345678"
            >
          </div>

        </div>

        <div class="group">
          <label>Email</label>

          <input
            type="email"
            value="vana@gmail.com"
          >
        </div>

        <div class="group">
          <label>Địa chỉ</label>

          <textarea rows="4">Đà Nẵng</textarea>
        </div>

        <div class="button-group">

          <RouterLink to="/benh-nhan/ho-so">
            <button
              type="button"
              class="cancel"
            >
              Hủy
            </button>
          </RouterLink>

          <button
            type="submit"
            class="save"
          >
            💾 Lưu thông tin
          </button>

        </div>

      </form>

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
    margin-bottom:30px;
}

.header h1{
    color:#1565c0;
}

.header p{
    color:#666;
    margin-top:8px;
}

.form-card{
    background:white;
    border-radius:15px;
    box-shadow:0 5px 15px rgba(0,0,0,.08);
    padding:35px;
}

.avatar-box{
    text-align:center;
    margin-bottom:35px;
}

.avatar{
    width:150px;
    height:150px;
    border-radius:50%;
    object-fit:cover;
    border:5px solid #e3f2fd;
}

.change-avatar{
    display:block;
    margin:20px auto 0;
    background:#43a047;
    color:white;
    border:none;
    padding:10px 20px;
    border-radius:8px;
    cursor:pointer;
}

.row{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:20px;
}

.group{
    display:flex;
    flex-direction:column;
    margin-bottom:22px;
}

label{
    margin-bottom:8px;
    font-weight:600;
}

input,
select,
textarea{
    padding:12px;
    border:1px solid #ccc;
    border-radius:8px;
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

.button-group{
    display:flex;
    justify-content:flex-end;
    gap:15px;
    margin-top:15px;
}

button{
    padding:12px 25px;
    border:none;
    border-radius:8px;
    cursor:pointer;
    font-size:15px;
}

.cancel{
    background:#9e9e9e;
    color:white;
}
//
.cancel:hover{
    background:#757575;
}

.save{
    background:#1565c0;
    color:white;
}

.save:hover{
    background:#1976d2;
}

a{
    text-decoration:none;
}

</style>
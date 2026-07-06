<template>
  <div class="container">

    <div class="header">

      <div>
        <h1>📅 Đặt lịch khám</h1>
        <p>Đặt lịch khám với bác sĩ theo chuyên khoa.</p>
      </div>

    </div>

    <div class="form-card">

      <form>

        <div class="row">

          <div class="group">
            <label>Chuyên khoa</label>

            <select>
              <option>Nội tổng quát</option>
              <option>Nhi khoa</option>
              <option>Tim mạch</option>
              <option>Da liễu</option>
              <option>Răng hàm mặt</option>
            </select>
          </div>

          <div class="group">
            <label>Bác sĩ</label>

            <select>
              <option>BS. Nguyễn Văn Bình</option>
              <option>BS. Trần Văn Hải</option>
              <option>BS. Lê Thị Lan</option>
            </select>
          </div>

        </div>

        <div class="row">

          <div class="group">
            <label>Ngày khám</label>
            <input type="date">
          </div>

          <div class="group">
            <label>Giờ khám</label>
            <input type="time">
          </div>

        </div>

        <div class="group">
          <label>Lý do khám</label>

          <textarea
            rows="5"
            placeholder="Nhập lý do khám bệnh..."
          ></textarea>
        </div>

        <div class="button-group">

          <RouterLink to="/benh-nhan">
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
            📅 Đặt lịch khám
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
    padding:35px;
    border-radius:15px;
    box-shadow:0 5px 15px rgba(0,0,0,.08);
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
<template>
  <div class="container">

    <div class="header">

      <div>
        <h1>📅 Lịch khám của tôi</h1>
        <p>Danh sách các lịch khám đã đặt.</p>
      </div>

      <RouterLink to="/benh-nhan/dat-lich">
        <button class="add-btn">
          + Đặt lịch mới
        </button>
      </RouterLink>

    </div>

    <div class="table-card">

      <table>

        <thead>
          <tr>
            <th>STT</th>
            <th>Ngày khám</th>
            <th>Giờ</th>
            <th>Bác sĩ</th>
            <th>Chuyên khoa</th>
            <th>Trạng thái</th>
            <th>Thao tác</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>1</td>
            <td>15/07/2026</td>
            <td>08:00</td>
            <td>BS. Nguyễn Văn Bình</td>
            <td>Nội tổng quát</td>

            <td>
              <span class="badge success">
                Đã xác nhận
              </span>
            </td>

            <td>
              <button class="cancel">
                Hủy lịch
              </button>
            </td>
          </tr>

          <tr>
            <td>2</td>
            <td>18/07/2026</td>
            <td>14:00</td>
            <td>BS. Lê Thị Lan</td>
            <td>Tim mạch</td>

            <td>
              <span class="badge waiting">
                Chờ xác nhận
              </span>
            </td>

            <td>
              <button class="cancel">
                Hủy lịch
              </button>
            </td>
          </tr>

        </tbody>

      </table>

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
    margin-bottom:30px;
}

.header h1{
    color:#1565c0;
}

.header p{
    color:#666;
    margin-top:8px;
}

.add-btn{
    background:#1565c0;
    color:white;
    border:none;
    padding:12px 20px;
    border-radius:8px;
    cursor:pointer;
    font-size:15px;
}

.add-btn:hover{
    background:#1976d2;
}

.table-card{
    background:white;
    border-radius:15px;
    overflow:hidden;
    box-shadow:0 5px 15px rgba(0,0,0,.08);
}

table{
    width:100%;
    border-collapse:collapse;
}

th{
    background:#1565c0;
    color:white;
    padding:15px;
}

td{
    padding:15px;
    text-align:center;
    border-bottom:1px solid #eee;
}

tr:hover{
    background:#f8fbff;
}

.badge{
    padding:6px 14px;
    border-radius:20px;
    color:white;
    font-size:13px;
    font-weight:600;
}

.success{
    background:#43a047;
}

.waiting{
    background:#fb8c00;
}

.cancel{
    background:#e53935;
    color:white;
    border:none;
    padding:8px 15px;
    border-radius:6px;
    cursor:pointer;
}

.cancel:hover{
    background:#c62828;
}

a{
    text-decoration:none;
}

</style>
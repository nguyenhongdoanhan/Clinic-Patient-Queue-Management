<template>
  <div class="container">

    <div class="header">

      <div>
        <h1>📅 Quản lý lịch khám</h1>
        <p>Quản lý các lịch khám của bệnh nhân.</p>
      </div>

      <button class="add-btn">
        ➕ Tạo lịch khám
      </button>

    </div>

    <div class="search-box">

      <input
        type="text"
        placeholder="🔍 Tìm theo tên bệnh nhân..."
      >

      <select>
        <option>Tất cả trạng thái</option>
        <option>Đã xác nhận</option>
        <option>Chờ khám</option>
        <option>Đã hoàn thành</option>
      </select>

    </div>

    <div class="table-box">

      <table>

        <thead>

          <tr>
            <th>Mã lịch</th>
            <th>Bệnh nhân</th>
            <th>Bác sĩ</th>
            <th>Chuyên khoa</th>
            <th>Ngày khám</th>
            <th>Giờ</th>
            <th>Trạng thái</th>
            <th>Thao tác</th>
          </tr>

        </thead>

        <tbody>

          <tr>

            <td>LK001</td>
            <td>Nguyễn Văn A</td>
            <td>BS. Trần Minh</td>
            <td>Nội tổng quát</td>
            <td>08/07/2026</td>
            <td>08:00</td>

            <td>
              <span class="success">
                Đã xác nhận
              </span>
            </td>

            <td>

              <button class="edit">
                ✏ Cập nhật
              </button>

              <button class="delete">
                🗑 Hủy
              </button>

            </td>

          </tr>

          <tr>

            <td>LK002</td>
            <td>Trần Thị B</td>
            <td>BS. Lê Hải</td>
            <td>Tim mạch</td>
            <td>08/07/2026</td>
            <td>09:30</td>

            <td>
              <span class="warning">
                Chờ khám
              </span>
            </td>

            <td>

              <button class="edit">
                ✏ Cập nhật
              </button>

              <button class="delete">
                🗑 Hủy
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
    margin-bottom:8px;
}

.header p{
    color:#666;
}

.add-btn{
    background:#1565c0;
    color:white;
    border:none;
    padding:13px 24px;
    border-radius:10px;
    cursor:pointer;
    transition:.3s;
}

.add-btn:hover{
    background:#1976d2;
    transform:translateY(-2px);
}

.search-box{
    display:flex;
    gap:20px;
    margin-bottom:25px;
}

.search-box input,
.search-box select{
    padding:12px;
    border:1px solid #ddd;
    border-radius:10px;
    font-size:15px;
}

.search-box input{
    width:350px;
}

.table-box{
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
    padding:16px;
}

td{
    padding:15px;
    text-align:center;
    border-bottom:1px solid #eee;
}

tr:hover{
    background:#f5f9ff;
}

.success{
    background:#4caf50;
    color:white;
    padding:6px 12px;
    border-radius:20px;
    font-size:13px;
}

.warning{
    background:#ff9800;
    color:white;
    padding:6px 12px;
    border-radius:20px;
    font-size:13px;
}

.edit,
.delete{
    border:none;
    padding:9px 15px;
    border-radius:8px;
    cursor:pointer;
    color:white;
    transition:.3s;
}

.edit{
    background:#1976d2;
    margin-right:8px;
}

.delete{
    background:#e53935;
}

.edit:hover{
    background:#1565c0;
}

.delete:hover{
    background:#c62828;
}

</style>
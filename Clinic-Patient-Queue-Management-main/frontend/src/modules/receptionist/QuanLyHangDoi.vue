<template>
  <div class="container">

    <div class="header">

      <div>
        <h1>🔢 Quản lý hàng đợi khám bệnh</h1>
        <p>Theo dõi và điều phối bệnh nhân đang chờ khám.</p>
      </div>

      <div class="summary">

        <div class="box">
          <h3>Đang chờ</h3>
          <span>12</span>
        </div>

        <div class="box">
          <h3>Đang khám</h3>
          <span>3</span>
        </div>

        <div class="box">
          <h3>Hoàn thành</h3>
          <span>20</span>
        </div>

      </div>

    </div>

    <div class="table-box">

      <table>

        <thead>

          <tr>
            <th>STT</th>
            <th>Bệnh nhân</th>
            <th>Bác sĩ</th>
            <th>Phòng khám</th>
            <th>Trạng thái</th>
            <th>Thao tác</th>
          </tr>

        </thead>

        <tbody>

          <tr>

            <td>A001</td>
            <td>Nguyễn Văn A</td>
            <td>BS. Trần Minh</td>
            <td>Phòng 101</td>

            <td>
              <span class="waiting">
                Đang chờ
              </span>
            </td>

            <td>

              <button class="blue">
                📢 Gọi
              </button>

              <button class="green">
                🔄 Chuyển
              </button>

              <button class="gray">
                ✔ Hoàn thành
              </button>

            </td>

          </tr>

          <tr>

            <td>A002</td>
            <td>Trần Thị B</td>
            <td>BS. Lê Hải</td>
            <td>Phòng 102</td>

            <td>
              <span class="exam">
                Đang khám
              </span>
            </td>

            <td>

              <button class="blue">
                📢 Gọi
              </button>

              <button class="green">
                🔄 Chuyển
              </button>

              <button class="gray">
                ✔ Hoàn thành
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
    align-items:flex-start;
    margin-bottom:30px;
}

.header h1{
    color:#1565c0;
    margin-bottom:8px;
}

.header p{
    color:#666;
}

.summary{
    display:flex;
    gap:15px;
}

.box{
    background:white;
    padding:18px;
    border-radius:12px;
    text-align:center;
    width:120px;
    box-shadow:0 4px 12px rgba(0,0,0,.08);
}

.box h3{
    font-size:14px;
    color:#777;
    margin-bottom:8px;
}

.box span{
    font-size:28px;
    color:#1565c0;
    font-weight:bold;
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
    padding:16px;
    text-align:center;
    border-bottom:1px solid #eee;
}

tr:hover{
    background:#f7fbff;
}

.waiting{
    background:#ff9800;
    color:white;
    padding:6px 14px;
    border-radius:20px;
    font-size:13px;
}

.exam{
    background:#43a047;
    color:white;
    padding:6px 14px;
    border-radius:20px;
    font-size:13px;
}

button{
    border:none;
    color:white;
    padding:9px 14px;
    border-radius:8px;
    cursor:pointer;
    margin:3px;
    transition:.3s;
}

.blue{
    background:#1976d2;
}

.blue:hover{
    background:#1565c0;
}
//
.green{
    background:#43a047;
}

.green:hover{
    background:#2e7d32;
}

.gray{
    background:#757575;
}

.gray:hover{
    background:#555;
}

</style>
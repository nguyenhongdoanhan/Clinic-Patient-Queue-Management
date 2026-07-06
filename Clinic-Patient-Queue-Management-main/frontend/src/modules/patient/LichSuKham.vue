<template>
  <div class="container">

    <div class="header">

      <div>
        <h1>📋 Lịch sử khám bệnh</h1>
        <p>Theo dõi các lần khám và đơn thuốc trước đây.</p>
      </div>

    </div>

    <div class="table-card">

      <table>

        <thead>

          <tr>
            <th>Ngày khám</th>
            <th>Bác sĩ</th>
            <th>Chẩn đoán</th>
            <th>Đơn thuốc</th>
            <th>Kết quả</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>10/06/2026</td>
            <td>BS. Trần Văn Hải</td>
            <td>Viêm họng</td>
            <td>Amoxicillin</td>

            <td>
              <span class="badge success">
                Hoàn thành
              </span>
            </td>

          </tr>

          <tr>
            <td>25/05/2026</td>
            <td>BS. Lê Thị Lan</td>
            <td>Cảm cúm</td>
            <td>Paracetamol</td>

            <td>
              <span class="badge success">
                Hoàn thành
              </span>
            </td>

          </tr>

          <tr>
            <td>12/04/2026</td>
            <td>BS. Nguyễn Văn Bình</td>
            <td>Đau dạ dày</td>
            <td>Omeprazole</td>

            <td>
              <span class="badge success">
                Hoàn thành
              </span>
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
    margin-bottom:30px;
}

.header h1{
    color:#1565c0;
}

.header p{
    color:#666;
    margin-top:8px;
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

</style>
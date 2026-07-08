<script setup>
import { ref } from "vue";

const patients = ref([
  {
    id: 1,
    code: "BN001",
    name: "Nguyễn Văn A",
    gender: "Nam",
    phone: "0912345678",
    status: "Đang chờ",
  },
  {
    id: 2,
    code: "BN002",
    name: "Trần Thị B",
    gender: "Nữ",
    phone: "0988123456",
    status: "Đã khám",
  },
]);
</script>

<template>
  <div class="container fade">

    <div
      style="
        display:flex;
        justify-content:space-between;
        align-items:center;
        margin-bottom:25px;
        flex-wrap:wrap;
        gap:15px;
      "
    >

      <h1 class="page-title">
        👥 Quản lý bệnh nhân
      </h1>

      <RouterLink to="/le-tan/them-benh-nhan">
        <button class="btn">
          ➕ Thêm bệnh nhân
        </button>
      </RouterLink>

    </div>

    <div class="card">

      <div
        style="
          display:flex;
          justify-content:space-between;
          gap:20px;
          margin-bottom:25px;
          flex-wrap:wrap;
        "
      >

        <input
          type="text"
          placeholder="🔍 Tìm theo tên hoặc số điện thoại..."
          style="max-width:400px;"
        />

      </div>

      <table>

        <thead>

          <tr>
            <th>Mã BN</th>
            <th>Họ và tên</th>
            <th>Giới tính</th>
            <th>Số điện thoại</th>
            <th>Trạng thái</th>
            <th>Thao tác</th>
          </tr>

        </thead>

        <tbody>

          <tr
            v-for="patient in patients"
            :key="patient.id"
          >

            <td>{{ patient.code }}</td>
            <td>{{ patient.name }}</td>
            <td>{{ patient.gender }}</td>
            <td>{{ patient.phone }}</td>

            <td>

              <span
                :class="
                  patient.status === 'Đang chờ'
                    ? 'badge-warning'
                    : 'badge-success'
                "
              >
                {{ patient.status }}
              </span>

            </td>

            <td>

              <RouterLink to="/le-tan/sua-benh-nhan">
                <button class="btn">
                  ✏️ Sửa
                </button>
              </RouterLink>

              &nbsp;

              <button class="btn">
                🗑 Xóa
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
}

.page-title{
    color:#1565c0;
    margin-bottom:10px;
}

.card{
    background:white;
    padding:25px;
    border-radius:12px;
    box-shadow:0 2px 10px rgba(0,0,0,.1);
}

input{
    width:100%;
    padding:12px;
    border:1px solid #ccc;
    border-radius:8px;
    font-size:15px;
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
    border-bottom:1px solid #ddd;
    text-align:center;
}

.btn{
    background:#1565c0;
    color:white;
    border:none;
    padding:8px 15px;
    border-radius:6px;
    cursor:pointer;
}

.btn:hover{
    background:#1976d2;
}

.badge-warning{
    background:#ff9800;
    color:white;
    padding:6px 12px;
    border-radius:20px;
    font-size:13px;
}

.badge-success{
    background:#43a047;
    color:white;
    padding:6px 12px;
    border-radius:20px;
    font-size:13px;
}

.fade{
    animation:fade .4s;
}

@keyframes fade{
    from{
        opacity:0;
        transform:translateY(10px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}
//
</style>
<template>

  <!-- Sidebar -->
  <AdminSidebar />

  <!-- Navbar -->
  <AdminNavbar />

  <!-- Nội dung -->
  <div class="content">

    <!-- Tiêu đề -->
    <div class="mb-4">

      <h2 class="fw-bold">
        Dashboard
      </h2>

      <p class="text-secondary">
        Chào mừng bạn đến với Hệ thống Quản lý Bệnh viện.
      </p>

    </div>

    <!-- Thống kê -->
    <div class="row">

      <div class="col-lg-3 col-md-6 mb-4">

        <StatCard
          title="Bác sĩ"
          :value="20"
          icon="bi bi-person-badge-fill"
          color="#0d6efd"
        />

      </div>

      <div class="col-lg-3 col-md-6 mb-4">

        <StatCard
          title="Bệnh nhân"
          :value="350"
          icon="bi bi-people-fill"
          color="#198754"
        />

      </div>

      <div class="col-lg-3 col-md-6 mb-4">

        <StatCard
          title="Lịch khám"
          :value="45"
          icon="bi bi-calendar-check-fill"
          color="#ffc107"
        />

      </div>

      <div class="col-lg-3 col-md-6 mb-4">

        <StatCard
          title="Đang chờ"
          :value="12"
          icon="bi bi-clock-history"
          color="#dc3545"
        />

      </div>

    </div>

    <!-- Bảng dữ liệu -->
    <div class="row">

      <!-- Bệnh nhân mới -->
      <div class="col-lg-6 mb-4">

        <div class="card shadow-sm border-0">

          <div class="card-header fw-bold bg-white">

            Bệnh nhân mới

          </div>

          <table class="table table-hover mb-0">

            <thead>

              <tr>

                <th>STT</th>

                <th>Họ tên</th>

                <th>SĐT</th>

              </tr>

            </thead>

            <tbody>

              <tr>

                <td>1</td>

                <td>Nguyễn Văn A</td>

                <td>0901234567</td>

              </tr>

              <tr>

                <td>2</td>

                <td>Trần Thị B</td>

                <td>0912345678</td>

              </tr>

              <tr>

                <td>3</td>

                <td>Lê Văn C</td>

                <td>0988888888</td>

              </tr>

            </tbody>

          </table>

        </div>

      </div>

      <!-- Lịch khám hôm nay -->
      <div class="col-lg-6 mb-4">

        <div class="card shadow-sm border-0">

          <div class="card-header fw-bold bg-white">

            Lịch khám hôm nay

          </div>

          <table class="table table-hover mb-0">

            <thead>

              <tr>

                <th>Giờ</th>

                <th>Bác sĩ</th>

                <th>Chuyên khoa</th>

              </tr>

            </thead>

            <tbody>

              <tr>

                <td>08:00</td>

                <td>BS. Minh</td>

                <td>Nội tổng quát</td>

              </tr>

              <tr>

                <td>09:00</td>

                <td>BS. Hùng</td>

                <td>Tim mạch</td>

              </tr>

              <tr>

                <td>10:30</td>

                <td>BS. Phương</td>

                <td>Nhi khoa</td>

              </tr>

            </tbody>

          </table>

        </div>

      </div>

    </div>

  </div>

</template>

<script setup>

import AdminSidebar from "../../components/layout/AdminSidebar.vue"
import AdminNavbar from "../../components/layout/AdminNavbar.vue"
import StatCard from "../../components/dashboard/StatCard.vue"

</script>

<style scoped>

.content{

    margin-left:260px;
    margin-top:75px;
    padding:30px;
    background:#f4f6f9;
    min-height:calc(100vh - 75px);

}

.card{

    border-radius:15px;

}

.card-header{

    font-size:18px;

}

.table{

    margin-bottom:0;

}

thead{

    background:#f8f9fa;

}

</style>
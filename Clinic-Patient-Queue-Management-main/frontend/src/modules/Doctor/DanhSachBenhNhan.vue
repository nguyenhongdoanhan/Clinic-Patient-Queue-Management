<template>
  <div class="container fade">

    <div class="flex-between" style="margin-bottom:25px;">

      <h1 class="page-title">👨‍⚕️ Danh sách bệnh nhân hôm nay</h1>

      <button class="btn">
        🔄 Làm mới
      </button>

    </div>

    <div class="card">

      <table>

        <thead>

          <tr>
            <th>Mã BN</th>
            <th>Họ tên</th>
            <th>Giới tính</th>
            <th>Chuyên khoa</th>
            <th>Số thứ tự</th>
            <th>Trạng thái</th>
            <th>Thao tác</th>
          </tr>

        </thead>

        <tbody>

          <tr>

            <td>BN001</td>
            <td>Nguyễn Văn A</td>
            <td>Nam</td>
            <td>Nội tổng quát</td>
            <td>A001</td>

            <td>
              <span class="badge-warning">
                Đang chờ
              </span>
            </td>

            <td>

              <RouterLink to="/bac-si/ho-so">
                <button class="btn">
                  📄 Hồ sơ
                </button>
              </RouterLink>

              &nbsp;

              <RouterLink to="/bac-si/chan-doan">
                <button class="btn">
                  🩺 Khám
                </button>
              </RouterLink>

            </td>

          </tr>

          <tr>

            <td>BN002</td>
            <td>Trần Thị B</td>
            <td>Nữ</td>
            <td>Tim mạch</td>
            <td>A002</td>

            <td>
              <span class="badge-success">
                Đã khám
              </span>
            </td>

            <td>

              <RouterLink to="/bac-si/ho-so">
                <button class="btn">
                  📄 Hồ sơ
                </button>
              </RouterLink>

              &nbsp;

              <RouterLink to="/bac-si/ket-qua">
                <button class="btn">
                  📋 Kết quả
                </button>
              </RouterLink>

            </td>

          </tr>

        </tbody>

      </table>

    </div>

  </div>
</template>
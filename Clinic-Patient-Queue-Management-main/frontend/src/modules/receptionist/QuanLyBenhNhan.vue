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
        >

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

          <tr>

            <td>BN001</td>
            <td>Nguyễn Văn A</td>
            <td>Nam</td>
            <td>0912345678</td>

            <td>
              <span class="badge-warning">
                Đang chờ
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

          <tr>

            <td>BN002</td>
            <td>Trần Thị B</td>
            <td>Nữ</td>
            <td>0988123456</td>

            <td>
              <span class="badge-success">
                Đã khám
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
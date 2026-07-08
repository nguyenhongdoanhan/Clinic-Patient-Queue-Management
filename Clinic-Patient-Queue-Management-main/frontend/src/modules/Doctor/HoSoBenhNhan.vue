<template>
  <div class="container fade">

    <div class="flex-between" style="margin-bottom:25px;">

      <h1 class="page-title">📋 Hồ sơ bệnh nhân</h1>

      <RouterLink to="/bac-si/chan-doan">
        <button class="btn">
          🩺 Bắt đầu khám
        </button>
      </RouterLink>

    </div>

    <div class="card">

      <table>

        <tbody>

          <tr>
            <th width="30%">Mã bệnh nhân</th>
            <td>BN001</td>
          </tr>

          <tr>
            <th>Họ và tên</th>
            <td>Nguyễn Văn A</td>
          </tr>

          <tr>
            <th>Ngày sinh</th>
            <td>10/05/2002</td>
          </tr>

          <tr>
            <th>Giới tính</th>
            <td>Nam</td>
          </tr>

          <tr>
            <th>Số điện thoại</th>
            <td>0912345678</td>
          </tr>

          <tr>
            <th>Địa chỉ</th>
            <td>Đà Nẵng</td>
          </tr>

          <tr>
            <th>Tiền sử bệnh</th>
            <td>Không có</td>
          </tr>
//
          <tr>
            <th>Dị ứng thuốc</th>
            <td>Không</td>
          </tr>

          <tr>
            <th>Nhóm máu</th>
            <td>O+</td>
          </tr>

        </tbody>

      </table>

    </div>

  </div>
</template>
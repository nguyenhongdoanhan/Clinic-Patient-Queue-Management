<template>
  <div class="container fade">

    <div class="card" style="max-width:700px;margin:auto;text-align:center;">

      <div style="font-size:80px;margin-bottom:20px;">
        ✅
      </div>

      <h1 class="page-title">
        Hoàn thành ca khám
      </h1>

      <p style="color:#666;margin-bottom:30px;">
        Hồ sơ khám bệnh đã được lưu thành công.
      </p>

      <table>

        <tbody>

          <tr>
            <th width="35%">Mã bệnh nhân</th>
            <td>BN001</td>
          </tr>

          <tr>
            <th>Họ và tên</th>
            <td>Nguyễn Văn A</td>
          </tr>

          <tr>
            <th>Bác sĩ khám</th>
            <td>BS. Trần Minh</td>
          </tr>

          <tr>
            <th>Chẩn đoán</th>
            <td>Viêm họng cấp</td>
          </tr>

          <tr>
            <th>Thời gian khám</th>
            <td>09:00 - 09:30</td>
          </tr>

          <tr>
            <th>Trạng thái</th>
            <td>
              <span class="badge-success">
                Hoàn thành
              </span>
            </td>
          </tr>

        </tbody>

      </table>

      <div
        style="
          display:flex;
          justify-content:center;
          gap:20px;
          margin-top:35px;
          flex-wrap:wrap;
        "
      >

        <RouterLink to="/bac-si/danh-sach">
          <button class="btn">
            👥 Danh sách bệnh nhân
          </button>
        </RouterLink>

        <RouterLink to="/bac-si">
          <button class="btn">
            🏠 Về Dashboard
          </button>
        </RouterLink>

      </div>

    </div>

  </div>
</template>
<template>
  <div class="container fade">

    <div
      style="
        display:flex;
        justify-content:space-between;
        align-items:center;
        margin-bottom:25px;
      "
    >

      <h1 class="page-title">
        ➕ Thêm bệnh nhân
      </h1>

      <RouterLink to="/le-tan/benh-nhan">
        <button class="btn">
          ← Quay lại
        </button>
      </RouterLink>

    </div>

    <div class="card">

      <div
        style="
          display:grid;
          grid-template-columns:repeat(2,1fr);
          gap:25px;
        "
      >

        <div class="group">
          <label>Họ và tên</label>
          <input
            type="text"
            placeholder="Nhập họ và tên"
          >
        </div>

        <div class="group">
          <label>Ngày sinh</label>
          <input type="date">
        </div>

        <div class="group">
          <label>Giới tính</label>

          <select>
            <option>Nam</option>
            <option>Nữ</option>
          </select>

        </div>

        <div class="group">
          <label>Số điện thoại</label>
          <input
            type="text"
            placeholder="09xxxxxxxx"
          >
        </div>

        <div class="group">
          <label>Địa chỉ</label>
          <input
            type="text"
            placeholder="Nhập địa chỉ"
          >
        </div>

        <div class="group">
          <label>Chuyên khoa</label>

          <select>
            <option>Nội tổng quát</option>
            <option>Tim mạch</option>
            <option>Nhi khoa</option>
            <option>Da liễu</option>
          </select>

        </div>

      </div>

      <div class="group">

        <label>Tiền sử bệnh</label>

        <textarea
          rows="4"
          placeholder="Nhập tiền sử bệnh nếu có..."
        ></textarea>

      </div>

      <div
        style="
          display:flex;
          justify-content:flex-end;
          gap:15px;
          margin-top:25px;
        "
      >
//
        <RouterLink to="/le-tan/benh-nhan">
          <button class="btn">
            ❌ Hủy
          </button>
        </RouterLink>

        <button class="btn">
          💾 Lưu bệnh nhân
        </button>

      </div>

    </div>

  </div>
</template>
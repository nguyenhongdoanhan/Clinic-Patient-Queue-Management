<template>
  <div class="container fade">

    <div class="flex-between" style="margin-bottom:25px;">

      <h1 class="page-title">💊 Kê đơn thuốc</h1>

      <RouterLink to="/bac-si/ket-qua">
        <button class="btn">
          ← Quay lại
        </button>
      </RouterLink>

    </div>

    <div class="card">

      <div class="group">
        <label>Mã bệnh nhân</label>
        <input type="text" value="BN001" readonly>
      </div>

      <div class="group">
        <label>Họ và tên</label>
        <input type="text" value="Nguyễn Văn A" readonly>
      </div>

      <div class="group">
        <label>Tên thuốc</label>
        <input
          type="text"
          placeholder="Ví dụ: Paracetamol 500mg"
        >
      </div>

      <div
        style="
          display:grid;
          grid-template-columns:repeat(2,1fr);
          gap:20px;
        "
      >

        <div class="group">
          <label>Số lượng</label>
          <input
            type="number"
            placeholder="Nhập số lượng"
          >
        </div>

        <div class="group">
          <label>Số ngày sử dụng</label>
          <input
            type="number"
            placeholder="Nhập số ngày"
          >
        </div>

      </div>

      <div class="group">
        <label>Cách dùng</label>
        <textarea
          rows="4"
          placeholder="Ví dụ: Uống 2 viên/ngày sau khi ăn"
        ></textarea>
      </div>

      <div class="group">
        <label>Ghi chú</label>
        <textarea
          rows="3"
          placeholder="Nhập ghi chú nếu có"
        ></textarea>
      </div>

      <div
        style="
          display:flex;
          justify-content:flex-end;
          gap:15px;
          margin-top:25px;
          flex-wrap:wrap;
        "
      >

        <RouterLink to="/bac-si/ket-qua">
          <button class="btn">
            📄 Sửa kết quả
          </button>
        </RouterLink>

        <RouterLink to="/bac-si/hoan-thanh">
          <button class="btn">
            💾 Lưu đơn thuốc
          </button>
        </RouterLink>

      </div>

    </div>
//
  </div>
</template>
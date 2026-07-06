<template>
  <div class="container fade">

    <div class="flex-between" style="margin-bottom:25px;">

      <h1 class="page-title">🩺 Chẩn đoán bệnh nhân</h1>

      <RouterLink to="/bac-si/danh-sach">
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
        <label>Triệu chứng</label>
        <textarea
          rows="4"
          placeholder="Ví dụ: Sốt cao, ho, đau họng..."
        ></textarea>
      </div>

      <div class="group">
        <label>Chẩn đoán</label>
        <textarea
          rows="4"
          placeholder="Ví dụ: Viêm họng cấp"
        ></textarea>
      </div>

      <div class="group">
        <label>Hướng điều trị</label>
        <textarea
          rows="3"
          placeholder="Nhập hướng điều trị"
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
            📄 Lưu & nhập kết quả
          </button>
        </RouterLink>

      </div>

    </div>

  </div>
</template>
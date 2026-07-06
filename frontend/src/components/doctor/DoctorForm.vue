<template>

  <div class="modal-backdrop-custom">

    <div class="modal-container">

      <div class="modal-header">

        <h4>

          {{ doctorData.id ? "Cập nhật bác sĩ" : "Thêm bác sĩ" }}

        </h4>

        <button
          class="btn-close"
          @click="$emit('close')"
        ></button>

      </div>

      <div class="modal-body">

        <div class="mb-3">

          <label class="form-label">

            Họ và tên

          </label>

          <input
            type="text"
            class="form-control"
            v-model="doctorData.name"
          >

        </div>

        <div class="mb-3">

          <label class="form-label">

            Chuyên khoa

          </label>

          <select
            class="form-select"
            v-model="doctorData.specialty"
          >

            <option value="">-- Chọn chuyên khoa --</option>

            <option>Tim mạch</option>

            <option>Nội tổng quát</option>

            <option>Ngoại tổng quát</option>

            <option>Nhi khoa</option>

            <option>Da liễu</option>

            <option>Tai Mũi Họng</option>

            <option>Răng Hàm Mặt</option>

          </select>

        </div>

        <div class="mb-3">

          <label class="form-label">

            Số điện thoại

          </label>

          <input
            type="text"
            class="form-control"
            v-model="doctorData.phone"
          >

        </div>

        <div class="mb-3">

          <label class="form-label">

            Email

          </label>

          <input
            type="email"
            class="form-control"
            v-model="doctorData.email"
          >

        </div>

        <div class="mb-3">

          <label class="form-label">

            Trạng thái

          </label>

          <select
            class="form-select"
            v-model="doctorData.status"
          >

            <option>Đang làm việc</option>

            <option>Nghỉ</option>

          </select>

        </div>

      </div>

      <div class="modal-footer">

        <button
          class="btn btn-secondary"
          @click="$emit('close')"
        >

          Hủy

        </button>

        <button
          class="btn btn-primary"
          @click="save"
        >

          {{ doctorData.id ? "Cập nhật" : "Thêm mới" }}

        </button>

      </div>

    </div>

  </div>

</template>

<script setup>

import { ref, watch } from "vue"

const props = defineProps({

  doctor: Object

})

const emit = defineEmits([

  "close",

  "save"

])

const doctorData = ref({

  id: null,

  name: "",

  specialty: "",

  phone: "",

  email: "",

  status: "Đang làm việc"

})

watch(

  () => props.doctor,

  (value) => {

    if (value) {

      doctorData.value = { ...value }

    } else {

      doctorData.value = {

        id: null,

        name: "",

        specialty: "",

        phone: "",

        email: "",

        status: "Đang làm việc"

      }

    }

  },

  { immediate: true }

)

const save = () => {

  emit("save", { ...doctorData.value })

  emit("close")

}

</script>

<style scoped>

.modal-backdrop-custom{

position:fixed;

top:0;

left:0;

right:0;

bottom:0;

background:rgba(0,0,0,.45);

display:flex;

justify-content:center;

align-items:center;

z-index:9999;

}

.modal-container{

width:550px;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 30px rgba(0,0,0,.25);

}

.modal-header{

padding:20px;

background:#0d6efd;

color:white;

display:flex;

justify-content:space-between;

align-items:center;

}

.modal-body{

padding:20px;

}

.modal-footer{

padding:20px;

display:flex;

justify-content:flex-end;

gap:10px;

border-top:1px solid #eee;

}

</style>
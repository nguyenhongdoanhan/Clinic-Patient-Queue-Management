<template>

  <div class="modal-backdrop-custom">

    <div class="modal-container">

      <div class="modal-header">

        <h4>

          {{ appointmentData.id ? "Cập nhật lịch khám" : "Đặt lịch khám" }}

        </h4>

        <button
          class="btn-close"
          @click="$emit('close')"
        ></button>

      </div>

      <div class="modal-body">

        <!-- Bệnh nhân -->

        <div class="mb-3">

          <label class="form-label">

            Bệnh nhân

          </label>

          <input
            class="form-control"
            v-model="appointmentData.patient"
            placeholder="Nhập tên bệnh nhân"
          >

        </div>

        <!-- Bác sĩ -->

        <div class="mb-3">

          <label class="form-label">

            Bác sĩ

          </label>

          <input
            class="form-control"
            v-model="appointmentData.doctor"
            placeholder="Nhập tên bác sĩ"
          >

        </div>

        <!-- Ngày khám -->

        <div class="mb-3">

          <label class="form-label">

            Ngày khám

          </label>

          <input
            type="date"
            class="form-control"
            v-model="appointmentData.date"
          >

        </div>

        <!-- Giờ khám -->

        <div class="mb-3">

          <label class="form-label">

            Giờ khám

          </label>

          <input
            type="time"
            class="form-control"
            v-model="appointmentData.time"
          >

        </div>

        <!-- Trạng thái -->

        <div class="mb-3">

          <label class="form-label">

            Trạng thái

          </label>

          <select
            class="form-select"
            v-model="appointmentData.status"
          >

            <option>Đã đặt</option>

            <option>Đã khám</option>

            <option>Đã hủy</option>

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

          {{ appointmentData.id ? "Cập nhật" : "Đặt lịch" }}

        </button>

      </div>

    </div>

  </div>

</template>

<script setup>

import { ref, watch } from "vue"

const props = defineProps({

    appointment: Object

})

const emit = defineEmits([

    "close",

    "save"

])

const appointmentData = ref({

    id: null,

    patient: "",

    doctor: "",

    date: "",

    time: "",

    status: "Đã đặt"

})

watch(

    () => props.appointment,

    (value) => {

        if (value) {

            appointmentData.value = { ...value }

        } else {

            appointmentData.value = {

                id: null,

                patient: "",

                doctor: "",

                date: "",

                time: "",

                status: "Đã đặt"

            }

        }

    },

    {

        immediate: true

    }

)

const save = () => {

    emit("save", { ...appointmentData.value })

    emit("close")

}

</script>

<style scoped>

.modal-backdrop-custom{

position:fixed;

left:0;

top:0;

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

background:#0d6efd;

color:white;

padding:18px 22px;

display:flex;

justify-content:space-between;

align-items:center;

}

.modal-body{

padding:22px;

}

.modal-footer{

padding:20px;

display:flex;

justify-content:flex-end;

gap:10px;

border-top:1px solid #eee;

}

</style>
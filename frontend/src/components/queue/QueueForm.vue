<template>

  <div class="modal-backdrop-custom">

    <div class="modal-container">

      <div class="modal-header">

        <h4>

          {{ queueData.id ? "Cập nhật hàng đợi" : "Thêm hàng đợi" }}

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
            v-model="queueData.patient"
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
            v-model="queueData.doctor"
            placeholder="Nhập tên bác sĩ"
          >

        </div>

        <!-- Phòng -->

        <div class="mb-3">

          <label class="form-label">

            Phòng khám

          </label>

          <input
            class="form-control"
            v-model="queueData.room"
            placeholder="Ví dụ: P101"
          >

        </div>

        <!-- Trạng thái -->

        <div class="mb-3">

          <label class="form-label">

            Trạng thái

          </label>

          <select
            class="form-select"
            v-model="queueData.status"
          >

            <option>Đang chờ</option>

            <option>Đang khám</option>

            <option>Đã hoàn thành</option>

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

          {{ queueData.id ? "Cập nhật" : "Thêm mới" }}

        </button>

      </div>

    </div>

  </div>

</template>

<script setup>

import { ref, watch } from "vue"

const props = defineProps({

    queue:Object

})

const emit = defineEmits([

    "close",

    "save"

])

const queueData = ref({

    id:null,

    number:"",

    patient:"",

    doctor:"",

    room:"",

    status:"Đang chờ"

})

watch(

    ()=>props.queue,

    (value)=>{

        if(value){

            queueData.value={...value}

        }else{

            queueData.value={

                id:null,

                number:"",

                patient:"",

                doctor:"",

                room:"",

                status:"Đang chờ"

            }

        }

    },

    {

        immediate:true

    }

)

function save(){

    emit("save",{...queueData.value})

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

padding:20px;

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
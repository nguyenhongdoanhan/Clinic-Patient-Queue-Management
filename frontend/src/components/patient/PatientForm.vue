<template>

  <div class="modal-backdrop-custom">

    <div class="modal-container">

      <div class="modal-header">

        <h4>

          {{ patientData.id ? "Cập nhật bệnh nhân" : "Thêm bệnh nhân" }}

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
            class="form-control"
            v-model="patientData.name"
          >

        </div>

        <div class="mb-3">

          <label class="form-label">

            Giới tính

          </label>

          <select
            class="form-select"
            v-model="patientData.gender"
          >

            <option>Nam</option>

            <option>Nữ</option>

          </select>

        </div>

        <div class="mb-3">

          <label class="form-label">

            Ngày sinh

          </label>

          <input
            type="date"
            class="form-control"
            v-model="patientData.birthday"
          >

        </div>

        <div class="mb-3">

          <label class="form-label">

            Số điện thoại

          </label>

          <input
            class="form-control"
            v-model="patientData.phone"
          >

        </div>

        <div class="mb-3">

          <label class="form-label">

            Địa chỉ

          </label>

          <textarea
            class="form-control"
            rows="3"
            v-model="patientData.address"
          ></textarea>

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

          {{ patientData.id ? "Cập nhật" : "Thêm mới" }}

        </button>

      </div>

    </div>

  </div>

</template>

<script setup>

import { ref, watch } from "vue"

const props = defineProps({

patient:Object

})

const emit = defineEmits([

"close",

"save"

])

const patientData = ref({

id:null,

name:"",

gender:"Nam",

birthday:"",

phone:"",

address:""

})

watch(

()=>props.patient,

(value)=>{

if(value){

patientData.value={...value}

}else{

patientData.value={

id:null,

name:"",

gender:"Nam",

birthday:"",

phone:"",

address:""

}

}

},

{immediate:true}

)

const save=()=>{

emit("save",{...patientData.value})

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

box-shadow:0 10px 30px rgba(0,0,0,.2);

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
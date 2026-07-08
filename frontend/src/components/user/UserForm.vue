<template>
  <div
    v-if="show"
    class="modal fade show d-block"
    tabindex="-1"
    style="background: rgba(0,0,0,.5)"
  >
    <div class="modal-dialog modal-lg">
      <div class="modal-content">

        <!-- Header -->
        <div class="modal-header bg-primary text-white">
          <h5 class="modal-title">
            <i class="bi bi-person-fill me-2"></i>

            {{ isEdit ? "Cập nhật người dùng" : "Thêm người dùng" }}

          </h5>

          <button
            class="btn-close btn-close-white"
            @click="$emit('close')"
          ></button>

        </div>

        <!-- Body -->

        <div class="modal-body">

          <div class="row">

            <div class="col-md-6 mb-3">

              <label class="form-label">

                Họ tên

              </label>

              <input
                type="text"
                class="form-control"
                v-model="form.name"
              >

            </div>

            <div class="col-md-6 mb-3">

              <label class="form-label">

                Email

              </label>

              <input
                type="email"
                class="form-control"
                v-model="form.email"
              >

            </div>

            <div
              class="col-md-6 mb-3"
              v-if="!isEdit"
            >

              <label class="form-label">

                Mật khẩu

              </label>

              <input
                type="password"
                class="form-control"
                v-model="form.password"
              >

            </div>

            <div class="col-md-6 mb-3">

              <label class="form-label">

                Vai trò

              </label>

              <select
                class="form-select"
                v-model="form.role"
              >

                <option>Admin</option>

                <option>Bác sĩ</option>

                <option>Lễ tân</option>

                <option>Bệnh nhân</option>

              </select>

            </div>

            <div class="col-md-6">

              <label class="form-label">

                Trạng thái

              </label>

              <select
                class="form-select"
                v-model="form.status"
              >

                <option>Hoạt động</option>

                <option>Khóa</option>

              </select>

            </div>

          </div>

        </div>

        <!-- Footer -->

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

            <i class="bi bi-check-circle me-1"></i>

            Lưu

          </button>

        </div>

      </div>

    </div>

  </div>
</template>

<script setup>

import { reactive, watch } from "vue"

const props = defineProps({

  show:Boolean,

  isEdit:Boolean,

  userData:Object

})

const emit = defineEmits([

  "close",

  "save"

])

const form = reactive({

  id:null,

  name:"",

  email:"",

  password:"",

  role:"Admin",

  status:"Hoạt động"

})

watch(

()=>props.userData,

(value)=>{

if(value){

Object.assign(form,value)

}
else{

form.id=null
form.name=""
form.email=""
form.password=""
form.role="Admin"
form.status="Hoạt động"

}

},

{immediate:true}

)

function save(){

emit("save",{...form})

}

</script>

<style scoped>

.modal-content{

border-radius:15px;

}

.form-control,

.form-select{

height:45px;

}

.modal-header{

border-top-left-radius:15px;

border-top-right-radius:15px;

}

</style>
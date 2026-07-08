<template>

  <div class="modal-backdrop-custom">

    <div class="modal-container">

      <div class="modal-header bg-danger text-white">

        <h5>Xác nhận xóa bác sĩ</h5>

      </div>

      <div class="modal-body">

        <p>

          Bạn có chắc chắn muốn xóa bác sĩ

          <strong>{{ doctor?.name }}</strong>

          không?

        </p>

        <p class="text-danger mb-0">

          Hành động này không thể hoàn tác.

        </p>

      </div>

      <div class="modal-footer">

        <button
          class="btn btn-secondary"
          @click="$emit('close')"
        >
          Hủy
        </button>

        <button
          class="btn btn-danger"
          @click="confirmDelete"
        >
          Xóa
        </button>

      </div>

    </div>

  </div>

</template>

<script setup>

const props = defineProps({

  doctor:Object

})

const emit = defineEmits([

"close",

"delete"

])

const confirmDelete=()=>{

emit("delete",props.doctor)

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

width:430px;

background:white;

border-radius:12px;

overflow:hidden;

box-shadow:0 10px 25px rgba(0,0,0,.25);

}

.modal-header{

padding:18px;

}

.modal-body{

padding:20px;

font-size:16px;

}

.modal-footer{

padding:18px;

display:flex;

justify-content:flex-end;

gap:10px;

border-top:1px solid #eee;

}

</style>
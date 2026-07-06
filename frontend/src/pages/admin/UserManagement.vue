<template>

  <AdminSidebar />

  <AdminNavbar />

  <div class="content">

    <!-- Tiêu đề -->

    <div class="d-flex justify-content-between align-items-center mb-4">

      <div>

        <h2 class="fw-bold">

          Quản lý người dùng

        </h2>

        <p class="text-secondary">

          Quản lý tài khoản trong hệ thống

        </p>

      </div>

      <button
        class="btn btn-primary"
        @click="showModal = true"
      >

        <i class="bi bi-plus-circle me-2"></i>

        Thêm người dùng

      </button>

    </div>

    <!-- Thanh tìm kiếm -->

    <div class="card shadow-sm mb-4">

      <div class="card-body">

        <input
          type="text"
          class="form-control"
          placeholder="Tìm kiếm theo họ tên hoặc email..."
          v-model="search"
        />

      </div>

    </div>

    <!-- Danh sách -->

    <div class="card shadow-sm">

      <div class="card-body p-0">

        <table class="table table-hover mb-0">

          <thead class="table-primary">

            <tr>

              <th>ID</th>

              <th>Họ tên</th>

              <th>Email</th>

              <th>Vai trò</th>

              <th>Trạng thái</th>

              <th class="text-center">

                Thao tác

              </th>

            </tr>

          </thead>

          <tbody>

            <tr
              v-for="user in filteredUsers"
              :key="user.id"
            >

              <td>

                {{ user.id }}

              </td>

              <td>

                {{ user.name }}

              </td>

              <td>

                {{ user.email }}

              </td>

              <td>

                <span
                  class="badge"
                  :class="{

                  'bg-danger':user.role==='Admin',

                  'bg-primary':user.role==='Bác sĩ',

                  'bg-warning text-dark':user.role==='Lễ tân',

                  'bg-info':user.role==='Bệnh nhân'

                  }"
                >

                  {{ user.role }}

                </span>

              </td>

              <td>

                <span
                  class="badge"
                  :class="user.status==='Hoạt động'
                  ?'bg-success'
                  :'bg-secondary'"
                >

                  {{ user.status }}

                </span>

              </td>

              <td class="text-center">

                <button
                  class="btn btn-warning btn-sm me-2"
                  @click="editUser(user)"
                >

                  <i class="bi bi-pencil"></i>

                </button>

                <button
                  class="btn btn-danger btn-sm"
                  @click="deleteUser(user.id)"
                >

                  <i class="bi bi-trash"></i>

                </button>

              </td>

            </tr>

          </tbody>

        </table>

      </div>

    </div>

  </div>

  <!-- Popup -->

  <UserForm

    :show="showModal"

    :isEdit="isEdit"

    :userData="selectedUser"

    @close="closeModal"

    @save="saveUser"

  />

</template>

<script setup>

import { ref, computed } from "vue"

import AdminSidebar from "../../components/layout/AdminSidebar.vue"

import AdminNavbar from "../../components/layout/AdminNavbar.vue"

import UserForm from "../../components/user/UserForm.vue"

const showModal = ref(false)

const isEdit = ref(false)

const search = ref("")

const selectedUser = ref(null)

const users = ref([

{

id:1,

name:"Nguyễn Văn A",

email:"admin@gmail.com",

role:"Admin",

status:"Hoạt động"

},

{

id:2,

name:"Trần Thị B",

email:"doctor@gmail.com",

role:"Bác sĩ",

status:"Hoạt động"

},

{

id:3,

name:"Lê Văn C",

email:"patient@gmail.com",

role:"Bệnh nhân",

status:"Khóa"

}

])

const filteredUsers = computed(()=>{

return users.value.filter(user=>

user.name.toLowerCase().includes(search.value.toLowerCase())

||

user.email.toLowerCase().includes(search.value.toLowerCase())

)

})

function saveUser(user){

if(isEdit.value){

const index = users.value.findIndex(

u=>u.id===user.id

)

users.value[index]=user

}

else{

user.id = users.value.length + 1

users.value.push(user)

}

closeModal()

}
function editUser(user){

  selectedUser.value = { ...user }

  isEdit.value = true

  showModal.value = true

}

function deleteUser(id){

  if(confirm("Bạn có chắc muốn xóa người dùng này?")){

    users.value = users.value.filter(

      user => user.id !== id

    )

  }

}

function closeModal(){

  showModal.value = false

  isEdit.value = false

  selectedUser.value = null

}

</script>

<style scoped>

.content{

  margin-left:260px;

  margin-top:75px;

  padding:30px;

  background:#f4f6f9;

  min-height:100vh;

}

.card{

  border:none;

  border-radius:15px;

  overflow:hidden;

}

.card-body{

  padding:20px;

}

.table{

  margin-bottom:0;

}

.table th{

  text-align:center;

  vertical-align:middle;

  font-weight:bold;

  font-size:15px;

}

.table td{

  vertical-align:middle;

}

.table tbody tr{

  transition:.25s;

}

.table tbody tr:hover{

  background:#f8fbff;

}

.btn{

  border-radius:8px;

}

.btn-primary{

  font-weight:600;

}

.btn-warning{

  color:white;

}

.badge{

  padding:8px 12px;

  font-size:13px;

}

.form-control{

  height:45px;

  border-radius:10px;

}

h2{

  color:#0d6efd;

}

.text-secondary{

  margin-bottom:0;

}

@media(max-width:992px){

.content{

margin-left:0;

padding:20px;

margin-top:70px;

}

}

</style>
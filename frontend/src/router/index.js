import { createRouter, createWebHistory } from "vue-router";

import Login from "../pages/login/Login.vue";
import Register from "../pages/register/Register.vue";
import Dashboard from "../pages/admin/Dashboard.vue";
import UserManagement from "../pages/admin/UserManagement.vue";
import DoctorManagement from "../pages/admin/DoctorManagement.vue"
import PatientManagement from "../pages/admin/PatientManagement.vue"
import AppointmentManagement from "../pages/admin/AppointmentManagement.vue"
import QueueManagement from "../pages/admin/QueueManagement.vue"


const routes = [
  {
    path: "/",
    redirect: "/login",
  },

  {
    path: "/login",
    name: "Login",
    component: Login,
  },

  {
    path: "/register",
    name: "Register",
    component: Register,
  },

  {
    path: "/admin/dashboard",
    name: "AdminDashboard",
    component: Dashboard,
  },

  {
    path: "/admin/users",
    name: "UserManagement",
    component: UserManagement,
  },
  {
    path: "/admin/doctors",
    name: "DoctorManagement",
    component: DoctorManagement
},
{
    path: "/admin/patients",
    name: "PatientManagement",
    component: PatientManagement
},
{
    path: "/admin/appointments",
    name: "AppointmentManagement",
    component: AppointmentManagement
},
{
    path: "/admin/queue",
    name: "QueueManagement",
    component: QueueManagement
},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
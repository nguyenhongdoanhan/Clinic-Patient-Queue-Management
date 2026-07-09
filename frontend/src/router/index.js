import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "../stores/auth";

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
    meta: { requiresGuest: true },
  },

  {
    path: "/register",
    name: "Register",
    component: Register,
    meta: { requiresGuest: true },
  },

  {
    path: "/admin/dashboard",
    name: "AdminDashboard",
    component: Dashboard,
    meta: { requiresAuth: true },
  },

  {
    path: "/admin/users",
    name: "UserManagement",
    component: UserManagement,
    meta: { requiresAuth: true },
  },
  {
    path: "/admin/doctors",
    name: "DoctorManagement",
    component: DoctorManagement,
    meta: { requiresAuth: true },
},
{
    path: "/admin/patients",
    name: "PatientManagement",
    component: PatientManagement,
    meta: { requiresAuth: true },
},
{
    path: "/admin/appointments",
    name: "AppointmentManagement",
    component: AppointmentManagement,
    meta: { requiresAuth: true },
},
{
    path: "/admin/queue",
    name: "QueueManagement",
    component: QueueManagement,
    meta: { requiresAuth: true },
},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Route guard: chặn truy cập /admin/* khi chưa đăng nhập,
// và chặn quay lại /login, /register khi đã đăng nhập rồi
router.beforeEach((to) => {
  const authStore = useAuthStore();

  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    return { name: "Login", query: { redirect: to.fullPath } };
  }

  if (to.meta.requiresGuest && authStore.isAuthenticated) {
    return { name: "AdminDashboard" };
  }

  return true;
});

export default router;

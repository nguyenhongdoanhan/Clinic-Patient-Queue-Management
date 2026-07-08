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
    meta: { requiresAuth: true }
  },

  {
    path: "/admin/users",
    name: "UserManagement",
    component: UserManagement,
    meta: { requiresAuth: true }
  },
  {
    path: "/admin/doctors",
    name: "DoctorManagement",
    component: DoctorManagement,
    meta: { requiresAuth: true }
},
{
    path: "/admin/patients",
    name: "PatientManagement",
    component: PatientManagement,
    meta: { requiresAuth: true }
},
{
    path: "/admin/appointments",
    name: "AppointmentManagement",
    component: AppointmentManagement,
    meta: { requiresAuth: true }
},
{
    path: "/admin/queue",
    name: "QueueManagement",
    component: QueueManagement,
    meta: { requiresAuth: true }
},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Route Guard
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  
  const isAuthenticated = authStore.isAuthenticated;
  const requiresAuth = to.meta.requiresAuth;
  
  console.log(`Navigating to ${to.path}`, {
    isAuthenticated,
    requiresAuth,
    token: !!localStorage.getItem('access_token')
  });
  
  // Nếu route yêu cầu auth nhưng không authenticated
  if (requiresAuth && !isAuthenticated) {
    console.log('Redirecting to login - no token');
    next('/login');
  } 
  // Nếu đã authenticated mà đi tới login/register
  else if (!requiresAuth && (to.path === '/login' || to.path === '/register') && isAuthenticated) {
    console.log('Redirecting to dashboard - already logged in');
    next('/admin/dashboard');
  } 
  // Cho phép điều hướng bình thường
  else {
    next();
  }
});

export default router;
import { createRouter, createWebHistory } from "vue-router";
import LoginAdmin from "../modules/admin/login-admin/LoginAdmin.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      redirect: "/admin/login",
    },
    {
      path: "/admin/login",
      component: LoginAdmin,
    },
  ],
});

export default router;
import { createRouter, createWebHistory } from "vue-router";

// ================= HOME =================
import Home from "../modules/Home.vue";

// ================= ADMIN =================
import LoginAdmin from "../modules/admin/login-admin/LoginAdmin.vue";

// ================= PATIENT =================
import DashboardPatient from "../modules/patient/Dashboard.vue";
import HoSo from "../modules/patient/HoSo.vue";
import CapNhatHoSo from "../modules/patient/CapNhatHoSo.vue";
import DatLichKham from "../modules/patient/DatLichKham.vue";
import LichKham from "../modules/patient/LichKham.vue";
import LichSuKham from "../modules/patient/LichSuKham.vue";
import TheoDoiHangDoi from "../modules/patient/TheoDoiHangDoi.vue";

// ================= RECEPTIONIST =================
import DashboardReceptionist from "../modules/receptionist/Dashboard.vue";
import QuanLyBenhNhan from "../modules/receptionist/QuanLyBenhNhan.vue";
import ThemBenhNhan from "../modules/receptionist/ThemBenhNhan.vue";
import SuaBenhNhan from "../modules/receptionist/SuaBenhNhan.vue";
import QuanLyLichKham from "../modules/receptionist/QuanLyLichKham.vue";
import QuanLyHangDoi from "../modules/receptionist/QuanLyHangDoi.vue";

// ================= DOCTOR =================
import DashboardDoctor from "../modules/doctor/Dashboard.vue";
import DanhSachBenhNhan from "../modules/doctor/DanhSachBenhNhan.vue";
import HoSoBenhNhan from "../modules/doctor/HoSoBenhNhan.vue";
import ChanDoan from "../modules/doctor/ChanDoan.vue";
import KetQuaKham from "../modules/doctor/KetQuaKham.vue";
import KeDonThuoc from "../modules/doctor/KeDonThuoc.vue";
import HoanThanhCaKham from "../modules/doctor/HoanThanhCaKham.vue";

const routes = [

  // ================= HOME =================
  {
    path: "/",
    component: Home,
  },

  // ================= ADMIN =================
  {
    path: "/admin/login",
    name: "LoginAdmin",
    component: LoginAdmin,
  },

  // ================= PATIENT =================
  {
    path: "/benh-nhan",
    component: DashboardPatient,
  },
  {
    path: "/benh-nhan/ho-so",
    component: HoSo,
  },
  {
    path: "/benh-nhan/cap-nhat-ho-so",
    component: CapNhatHoSo,
  },
  {
    path: "/benh-nhan/dat-lich",
    component: DatLichKham,
  },
  {
    path: "/benh-nhan/lich-kham",
    component: LichKham,
  },
  {
    path: "/benh-nhan/lich-su",
    component: LichSuKham,
  },
  {
    path: "/benh-nhan/hang-doi",
    component: TheoDoiHangDoi,
  },

  // ================= RECEPTIONIST =================
  {
    path: "/le-tan",
    component: DashboardReceptionist,
  },
  {
    path: "/le-tan/benh-nhan",
    component: QuanLyBenhNhan,
  },
  {
    path: "/le-tan/them-benh-nhan",
    component: ThemBenhNhan,
  },
  {
    path: "/le-tan/sua-benh-nhan",
    component: SuaBenhNhan,
  },
  {
    path: "/le-tan/lich-kham",
    component: QuanLyLichKham,
  },
  {
    path: "/le-tan/hang-doi",
    component: QuanLyHangDoi,
  },

  // ================= DOCTOR =================
  {
    path: "/bac-si",
    component: DashboardDoctor,
  },
  {
    path: "/bac-si/danh-sach",
    component: DanhSachBenhNhan,
  },
  {
    path: "/bac-si/ho-so",
    component: HoSoBenhNhan,
  },
  {
    path: "/bac-si/chan-doan",
    component: ChanDoan,
  },
  {
    path: "/bac-si/ket-qua",
    component: KetQuaKham,
  },
  {
    path: "/bac-si/ke-don",
    component: KeDonThuoc,
  },
  {
    path: "/bac-si/hoan-thanh",
    component: HoanThanhCaKham,
  },

  // ================= 404 =================
  {
    path: "/:pathMatch(.*)*",
    redirect: "/",
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
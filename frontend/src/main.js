import { createApp } from "vue";
import App from "./App.vue";
import router from "./router/router.js";

// CSS dùng chung cho toàn bộ hệ thống
import "./assets/css/main.css";

createApp(App)
  .use(router)
  .mount("#app");
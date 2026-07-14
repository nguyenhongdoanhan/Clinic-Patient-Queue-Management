import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import router from "./router/router.js";

// CSS dùng chung cho toàn bộ hệ thống
import "./assets/css/main.css";

const app = createApp(App);
app.use(createPinia());
app.use(router);
app.mount("#app");
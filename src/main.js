import Vue from "vue";
import "./plugins/vuetify";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "@/plugins/vuetify";
import layout from "@/components/Layout.vue";
import sidebar from "@/components/sidebar";
import postCard from "@/components/card";
import comment from "@/components/comment";
Vue.component("a-layout", layout);
Vue.component("sidebar", sidebar);
Vue.component("postCard", postCard);
Vue.component("comment", comment);
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App)
}).$mount("#app");

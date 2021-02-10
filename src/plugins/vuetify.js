import Vue from "vue";
import Vuetify from "vuetify/lib";
import "@mdi/font/css/materialdesignicons.css";
Vue.use(Vuetify);

export default new Vuetify({
  rtl: true,
  iconfont: "mdi",
  theme: {
    dark: false,
    themes: {
      dark: {
        accent: "#00b8ff"
      }
    }
  }
});

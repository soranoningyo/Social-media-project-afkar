import Vue from "vue";
import Vuex from "vuex";
import essays from "./views/essays.json";
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    category: null,
    essays,
    user: {
      username: null,
      password: null,
      email: null,
      birth_date: null,
      gender: null,
      country: null,
      mbti: null
    },
    userdata: null
  },
  mutations: {
    setCategoryActive(state, n) {
      state.category = n;
    },
    CurrentUser(state, user) {
      state.user = user;
    },
    userData(state, data) {
      state.userdata = data;
    }
  },
  actions: {},
  getters: {
    retUserData: (state) => {
      return state.userdata;
    }
  }
});

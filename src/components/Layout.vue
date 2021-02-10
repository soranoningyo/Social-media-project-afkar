<template>
  <div>
    <v-navigation-drawer v-model="drawer" fixed clipped right app>
      <v-list-item to="/profile">
        <v-list-item-avatar class="ml-3 mr-0">
          <img
            src="https://i.ytimg.com/vi/ktlQrO2Sifg/maxresdefault.jpg"
            alt=""
          />
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title class="title">علي محمد</v-list-item-title>
          <v-list-item-subtitle>100 نقطة</v-list-item-subtitle>
          <v-list-item-subtitle></v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-expansion-panels accordion style="padding-left:1px;">
        <v-expansion-panel v-for="(item, i) in 5" :key="i">
          <v-expansion-panel-header>Item</v-expansion-panel-header>
          <v-expansion-panel-content>
            . Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
            nisi ut aliquip ex ea commodo consequat.
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-navigation-drawer>
    <v-app-bar color="blue" dense fixed dark clipped-right app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title class="mr-1 align-center">
        <router-link to="/" tag="span" class="title"> افكار </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon @click="night" v-show="this.$vuetify.theme.dark == false">
        <v-icon>mdi-weather-night</v-icon>
      </v-btn>
      <v-btn icon @click="sun" v-show="this.$vuetify.theme.dark == true">
        <v-icon>mdi-white-balance-sunny</v-icon>
      </v-btn>
      <v-chip color="blue lighten-1" class="mx-2" to="/login">
        دخول
        <v-icon right>mdi-login-variant</v-icon>
      </v-chip>
      <v-chip color="blue lighten-1" to="/register">
        تسجيل
        <v-icon right>mdi-square-edit-outline</v-icon>
      </v-chip>
      <v-chip color="blue lighten-1" @click="logout">
        خروج
        <v-icon right>mdi-square-edit-outline</v-icon>
      </v-chip>
    </v-app-bar>
    <v-bottom-navigation :value="activeBtn" grow color="blue" fixed>
      <v-btn max-width="275" @click="setActive(0)">
        <span>مقالات</span>
        <v-icon>mdi-book</v-icon>
      </v-btn>

      <v-btn max-width="275" @click="setActive(1)">
        <span>نقاشات</span>
        <v-icon>mdi-forum</v-icon>
      </v-btn>

      <v-btn max-width="275" @click="setActive(2)">
        <span>غرفة حوار</span>
        <v-icon>mdi-account-multiple-outline</v-icon>
      </v-btn>
    </v-bottom-navigation>
  </div>
</template>

<script>
import axios from "axios";
export default {
  computed: {
    activeBtn: function() {
      return this.$store.state.category;
    }
  },
  data: () => ({
    drawer: false,
    items: [
      { title: "Dashboard", icon: "mdi-view-dashboard" },
      { title: "Photos", icon: "mdi-image" },
      { title: "About", icon: "mdi-help-box" }
    ]
  }),
  methods: {
    night() {
      this.$vuetify.theme.dark = true;
    },
    sun() {
      this.$vuetify.theme.dark = false;
    },
    logout() {
      function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== "") {
          var cookies = document.cookie.split(";");
          for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === name + "=") {
              cookieValue = decodeURIComponent(
                cookie.substring(name.length + 1)
              );
              break;
            }
          }
        }
        return cookieValue;
      }
      var csrftoken = getCookie("csrftoken");
      // let csrftoken = Cookies.get("csrftoken");
      let headers = {
        "X-CSRFToken": csrftoken
      };
      axios
        .post("logout/", {}, { headers: headers })
        .then(function(response) {
          console.log(response);
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    setActive(n) {
      this.$store.commit("setCategoryActive", n);
      switch (this.activeBtn) {
        case 0:
          console.log(0);
          // this.$router.push({path:"/post"})
          break;
        case 1:
          console.log(1);
          break;
        default:
          console.log(2);
          break;
      }
    }
  }
};
</script>

<template>
  <v-app id="inspire">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md5>
            <v-card class="elevation-12">
              <v-toolbar color="primary" dark flat>
                <v-toolbar-title style="overflow:initial"
                  >تسجيل الدخول</v-toolbar-title
                >
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field
                    label="البريد الالكتروني"
                    name="login"
                    prepend-icon="person"
                    type="text"
                    class="rightIt"
                    v-model="email"
                  ></v-text-field>

                  <v-text-field
                    id="password"
                    label="كلمة السر"
                    name="password"
                    prepend-icon="lock"
                    type="password"
                    class="rightIt"
                    v-model="password"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-switch
                  class="mr-3"
                  v-model="remember"
                  color="primary"
                  label="تذكرني"
                />
                <v-spacer></v-spacer>
                <v-btn
                  class="ml-2"
                  @click="login"
                  hide-details
                  hint="false"
                  color="primary"
                  >دخول</v-btn
                >
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import axios from "axios";
export default {
  props: {
    source: String
  },
  data: () => ({
    email: "",
    password: "",
    remember: null
  }),
  methods: {
    login() {
      const t = this;
      axios
        .post("login/", {
          email: this.email,
          password: this.password
        })
        .then(function(response) {
          console.log(response);
          t.$router.push({ path: "/" });
          t.$store.commit("userData", response.data);
          console.log(response.data);
          console.log(t.$store.getters.retUserData);
        })
        .catch(function(error) {
          console.log(error);
        });
    }
  }
};
</script>
<style>
.rightIt label.v-label {
  right: 10px !important;
}
</style>

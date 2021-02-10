<template>
  <v-app id="inspire">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md5>
            <v-card>
              <v-card-title
                style="color:white"
                class=" blue title font-weight-regular justify-space-between"
              >
                <span>{{ currentTitle }}</span>
                <span class="ml-3" v-text="step" v-show="step !== 0" />
              </v-card-title>

              <v-window v-model="step">
                <!-- <v-window-item :value="0">
                  <v-card-text>
                    <p class="headline">انشئ حسابًا في أفكار وأنشر معرفتك !</p>
                    <span class="subtitle-1 text-xs-center d-block">يمكنك التسجيل بواسطة </span>
                    <v-btn dark class="my-2 mx-auto d-block px-5" color="blue">
                      facebook
                      <v-icon right>mdi-facebook-box</v-icon> 
                    </v-btn>
                    <v-divider :class="['my-4' ,'mx-auto','hr-or',this.$vuetify.theme.dark == true? 'hr-or-dark': '']"  style="position:relative;max-width:70%"/>
                    <v-btn dark class="my-2 mx-auto d-block px-5" color="red">
                      google
                      <v-icon right>mdi-google</v-icon> 
                    </v-btn>
                    <v-divider :class="['my-4' ,'hr-or',this.$vuetify.theme.dark == true? 'hr-or-dark': '']" style="position:relative;"/>
                    <p class="headline text-xs-center" >أنشئ حسابك بالضغط على التالي</p>
                  </v-card-text>
                </v-window-item> -->
                <v-window-item :value="0">
                  <v-card-text>
                    <v-text-field label="أسم المستخدم" v-model="user.name" />
                    <v-text-field
                      label="البريد الألكتروني"
                      type="email"
                      v-model="user.email"
                    />
                    <v-text-field
                      label="كلمة السر"
                      type="password"
                      v-model="user.password"
                    />
                  </v-card-text>
                </v-window-item>

                <v-window-item :value="1">
                  <v-card-text>
                    <v-menu
                      ref="menu"
                      v-model="menu"
                      :close-on-content-click="false"
                      :return-value.sync="user.BirthDate"
                      transition="scale-transition"
                      offset-y
                      readonly
                      min-width="290px"
                    >
                      <template v-slot:activator="{ on }">
                        <v-text-field
                          v-model="user.BirthDate"
                          label="تاريخ ميلادك"
                          prepend-icon="event"
                          v-on="on"
                          readonly
                        ></v-text-field>
                      </template>
                      <v-date-picker
                        v-model="user.BirthDate"
                        no-title
                        scrollable
                        locale="ar-sd"
                        first-day-of-week="0"
                        min="1920-01-01"
                        :max="new Date().toISOString().substr(0, 10)"
                      >
                        <v-spacer></v-spacer>
                        <v-btn
                          text
                          color="primary"
                          @click="$refs.menu.save(user.BirthDate)"
                          >موافق</v-btn
                        >
                        <v-btn text color="primary" @click="menu = false"
                          >إلغاء</v-btn
                        >
                      </v-date-picker>
                    </v-menu>
                    <v-select
                      :items="genders"
                      item-value="abbr"
                      item-text="human"
                      label="الجنس"
                      v-model="user.gender"
                      hide-details
                      solo
                    ></v-select>
                    <v-autocomplete
                      :items="countries"
                      item-value="code"
                      item-text="name"
                      label="الدولة"
                      v-model="user.countries"
                      hide-details
                      no-data-text="لا نتائج"
                      clearable
                      solo
                      open-on-clear
                      class="my-3"
                    />
                    <v-autocomplete
                      label="نمط الشخصية"
                      :items="personalities"
                      v-model="user.Mbti"
                      hide-details
                      no-data-text="لا نتائج"
                      clearable
                      solo
                      open-on-clear
                    />
                  </v-card-text>
                </v-window-item>

                <v-window-item :value="2">
                  <v-card-text class="pa-4 text-xs-center">
                    <v-icon color="green" class="d-flex" size="135"
                      >mdi-check-circle</v-icon
                    >
                    <h3 class="title font-weight-light mb-2">
                      تم إنشاء الحساب بنجاح
                    </h3>
                    <span class="caption grey--text"
                      >اضغط على التالي للذهاب لصفحة تسجيل الدخول</span
                    >
                  </v-card-text>
                </v-window-item>
              </v-window>

              <v-divider></v-divider>

              <v-card-actions>
                <v-btn
                  color="primary"
                  @click="step == 0 ? step++ : createUser()"
                  :class="[step === 0 ? 'mx-auto d-block' : '']"
                  :to="step === 2 ? '/' : undefined"
                >
                  <!-- <span :v-html="step != 2 ? 'a' : 'v' "></span> -->
                  {{ step != 2 ? "التالي" : "الى الصفحة الرئيسية" }}
                </v-btn>
                <v-spacer v-if="step !== 0"></v-spacer>
                <v-btn v-show="step !== 0" text @click="step--">
                  السابق
                </v-btn>
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
import countr from "./countries.json";
console.log(countr);
export default {
  data: () => ({
    step: 0,
    menu: false,
    user: {
      name: null,
      password: null,
      email: null,
      gender: null,
      countries: null,
      BirthDate: new Date().toISOString().substr(0, 10),
      Mbti: null
    },

    genders: [
      {
        human: "ذكر",
        abbr: "M"
      },
      {
        human: "انثى",
        abbr: "F"
      }
    ],
    countries: countr,
    personalities: [
      { header: 'مجموعة ال"NT"' },
      "INTJ",
      "ENTJ",
      "INTP",
      "ENTP",
      { header: 'مجموعة ال"NF"' },
      "INFJ",
      "ENFJ",
      "INFP",
      "ENFP",
      { header: 'مجموعة ال"ST"' },
      "ISTJ",
      "ESTJ",
      "ISTP",
      "ESTP",
      { header: 'مجموعة ال"SF"' },
      "ISFJ",
      "ESFJ",
      "ISFP",
      "ESFP"
    ]
  }),

  computed: {
    currentTitle() {
      switch (this.step) {
        case 0:
          return "المعلومات الأساسية";
        case 1:
          return "المزيد عنك";
        default:
          return "تم بنجاح";
      }
    }
  },

  methods: {
    createUser: function() {
      const t = this;

      axios
        .post("registers/", this.user)
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
      this.$store.commit("CurrentUser", this.user);
      this.step++;
      console.log(this.$store.state.user);
    }
  }
};
</script>

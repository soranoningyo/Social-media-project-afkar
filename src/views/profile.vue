<template>
  <v-app id="inspire">
    <a-layout/>
    <v-content>
      <v-container grid-list-xl>
        <v-layout row wrap>
          <v-flex xs12>
            <v-sheet elevation="10" width="100%" style="position:relative"> 
              <div style="height:400px" class="profile-img-div">
                <v-img src="https://scontent.fkrt1-2.fna.fbcdn.net/v/t1.0-9/66725961_2364861590438125_9223060192164315136_o.jpg?_nc_cat=108&_nc_eui2=AeEEwb1upd5oO0Ng9OKUOJJJuEh4C9W7xnPtBU4l8nL_tU93n6g0T8LmxjhZI5Clcqttm3DnEnMlnaK2txv7wA6mMkiKRuc0i_OSqgWX5jL38w&_nc_oc=AQkn_-uvrv-xi4Fnpe95RMkJ171Z9T6uJgoF3UUq6SMBqkbs90WI7rp-4q-pNytDU3k&_nc_ht=scontent.fkrt1-2.fna&oh=2aa52076e783e3cee5cbe2972898c006&oe=5DA3CCFA" max-width="100%" height="inherit"/>
                <v-img src="https://scontent.fkrt1-2.fna.fbcdn.net/v/t1.0-9/14956489_1804503339807289_5549833958709266648_n.jpg?_nc_cat=106&_nc_eui2=AeFYJB-61MBO0rt7e2X-Du6tB4ycmxP1xTmPLRCf8Tn_nvROZHRCfY9qdD_yB3lgRi0BNQIl5SYgqVKDq2k24rtERLnmwzxlW8OmYNy7qw7EVg&_nc_oc=AQk0CDjZwPh2PSIRlvgdCFkTiWK3L7dA2SA71iv74Twz78cy3goxuS6YKcvhCuZtxIk&_nc_ht=scontent.fkrt1-2.fna&oh=1f59b735833f01dfc569e8b702635d1c&oe=5DE94B36" class="profile-pic"/>
              </div>
            </v-sheet>
            <v-sheet elevation="10" width="84%" class="aboutMe my-4 mx-auto" style="padding:24px 64px 24px 24px">
              <div class="mb-1">
                <v-icon large color="blue">mdi-account</v-icon>
                <bdi class="headline pr-1" >ahmed abdelkhalig</bdi>
              </div>
              <v-divider />
              <div class="text-center mt-3">
                سأستمر بالتقدم ... حتى أمسح العدو ..
              </div>
            </v-sheet>
            <v-sheet elevation="10" class="pa-4">
              <v-layout row wrap>
                <v-flex md6 xs12>
                  <v-card tile>
                    <v-list-item>
                      <v-list-item-content>
                        <v-list-item-title>نقاط الأفكار</v-list-item-title>
                      </v-list-item-content>
                      <v-list-item-action>200 نقطة</v-list-item-action>
                    </v-list-item>
                    <v-divider/>
                    <v-list-item>
                      <v-list-item-content>
                        <v-list-item-title>أخر ظهور</v-list-item-title>
                      </v-list-item-content>
                      <v-list-item-action>قبل ساعة</v-list-item-action>
                    </v-list-item>
                    <v-divider/>
                    <v-list-item >
                      <v-list-item-content>
                        <v-list-item-title>عدد الأفكار المساهم بها</v-list-item-title>
                      </v-list-item-content>
                      <v-list-item-action>76 فكرة</v-list-item-action>
                    </v-list-item>
                  </v-card>
                </v-flex>
                <v-flex md6 xs12>
                  <v-card tile>
                    <v-list-item>
                      <v-list-item-content>
                        <v-list-item-title>نوع الشخصية</v-list-item-title>
                      </v-list-item-content>
                      <v-list-item-action>INTJ</v-list-item-action>
                    </v-list-item>
                    <v-divider/>
                    <v-list-item>
                      <v-list-item-content>
                        <v-list-item-title>تأريخ التسجيل</v-list-item-title>
                      </v-list-item-content>
                      <v-list-item-action>2019/8/11</v-list-item-action>
                    </v-list-item>
                    <v-divider/>
                    <v-list-item>
                      <v-list-item-content>
                        <v-list-item-title>الرتبة</v-list-item-title>
                      </v-list-item-content>
                      <v-list-item-action>عضو مميز</v-list-item-action>
                    </v-list-item>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-sheet>
            <v-sheet elevation="10" class="pa-4 my-4">
              <div class="display-1">
                أفكاري
              </div>
              <v-divider class="mb-4 mt-2"/>
              <v-layout row wrap justify-center>
                <v-flex md10>
                  <postCard v-for="(n,i) in cardData" :key="i" class="mb-3" :id="n.id" :cardTitle="n.title" :cardText="n.context" :date="n.publishedDate" :user="n.user" :rating="n.rating" :imgSrc="n.img"/>
                </v-flex>
              </v-layout>
            </v-sheet>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>
<script>
  export default {
    data: () => ({
      items: [
        { title: 'Click Me' },
        { title: 'Click Me' },
        { title: 'Click Me' },
        { title: 'Click Me 2' },
      ],
    }),
    computed: {
      cardData () {
        return this.$store.state.essays.slice(2)
      }
    }
  }
</script>
<style>
  .profile-pic  {
    border-radius: 50%;
    background-color:#2196f3;
    background-clip: content-box;
    position: absolute;
    height: 150px;
    width: 150px;
    bottom: -75px;
    right: 15px;
    z-index: 2;
  }
  @media (max-width:900px) {
    .profile-pic {
      right: calc(50% - 75px);
    }
    .v-sheet.aboutMe {
      margin-top: 56px !important;
      padding: 24px !important;
      text-align: center;
    }
    .v-sheet.aboutMe i {
      display: none
    }
    .profile-img-div {
      height: 300px !important;
    }
  }
  .profile-pic .v-image__image {
    padding: 3px;
    background-clip: content-box;
    border-radius: 50%;
  }
  .v-icon {
    vertical-align: sub !important;
  }
</style>

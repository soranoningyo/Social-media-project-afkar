<template>
  <v-app id="inspire">
    <a-layout />
    <v-content>
      <v-container grid-list-xl>
        <v-layout row wrap>
          <v-flex md8>
            <div class="headline mb-1">
              <span>مخزن أفكار</span>
            </div>
            <v-divider class="mb-2"></v-divider>
            <newsW :cardData="EssaysNewsData" />
            <div
              class="headline mb-2 mt-4"
              style="display: flex;justify-content: space-between;font-family: 'flat-jooza' , cursive !important"
            >
              <span>نقاشات مفتوحة</span>
              <v-btn color="blue darken-2" dark to="/initDisccution"
                >أبدا نقاشًا</v-btn
              >
            </div>
            <v-divider class="mb-2"></v-divider>
            <newsW :cardData="EssaysNewsData" />
            <div class="headline mb-2 mt-4">
              <router-link to="/disccution">ناقش</router-link>
            </div>
          </v-flex>
          <v-flex md4>
            <sidebar />
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import newsW from "@/components/news";
import axios from "axios";
export default {
  components: {
    newsW
  },
  data() {
    return {
      EssaysNewsData: {}
    };
  },
  created() {
    axios
      .get("api/essays/")
      .then((response) => {
        this.EssaysNewsData = response.data;
        console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }
};
</script>

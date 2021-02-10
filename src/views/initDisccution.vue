<template>
  <v-app id="inspire">
    <a-layout />
    <v-content>
      <v-container grid-list-xl>
        <v-layout row wrap>
          <v-flex md8>
            <div class="headline mb-1">
              <span> فكرة جديدة</span>
            </div>
            <v-divider class="mb-3"></v-divider>
            <v-text-field
              v-model="dis_data.title"
              label="عنوان النقاش"
              hide-details
              class="mb-5"
            ></v-text-field>
            <v-textarea
              v-model="dis_data.context"
              label="محتوى النقاش"
              auto-grow
              outlined
              color="blue"
              row-height="25"
              shaped
              hide-details
              clearable
              class="my-5"
            />
            <v-select
              v-model="dis_data.cate"
              :items="cate"
              label="التوجه"
              solo
              hide-details
              class="my-5"
            />
            <v-file-input
              v-model="dis_data.imgfile"
              class="my-5"
              label="أرفق صورة"
              prepend-icon="mdi-paperclip"
            >
              <template v-slot:selection="{ text }">
                <v-chip small label color="primary">
                  {{ text }}
                </v-chip>
              </template>
            </v-file-input>
            <v-btn color="blue darken-2" dark @click="post">نشر</v-btn>
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
import axios from "axios";
export default {
  data() {
    return {
      cate: ["ثقافة", "سياسة", "رياضة", "علوم طبية", "تقنية", "هندسة", "اداب"],
      dis_data: {
        title: null,
        context: null,
        // cate:null,
        img: ""
      }
    };
  },
  methods: {
    post: function() {
      axios({
        method: "post",
        url: "api/tarh/",
        data: this.dis_data
      });
    }
  }
};
</script>

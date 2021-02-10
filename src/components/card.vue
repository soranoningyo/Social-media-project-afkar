<template>
  <v-card elevation="7">
    <div style="position:relative">
      <v-list-item>
        <v-list-item-avatar color="blue" class="mx-3"></v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title class="headline">{{
            this.cardTitle
          }}</v-list-item-title>
          <v-list-item-subtitle
            >بواسطة
            <router-link
              to="/profile"
              style="text-decoration:none;cursor:pointer"
              >{{ this.user }}</router-link
            ></v-list-item-subtitle
          >
          <v-list-item-subtitle class="mt-1 mr-1">
            في {{ this.date }}</v-list-item-subtitle
          >
        </v-list-item-content>
      </v-list-item>
    </div>
    <v-img :src="imgSrc" class="grey" height="220">
      <template v-slot:placeholder>
        <v-layout fill-height align-center justify-center ma-0>
          <v-progress-circular indeterminate color="grey lighten-5" />
          <span class="mr-2">جارِ التحميل</span>
        </v-layout>
      </template>
    </v-img>
    <v-card-text :class="[this.len == true ? 'title' : '']">
      {{ this.all }}
    </v-card-text>
    <v-card-actions>
      <v-btn
        text
        dark
        color="blue"
        class="title"
        :to="{ path: `/essay/${this.id}` }"
        v-if="this.len != true"
      >
        تابع القراءة
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn icon color="blue">
        <v-icon>mdi-share-variant</v-icon>
      </v-btn>
      <v-btn class="mx-2" fab dark icon color="blue">
        <v-icon dark>remove</v-icon>
      </v-btn>

      <v-chip color="blue" dark class="subtitle-1">{{ this.rating }}</v-chip>

      <v-btn class="mx-2" fab dark icon color="blue">
        <v-icon dark>add</v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>
<script>
export default {
  props: [
    "cardTitle",
    "cardText",
    "date",
    "user",
    "imgSrc",
    "rating",
    "id",
    "len",
  ],
  computed: {
    all: function() {
      return this.len == true
        ? this.cardText
        : this.cardText.substring(0, 300) + " ...";
    },
  },
};
</script>

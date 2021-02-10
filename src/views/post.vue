<template>
  <v-app id="inspire">
    <a-layout />
    <v-content>
      <v-container grid-list-xl>
        <v-layout row wrap>
          <v-flex md12>
            <postCard
              class="mb-5"
              :id="cardData.pk"
              :len="true"
              :cardTitle="cardData.title"
              :cardText="cardData.context"
              :date="cardData.publishedDate"
              :user="cardData.user"
              :rating="cardData.rating"
              :imgSrc="cardData.img"
            />
            <div>
              <comment
                v-for="(item, index) in cardData.comments"
                :key="index"
                :comment="item.comment"
                :pk="item.id"
                :user="item.user_id"
                :parent="item.parent_id"
                :children="item.children"
                :depth="0"
              ></comment>
            </div>
          </v-flex>
          <!-- <v-flex md4>
            <sidebar />
          </v-flex> -->
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>
<script>
import axios from "axios";
import comment from "@/components/comment";
export default {
  components: {
    comment,
  },
  data() {
    return {
      cardData: {},
    };
  },
  created() {
    axios.get("api/essays/" + this.$route.params.id + "/").then((response) => {
      this.cardData = response.data;
      console.log(response.data);
    });
    // (function() { // DON'T EDIT BELOW THIS LINE
    // var d = document, s = d.createElement('script');
    // s.src = 'https://beta-6.disqus.com/embed.js';
    // s.setAttribute('data-timestamp', +new Date());
    // (d.head || d.body).appendChild(s);
    // })();
  },
};
</script>
<style>
.appliction .title {
  font-family: "flat-jooza", cursive !important;
}
</style>

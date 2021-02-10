<template>
  <v-app id="inspire">
    <a-layout/>
    <v-content>
      <v-container grid-list-xl>
        <v-layout row wrap>
          <v-flex md8>
            <div class="headline mb-1">
              <span>مخزن أفكار</span>
            </div>
            <v-divider class="mb-2"></v-divider>
            <postCard class="mb-3" v-for="(n, index) in cardData" :key="index" :id="n.id" :cardTitle="n.title" :cardText="n.context" :date="n.publishedDate" :user="n.user" :rating="n.rating" :imgSrc="n.img"/>
          </v-flex>
          <v-flex md4 >
            <sidebar />
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>


<script>
import json from './../views/essays.json'
  export default {
    data() {
      return {
        cardData:json
      }
    },
  }
</script>
<template>
  <v-layout justify-center>
    <v-expansion-panels inset>
      <v-expansion-panel v-for="(item, i) in 1" :key="i">
        <v-expansion-panel-header>Item</v-expansion-panel-header>
        <v-expansion-panel-content>
          <div ref="input"></div>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </v-layout>
</template>
<script>
import acomment from "./comment.vue";
import Vue from "vue";
export default {
  created() {
    var vuecomment = Vue.extend(acomment);
    var comment = new vuecomment();
    comment.$mount(); // pass nothing
    // this.refs.container.appendChild(comment.$el);
    console.log(this.refs);
  }
};
</script>

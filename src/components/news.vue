<template>
  <v-layout align-center wrap>
    <v-flex md1 xs12 order-md1 order-xs2 class="text-center">
      <v-item-group v-model="window" class="shrink horizontally" mandatory>
        <div class="d-inline-block">
          <v-btn icon @click="prev">
            <v-icon v-if="$vuetify.breakpoint.mdAndUp">mdi-chevron-up</v-icon>
            <v-icon v-else>mdi-chevron-left</v-icon>
          </v-btn>
        </div>
        <v-item
          v-for="(n, i) in cardData"
          :key="i"
          v-slot:default="{ active, toggle }"
        >
          <div class="d-inline-block">
            <v-btn :input-value="active" icon @click="toggle">
              <v-icon>mdi-record</v-icon>
            </v-btn>
          </div>
        </v-item>
        <div class="d-inline-block">
          <v-btn icon @click="next">
            <v-icon v-if="$vuetify.breakpoint.mdAndUp">mdi-chevron-down</v-icon>
            <v-icon v-else>mdi-chevron-right</v-icon>
          </v-btn>
        </div>
      </v-item-group>
    </v-flex>

    <v-flex md11 xs12 order-md2 order-xs1>
      <v-window
        :touch="{ left: prev, right: next }"
        v-model="window"
        class="elevation-1"
      >
        <v-window-item
          v-for="(n, i) in cardData"
          :key="i"
          transition="fade-transition"
          reverse-transition="fade-transition"
        >
          <postCard
            :id="n.pk"
            :cardTitle="n.title"
            :cardText="n.context"
            :date="n.publishedDate"
            :user="n.user"
            :rating="n.rating"
            :imgSrc="n.img"
          />
        </v-window-item>
      </v-window>
    </v-flex>
  </v-layout>
</template>
<script>
export default {
  data: () => ({
    window: 0,
  }),
  props: ["cardData"],
  methods: {
    next() {
      this.window =
        this.window + 1 === this.cardData.length ? 0 : this.window + 1;
    },
    prev() {
      this.window =
        this.window - 1 < 0 ? this.cardData.length - 1 : this.window - 1;
    },
  },
};
</script>
<style>
@media (max-width: 960px) {
  .horizontally {
    display: inline-flex;
    flex-direction: row-reverse;
  }
}
</style>

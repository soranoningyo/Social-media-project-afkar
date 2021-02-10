<template>
  <div>
    <v-card :style="indent" class="mt-1">
      <v-container class="pt-0">
        <v-row justify="space-between">
          <v-col cols="auto" class="text-center pl-0 py-0">
            <v-row class="flex-column ma-0 " justify="center">
              <v-col class="px-0 py-2">
                <v-btn icon color="blue">
                  <v-icon>add</v-icon>
                </v-btn>
              </v-col>

              <v-col class="px-0 py-2">
                5
              </v-col>

              <v-col class="px-0 py-2">
                <v-btn icon color="blue">
                  <v-icon>remove</v-icon>
                </v-btn>
              </v-col>
            </v-row>
          </v-col>
          <v-col class="py-0">
            <v-row class="flex-column ma-0 fill-height" justify="center">
              <v-col>
                <v-list-item class="px-0">
                  <v-list-item-avatar
                    color="blue"
                    class="mr-1"
                  ></v-list-item-avatar>
                  <v-list-item-content>
                    <v-list-item-title class="headline">
                      <router-link
                        to="/profile"
                        style="text-decoration:none;cursor:pointer"
                        >مج قهوة</router-link
                      ></v-list-item-title
                    >

                    <v-list-item-subtitle class=" mr-2">
                      منذ {{ this.depth }} ساعات
                    </v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-divider />
              </v-col>
              <v-col class="pr-5">
                <p>
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. In
                  excepturi vel veritatis. Possimus totam distinctio laboriosam
                  ducimus consectetur rerum dolorum quia rem velit odit iure,
                  deleniti iste nostrum quasi quas.
                </p>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
    </v-card>
    <comment
      v-for="(item, index) in children"
      :key="index"
      :comment="item.comment"
      :pk="item.id"
      :user="item.user_id"
      :parent="item.parent_id"
      :children="item.children"
      :depth="depth + 1"
    >
    </comment>
  </div>
</template>
<script>
export default {
  props: ["pk", "comment", "user", "children", "depth", "parent"],
  computed: {
    indent() {
      return {
        "margin-right": `${this.depth * 20}px`,
      };
    },
  },
  data() {
    return { showChildren: false };
  },
  methods: {
    toggleChildren() {
      this.showChildren = !this.showChildren;
    },
  },
};
// <v-card-text>
//   <p class="display-1 text--primary">
//     {{ user }}
//   </p>
//   <div class="text--primary">
//     {{ comment }}<br />
//     <span v-if="parent != null">{{ parent }}</span>
//     <span v-if="parent == null">no parent</span>
//   </div>
// </v-card-text>
</script>

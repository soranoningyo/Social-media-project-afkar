<template>
  <v-app id="inspire">
    <a-layout/>
    <v-content>
      <v-container fill-height fluid>
        <v-layout row wrap>
          <v-flex lg3 xs12 order-xs3 order-lg1>
            <v-sheet elevation="1" class="fix-on-mobile" height="100%" style="display:flex;flex-direction:column">
              <v-list three-line shaped flat avatar style="overflow:auto;flex: 1 1 0">
                <v-subheader>المشاركين في النقاش</v-subheader>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item v-for="(item, i) in items" :key="i">
                    <v-list-item-avatar avatar class="mx-2">
                      <v-img :src="item.avatar"></v-img>
                    </v-list-item-avatar>
                    <v-list-item-content>
                      <v-list-item-title v-html="item.title"></v-list-item-title>
                      <v-list-item-subtitle v-html="item.subtitle"></v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-sheet>
          </v-flex>
          <v-flex xs12 lg6 order-lg2 order-xs1>
            <v-sheet elevation="1" class="full-vh" height="100%">
              <v-card height="100%" style="display:flex;flex-direction: column;">
                <v-card-title>تأملات ميتافيزيقية</v-card-title>
                <v-card-text style="flex:2 1 0 !important;overflow:auto">
                  <div v-for="(item, index) in Comments" :key="index" style="display:flex">
                    <span style="flex-grow:1" v-if="item.dir == 'gray'"></span>
                    <div
                      class="ma-2 px-2 py-1 rounded"
                      :class="[item.dir == 'blue' ? 'blue' : 'red']"
                      style="max-width:250px;color:white;border-radius:5px;word-break: break-word;"
                      v-text="item.content"
                    ></div>
                  </div>
                </v-card-text>
                <v-card-actions>
                  <v-textarea
                    v-model="first"
                    outlined
                    shaped
                    hide-details
                    autofocus
                    no-resize
                    rows="2"
                    @keyup.enter="comment"/>
                  <v-btn icon @click="comment">
                    <v-icon style="transform:rotateY(180deg)">mdi-send</v-icon>
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-sheet>
          </v-flex>
          <v-flex lg3 xs12 order-xs2 order-lg3>
            <v-sheet elevation="1" class="fix-on-mobile" height="100%" style="flex-direction:column;display:flex">
              <v-card style="overflow:auto;flex: 3 1 0">
                <v-list>
                  <v-list-group
                    v-for="item in source"
                    :key="item.title"
                    v-model="item.active"
                    :prepend-icon="item.action"
                    no-action>
                    <template v-slot:activator>
                      <v-list-item-content>
                        <v-list-item-title v-text="item.title"></v-list-item-title>
                      </v-list-item-content>
                    </template>
                    <v-list-item v-for="subItem in item.items" :key="subItem.title">
                      <v-list-item-content >
                        <v-list-item-title v-text="subItem.title"></v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list-group>
                </v-list>
              </v-card>

                <v-card style="overflow:auto;
                              flex: 2 1 0;
                              display: flex;
                              flex-wrap: wrap;
                              flex-direction: column;
                              align-content: space-around;
                              text-align:center;
                              min-height:175px
                              ">
                  <v-subheader class="d-block mt-2 mb-0">النقاط المرشحة</v-subheader>
                  <div class="text-center">
                    <v-dialog v-model="dialog" width="500" >
                      <template v-slot:activator="{ on }">
                        <v-btn
                          color="blue lighten-2"
                          dark
                          class="title"
                          block
                          depressed
                          elevation="1"
                          v-on="on">
                          أضف نقطة
                        </v-btn>
                      </template>

                      <v-card>
                        <v-card-title primary-title>
                          إضافة نقطة
                        </v-card-title>
                        <v-divider class="my-2"/>
                        <v-card-text>
                          <v-textarea
                            label="أضف نقطة ما"
                            auto-grow
                            outlined
                            color="blue"
                            row-height="25"
                            shaped
                            hide-details
                            clearable
                            v-model="point"
                            @keyup.enter="addpoint"
                          />
                        </v-card-text>

                        <v-divider class="mb-1"/>

                        <v-card-actions>
                          <v-btn color="primary" text @click="addpoint" >
                            أضف
                          </v-btn>
                          <v-btn color="gray" text @click="dialog = false" >
                            إلغاء
                          </v-btn>
                        </v-card-actions>
                      </v-card>
                    </v-dialog>
                  </div>
                  <v-select :items="points" label="النقاط المرشحة" solo hide-details/>
                </v-card>
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
      item: 5,
      items: [
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
          title: 'احمد خيري',
          subtitle: "هذا النص هو مثال لنص يمكن أن يستبدل في نفس المساحة، لقد تم توليد هذا النص من مولد النص العربى، حيث يمكنك أن تولد مثل هذا النص أو العديد من النصوص الأخرى إضافة إلى زيادة عدد الحروف",
        },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
          title: 'عمر منصور',
          subtitle: "هذا النص هو مثال لنص يمكن أن يستبدل في نفس المساحة، لقد تم توليد هذا النص من مولد النص العربى، حيث يمكنك أن تولد مثل هذا النص أو العديد من النصوص الأخرى إضافة إلى زيادة عدد الحروف",
        },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
          title: 'مريم خالد',
          subtitle: "هذا النص هو مثال لنص يمكن أن يستبدل في نفس المساحة، لقد تم توليد هذا النص من مولد النص العربى، حيث يمكنك أن تولد مثل هذا النص أو العديد من النصوص الأخرى إضافة إلى زيادة عدد الحروف",
        },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
          title: 'امنية احمد',
          subtitle: "هذا النص هو مثال لنص يمكن أن يستبدل في نفس المساحة، لقد تم توليد هذا النص من مولد النص العربى، حيث يمكنك أن تولد مثل هذا النص أو العديد من النصوص الأخرى إضافة إلى زيادة عدد الحروف",
        },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
          title: 'Samar Mohammed',
          subtitle: "هذا النص هو مثال لنص يمكن أن يستبدل في نفس المساحة، لقد تم توليد هذا النص من مولد النص العربى، حيث يمكنك أن تولد مثل هذا النص أو العديد من النصوص الأخرى إضافة إلى زيادة عدد الحروف",
        },
      ],
      source : [
          {
            action: 'local_activity',
            title: 'مصادر اساسية',
            items: [
              { title: 'https://www.google.com' },
            ],
          },
          {
            action: 'restaurant',
            title: 'مصادر ثانوية 1',
            items: [
              { title: '1' },
              { title: '2' },
              { title: '3' },
              { title: '4' },
              { title: '5' },
              { title: '6' },
              { title: '7' },
              { title: '8' },
              { title: '9' },
              { title: '10' },
              { title: '11' },
              { title: '12' },
            ],
          },
          {
            action: 'school',
            title: 'مصادر فرعية 2',
            items: [
              { title: '1' },
            ],
          },
          {
            action: 'directions_run',
            title: 'مصادر فرعية 3',
            items: [
              { title: '1' },
            ],
          },
        ],
        points: [
          'طيصط طيصط وان طو صري',
          'halo halo goodie goodie',
        ],
        point : "",
        dialog:false,
        first: "",
        Comments : [
          {
            content :"Asa",
            dir : "gray"
          },
          {
            content :"Asa",
            dir : "blue"
          },
          {
            content :"Asa",
            dir : "blue"
          },
          {
            content :"Asa",
            dir : "gray"
          },
          {
            content :"Asa",
            dir : "blue"
          },
          {
            content :"Asa",
            dir : "gray"
          }
        ]
    }),
    methods: {
      addpoint: function () {
        this.points.push(this.point)
        this.point = ""
        this.dialog = false
      },
      deleteItem(item) {
      this.points.splice(this.points.indexOf(item), 1);
      },
      comment : function () {
        this.Comments.push({
          content: this.first,
          dir : "blue"
        })
        this.first = ""
      }
    },
  }
</script>

<style>
@media (max-width:1260px) {

  .fix-on-mobile {
    height: 512px !important
  }
  .full-vh {
    height: calc(100vh - 56px - 48px - 23px) !important;
  }
}
.v-list-item__content {
  padding-right: 6px;
}
</style>

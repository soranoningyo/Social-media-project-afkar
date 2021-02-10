<template>
  <v-app id="inspire">
    <a-layout/>
    <v-content>
      <v-container grid-list-xl>
        <v-layout row wrap>
          <v-flex md8>
            <h1>عن الموقع</h1>
            <router-link to="/">الرئيسية</router-link><br/>
            <router-link to="/post">مقال</router-link>
          </v-flex>
          <v-flex md4 >
            <sidebar />
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

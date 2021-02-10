import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/About.vue")
    },
    {
      path: "/post",
      name: "post",
      component: () => import("./views/post.vue")
    },
    {
      path: "/login",
      name: "login",
      component: () => import("./views/login.vue")
    },
    {
      path: "/register",
      name: "register",
      component: () => import("./views/register.vue")
    },
    {
      path: "/profile",
      name: "profile",
      component: () => import("./views/profile.vue")
    },
    {
      path: "/disccution",
      name: "disccution",
      component: () => import("./views/disccution.vue")
    },
    {
      path: "/essays",
      name: "essays",
      component: () => import("./components/showAll.vue")
    },
    {
      path: "/essay/:id",
      name: "essay",
      component: () => import("./views/post.vue")
    },
    {
      path: "/initDisccution",
      name: "initDisccution",
      component: () => import("./views/initDisccution.vue")
    }
    // {
    //   path: "*",
    //   name: "notFound",
    //   component: () => import("./components/NOTFOUNDed.vue")
    // }
  ]
});

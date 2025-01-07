import { createRouter, createWebHistory } from "vue-router";
import DashBoard from "../views/DashBoardView.vue";
import FourView from "../views/FourView.vue";

const routes = [
  {
    path: "/",
    name: "dashboard",
    component: DashBoard,
  },
  {
    path: "/:catchAll(.*)",
    component: FourView,
    name: "NotFound",
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

// Add a global beforeEach guard
router.beforeEach((to, from, next) => {
  const isPageReload = sessionStorage.getItem("isPageReload");
  sessionStorage.removeItem("isPageReload");

  if (isPageReload && to.fullPath !== "/") {
    next("/");
  } else {
    next();
  }
});

// Set a flag to detect page reload
window.addEventListener("beforeunload", () => {
  sessionStorage.setItem("isPageReload", "true");
});

export default router;

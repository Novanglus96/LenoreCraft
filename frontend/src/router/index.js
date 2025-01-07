import { createRouter, createWebHistory } from "vue-router";
import DashBoard from "../views/DashBoardView.vue";
import FourView from "../views/FourView.vue";
import TasksView from "@/views/TasksView.vue";
import ShoppingView from "@/views/ShoppingView.vue";
import ProjectsView from "@/views/ProjectsView.vue";
import ToolsView from "@/views/ToolsView.vue";

const routes = [
  {
    path: "/",
    name: "dashboard",
    component: DashBoard,
  },
  {
    path: "/tasks",
    name: "tasks",
    component: TasksView,
  },
  {
    path: "/shopping",
    name: "shopping",
    component: ShoppingView,
  },
  {
    path: "/projects",
    name: "projects",
    component: ProjectsView,
  },
  {
    path: "/tools",
    name: "tools",
    component: ToolsView,
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

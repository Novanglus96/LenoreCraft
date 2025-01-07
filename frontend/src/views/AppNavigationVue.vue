<template>
  <v-app-bar color="primary" density="compact">
    <template v-slot:prepend>
      <v-menu width="200">
        <template v-slot:activator="{ props }">
          <v-app-bar-nav-icon v-bind="props"></v-app-bar-nav-icon>
        </template>
        <v-list>
          <v-list-item
            v-for="(item, index) in menu_items"
            class="hover-theme"
            :key="index"
            :prepend-icon="item.icon"
            :base-color="item.basecolor"
            :color="item.color"
            :to="item.to"
            :title="item.title"
          ></v-list-item>
          <v-list-item
            class="hover-theme"
            prepend-icon="mdi-hammer-screwdriver"
            as="a"
            href="/admin"
            v-bind="props"
            base-color="primary"
            color="accent-darken-1"
            title="Settings"
          ></v-list-item>
        </v-list>
      </v-menu>
      <v-img :width="132" aspect-ratio="1/1" cover src="/logov2.png"></v-img>
    </template>
    <v-app-bar-title>
      <span class="text-caption font-weight-bold">v0.0.1</span></v-app-bar-title
    >
  </v-app-bar>
</template>
<script setup>
import { ref } from "vue";

const menu_items = ref([
  {
    icon: "mdi-toolbox",
    color: "accent-darken-1",
    basecolor: "primary",
    to: "/",
    title: "Dashboard",
    tooltip: "Dashboard",
  },
  {
    icon: "mdi-screw-flat-top",
    color: "accent-darken-1",
    basecolor: "primary",
    to: "/tasks",
    title: "Tasks",
    tooltip: "Tasks",
  },
  {
    icon: "mdi-wheel-barrow",
    color: "accent-darken-1",
    basecolor: "primary",
    to: "/shopping",
    title: "Shopping List",
    tooltip: "Shopping List",
  },
  {
    icon: "mdi-hand-saw",
    color: "accent-darken-1",
    basecolor: "primary",
    to: "/projects",
    title: "Projects",
    tooltip: "Projects",
  },
  {
    icon: "mdi-tape-measure",
    color: "accent-darken-1",
    basecolor: "primary",
    to: "/tools",
    title: "Tools",
    tooltip: "Tools",
  },
]);
</script>
<style>
.hover-theme:hover {
  background-color: #ffe480;
}
</style>

<template>
  <div>
    <v-row class="pa-2 ga-2 d-flex">
      <v-col class="rounded text-center"><ProjectListWidget /></v-col>
    </v-row>
    <v-row class="pa-2 ga-2 d-flex">
      <v-col class="rounded text-center" cols="12" sm=""
        ><TaskListWidget
      /></v-col>
      <v-col class="rounded text-center" cols="12" sm=""
        ><ShoppingListWidget /></v-col
    ></v-row>
  </div>
</template>

<script setup>
import TaskListWidget from "@/components/TaskListWidget.vue";
import ShoppingListWidget from "@/components/ShoppingListWidget.vue";
import ProjectListWidget from "@/components/ProjectListWidget.vue";
</script>

<template>
  <div>
    <v-row class="pa-2 ga-2 d-flex">
      <v-col class="rounded text-center"><ProjectList :dash="true" /></v-col>
    </v-row>
    <v-row class="pa-2 ga-2 d-flex">
      <v-col class="rounded text-center" cols="12" sm=""
        ><TaskList :dash="true"
      /></v-col>
      <v-col class="rounded text-center" cols="12" sm=""
        ><ShoppingList :dash="true" /></v-col></v-row
    >
  </div>
</template>

<script setup>
import TaskList from "@/components/TaskList.vue";
import ShoppingList from "@/components/ShoppingList.vue";
import ProjectList from "@/components/ProjectList.vue";
</script>

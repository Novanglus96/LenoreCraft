<template>
  <div>
    <v-row class="pa-2 ga-2">
      <v-col class="rounded text-center"><TaskList :dash="True" /></v-col>
      <v-col class="rounded text-center"
        ><ShoppingList :dash="True" /></v-col></v-row
    ><v-row class="pa-2 ga-2">
      <v-col class="rounded text-center"><ProjectList :dash="True" /></v-col>
    </v-row>
  </div>
</template>

<script setup>
import TaskList from "@/components/TaskList.vue";
import ShoppingList from "@/components/ShoppingList.vue";
import ProjectList from "@/components/ProjectList.vue";
</script>

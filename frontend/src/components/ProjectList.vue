<template>
  <div>
    <v-card variant="outlined" :elevation="4" class="bg-secondary"
      ><v-card-title>Projects</v-card-title>
      <v-card-text
        ><v-data-table-server
          :headers="headers"
          :items="projects ? projects : []"
          :items-length="projects ? projects.length : 0"
          :loading="isLoading"
          item-value="id"
          items-per-page="5"
          color="primary"
          hover
          class="bg-secondary"
          no-data-text="No projects!"
          loading-text="Loading projects..."
          v-if="!isMobile"
          ><template v-slot:[`item.dimensions`]="{ item }">
            {{ convertToPrettyDimension(item.width_in) }}W
            {{ convertToPrettyDimension(item.depth_in) }}D
            {{ convertToPrettyDimension(item.height_in) }}H
          </template></v-data-table-server
        >
      </v-card-text>
    </v-card>
  </div>
</template>
<script setup>
import { ref } from "vue";
import { convertToPrettyDimension } from "@/utils/convertToPrettyDimension";
import { getProjectStatusColor } from "@/utils/getProjectStatusColor";
import { useDisplay } from "vuetify";
import { useProjects } from "@/composables/projectComposable";

const { smAndDown } = useDisplay();
const isMobile = smAndDown;

const headers = ref([
  {
    title: "Status",
    align: "start",
    sortable: false,
    key: "project_status.id",
  },
  { title: "Project Name", key: "project_name", align: "start" },
  { title: "Dimensions", key: "dimensions", align: "center" },
  { title: "Start", key: "start_date", align: "center" },
  { title: "Due", key: "due_date", align: "center" },
  { title: "Completed", key: "completed_date", align: "center" },
]);

const { projects, isLoading } = useProjects(false);
</script>

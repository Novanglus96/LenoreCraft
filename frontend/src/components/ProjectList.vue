<template>
  <div>
    <v-card variant="outlined" :elevation="4" class="bg-secondary"
      ><v-card-title
        >Projects
        <v-tooltip text="Add Project" location="top">
          <template v-slot:activator="{ props }"
            ><v-icon
              icon="mdi-plus-circle"
              size="small"
              v-bind="props"
            ></v-icon></template></v-tooltip
      ></v-card-title>
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
        >
          <template v-slot:[`header.project_name`]>
            <div class="font-weight-bold">Project Name</div>
          </template>
          <template v-slot:[`header.dimensions`]>
            <div class="font-weight-bold">Dimensions</div>
          </template>
          <template v-slot:[`header.start_date`]>
            <div class="font-weight-bold">Start</div>
          </template>
          <template v-slot:[`header.due_date`]>
            <div class="font-weight-bold">Due</div>
          </template>
          <template v-slot:[`header.completed_date`]>
            <div class="font-weight-bold">Completed</div>
          </template>
          <template v-slot:[`item.dimensions`]="{ item }">
            {{
              convertToPrettyDimension(
                item.height_in,
                item.width_in,
                item.depth_in,
                false,
              )
            }}
          </template>
          <template v-slot:[`item.project_name`]="{ item }"
            ><div class="text-left">
              <v-tooltip
                :text="item.project_status.project_status"
                location="top"
              >
                <template v-slot:activator="{ props }"
                  ><v-icon
                    icon="mdi-progress-wrench"
                    :color="getProjectStatusColor(item.project_status)"
                    v-bind="props"
                  ></v-icon></template
              ></v-tooltip>
              {{ item.project_name }}
            </div></template
          >
          <template v-slot:[`item.start_date`]="{ item }">{{
            item.start_date ? item.start_date : "(none)"
          }}</template>
          <template v-slot:[`item.due_date`]="{ item }">{{
            item.due_date ? item.due_date : "(none)"
          }}</template>
          <template v-slot:[`item.completed_date`]="{ item }">{{
            item.completed_date ? item.completed_date : "(none)"
          }}</template>
          <template v-slot:[`item.actions`]="{ item }">
            <v-tooltip text="Edit Project" location="top">
              <template v-slot:activator="{ props }"
                ><v-icon
                  class="me-2"
                  size="small"
                  @click="editItem(item.id)"
                  v-bind="props"
                >
                  mdi-pencil
                </v-icon>
              </template></v-tooltip
            >
            <v-tooltip text="Delete Project" location="top">
              <template v-slot:activator="{ props }"
                ><v-icon size="small" @click="deleteItem(item)" v-bind="props">
                  mdi-delete
                </v-icon></template
              ></v-tooltip
            >
          </template>
        </v-data-table-server>
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
    title: "Project Name",
    key: "project_name",
    align: "start",
    sortable: false,
  },
  { title: "Dimensions", key: "dimensions", align: "center", sortable: false },
  { title: "Start", key: "start_date", align: "center", sortable: false },
  { title: "Due", key: "due_date", align: "center", sortable: false },
  {
    title: "Completed",
    key: "completed_date",
    align: "center",
    sortable: false,
  },
  {
    title: "",
    key: "actions",
    align: "center",
    sortable: false,
  },
]);

const { projects, isLoading } = useProjects(false);
</script>

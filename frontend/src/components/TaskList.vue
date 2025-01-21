<template>
  <div>
    <v-card
      variant="outlined"
      :elevation="4"
      class="bg-secondary"
      v-if="!isMobile"
      :rounded="0"
      ><v-card-tile>Tasks</v-card-tile
      ><v-card-text
        ><v-data-table-server
          :headers="headers"
          :items="tasks"
          :items-length="tasks.length"
          :loading="isLoading"
          item-value="id"
          items-per-page="5"
          color="primary"
          hover
          class="blackboard"
          :rounded="0"
          ><template v-slot:[`header.task_status.id`]
            ><v-icon icon="mdi-nail" size="x-small"></v-icon
          ></template>
          <template v-slot:[`header.task_name`]>
            <div class="font-weight-bold">Task Name</div>
          </template>
          <template v-slot:[`header.start_date`]>
            <div class="font-weight-bold">Start Date</div>
          </template>
          <template v-slot:[`header.due_date`]>
            <div class="font-weight-bold">Due Date</div>
          </template>
          <template v-slot:[`header.completed_date`]>
            <div class="font-weight-bold">Completed Date</div>
          </template>
          <template v-slot:[`header.project.project_name`]>
            <div class="font-weight-bold">Project</div>
          </template>
          <template v-slot:[`item.task_name`]="{ item }"
            ><div class="text-start">{{ item.task_name }}</div></template
          ><template v-slot:[`item.project.project_name`]="{ item }"
            ><div class="text-start">
              {{ item.project.project_name }}
            </div></template
          ><template v-slot:[`item.task_status.id`]="{ item }"
            ><v-tooltip :text="item.task_status.status" location="top">
              <template v-slot:activator="{ props }"
                ><v-icon
                  icon="mdi-nail"
                  :color="getTaskStatusColor(item.task_status)"
                  v-bind="props"
                  size="small"
                ></v-icon></template></v-tooltip></template></v-data-table-server></v-card-text></v-card
    ><v-card v-if="isMobile && props.dash" :rounded="0">
      <v-list class="blackboard" :rounded="0">
        <v-list-item v-for="task in tasks" :key="task.id">
          <v-list-item-content>
            <v-list-item-title>{{ task.task_name }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-card>
  </div>
</template>
<script setup>
import { ref, defineProps } from "vue";
import { useDisplay } from "vuetify";
import { getTaskStatusColor } from "@/utils/getTaskStatusColor";

const { smAndDown } = useDisplay();
const isMobile = smAndDown;

const props = defineProps({
  dash: { type: Boolean, default: false },
});

const headers = ref([
  {
    title: "Status",
    align: "center",
    sortable: false,
    key: "task_status.id",
  },
  { title: "Task Name", key: "task_name", align: "start", sortable: false },
  { title: "Start", key: "start_date", align: "center", sortable: false },
  { title: "Due", key: "due_date", align: "center", sortable: false },
  {
    title: "Completed",
    key: "completed_date",
    align: "center",
    sortable: false,
  },
  {
    title: "Project",
    key: "project.project_name",
    align: "start",
    sortable: false,
  },
]);

const tasks = ref([
  {
    id: 1,
    task_status: {
      id: 3,
      status: "On Hold",
    },
    task_name: "Test task",
    start_date: "2025-01-01",
    due_date: "2025-01-01",
    completed_date: null,
    project: {
      id: 1,
      project_name: "Growth Board",
      project_status: {
        id: 1,
        status: "In Progress",
      },
      project_image: "image.jpg",
      start_date: "2023-06-25",
      due_date: "2023-07-09",
      completed_date: null,
      depth_in: 0.75,
      width_in: 24,
      height_in: 68,
    },
  },
  {
    id: 2,
    task_status: {
      id: 1,
      status: "Not Started",
    },
    task_name: "Test task #2",
    start_date: "2025-01-01",
    due_date: "2025-01-01",
    completed_date: null,
    project: {
      id: 1,
      project_name: "Growth Board",
      project_status: {
        id: 1,
        status: "In Progress",
      },
      project_image: "image.jpg",
      start_date: "2023-06-25",
      due_date: "2023-07-09",
      completed_date: null,
      depth_in: 0.75,
      width_in: 24,
      height_in: 68,
    },
  },
  {
    id: 3,
    task_status: {
      id: 2,
      status: "In Progress",
    },
    task_name: "Test task #3",
    start_date: "2025-01-01",
    due_date: "2025-01-01",
    completed_date: null,
    project: {
      id: 1,
      project_name: "Growth Board",
      project_status: {
        id: 1,
        status: "In Progress",
      },
      project_image: "image.jpg",
      start_date: "2023-06-25",
      due_date: "2023-07-09",
      completed_date: null,
      depth_in: 0.75,
      width_in: 24,
      height_in: 68,
    },
  },
  {
    id: 4,
    task_status: {
      id: 4,
      status: "Completed",
    },
    task_name: "Test task #4",
    start_date: "2025-01-01",
    due_date: "2025-01-01",
    completed_date: null,
    project: {
      id: 1,
      project_name: "Growth Board",
      project_status: {
        id: 1,
        status: "In Progress",
      },
      project_image: "image.jpg",
      start_date: "2023-06-25",
      due_date: "2023-07-09",
      completed_date: null,
      depth_in: 0.75,
      width_in: 24,
      height_in: 68,
    },
  },
  {
    id: 5,
    task_status: {
      id: 5,
      status: "Cancelled",
    },
    task_name: "Test task #5",
    start_date: "2025-01-01",
    due_date: "2025-01-01",
    completed_date: null,
    project: {
      id: 1,
      project_name: "Growth Board",
      project_status: {
        id: 1,
        status: "In Progress",
      },
      project_image: "image.jpg",
      start_date: "2023-06-25",
      due_date: "2023-07-09",
      completed_date: null,
      depth_in: 0.75,
      width_in: 24,
      height_in: 68,
    },
  },
]);
</script>
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap");

/* Blackboard styles */
.blackboard {
  background-image: url("@/assets/blackboard-texture.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  color: white;
  font-family: "Patrick Hand", sans-serif;
  padding: 16px;
  border-radius: 8px;
  box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.5);
}

.blackboard .v-list-item-title {
  font-size: 18px;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
}

.blackboard .v-list-item {
  border-bottom: 1px dashed rgba(255, 255, 255, 0.5);
}

.blackboard .v-list-item:last-child {
  border-bottom: none;
}
</style>

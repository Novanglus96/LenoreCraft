<template>
  <div>
    <v-card variant="outlined" :elevation="4" class="bg-secondary"
      ><v-card-title>Projects</v-card-title>
      <v-card-text
        ><v-data-table-server
          :headers="headers"
          :items="projects"
          :items-length="projects.length"
          :loading="isLoading"
          item-value="id"
          items-per-page="5"
          color="primary"
          hover
          class="bg-secondary"
          v-if="!props.dash && !isMobile"
          ><template v-slot:[`item.dimensions`]="{ item }">
            {{ convertToPrettyDimension(item.width_in) }}W
            {{ convertToPrettyDimension(item.depth_in) }}D
            {{ convertToPrettyDimension(item.height_in) }}H
          </template></v-data-table-server
        >
        <v-carousel
          hide-delimiter-background
          v-if="(props.dash || isMobile) && !isLoading"
          height="300"
        >
          <v-carousel-item
            v-for="(project, i) in projects"
            :key="i"
            :src="placeholderImage2"
            cover
          >
            <v-card width="100%" height="100%" variant="outlined"
              ><v-card-title class="bg-white"
                ><v-tooltip
                  :text="project.project_status.project_status"
                  location="top"
                >
                  <template v-slot:activator="{ props }"
                    ><v-icon
                      icon="mdi-progress-wrench"
                      :color="getProjectStatusColor(project.project_status)"
                      v-bind="props"
                    ></v-icon></template
                ></v-tooltip>
                {{ project.project_name }}</v-card-title
              ><v-card-text
                ><v-container
                  ><v-row dense
                    ><v-col v-if="!isMobile"></v-col
                    ><v-col :cols="isMobile ? 4 : 2" class="bg-white"
                      ><v-img
                        :src="
                          project.project_image
                            ? project.project_image
                            : placeholderImage
                        "
                        height="100"
                        gradient="to top right, rgba(0,115,201,.33), rgba(25,32,72,.7)"
                      ></v-img
                      ><span class="text-bold text-primary bg-white text-body-2"
                        >{{ convertToPrettyDimension(project.width_in) }}W
                        {{ convertToPrettyDimension(project.depth_in) }}D
                        {{ convertToPrettyDimension(project.height_in) }}H</span
                      ></v-col
                    ><v-col class="text-left" :cols="isMobile ? 8 : 6"
                      ><v-container
                        ><v-row dense
                          ><v-col
                            :cols="isMobile ? 4 : 1"
                            class="bg-white text-right text-primary font-weight-bold"
                            ><v-tooltip text="Start Date" location="top">
                              <template v-slot:activator="{ props }"
                                ><v-icon
                                  icon="mdi-calendar-blank"
                                  v-bind="props"
                                ></v-icon></template></v-tooltip></v-col
                          ><v-col :cols="isMobile ? 8 : 3" class="bg-white">{{
                            project.start_date
                          }}</v-col></v-row
                        ><v-row dense
                          ><v-col
                            :cols="isMobile ? 4 : 1"
                            class="bg-white text-right text-primary font-weight-bold"
                            ><v-tooltip text="Due Date" location="top">
                              <template v-slot:activator="{ props }"
                                ><v-icon
                                  icon="mdi-calendar-alert"
                                  v-bind="props"
                                ></v-icon></template></v-tooltip></v-col
                          ><v-col :cols="isMobile ? 8 : 3" class="bg-white">{{
                            project.due_date
                          }}</v-col></v-row
                        ><v-row dense
                          ><v-col
                            :cols="isMobile ? 4 : 1"
                            class="bg-white text-right text-primary font-weight-bold"
                            ><v-tooltip text="Completed Date" location="top">
                              <template v-slot:activator="{ props }"
                                ><v-icon
                                  icon="mdi-calendar-check"
                                  v-bind="props"
                                ></v-icon></template></v-tooltip></v-col
                          ><v-col :cols="isMobile ? 8 : 3" class="bg-white">{{
                            project.completed_date
                          }}</v-col></v-row
                        >
                      </v-container></v-col
                    ></v-row
                  ></v-container
                ></v-card-text
              ><v-card-actions
                ><v-btn
                  variant="flat"
                  block
                  color="accent"
                  append-icon="mdi-chevron-right"
                  >view</v-btn
                ></v-card-actions
              ></v-card
            >
          </v-carousel-item>
        </v-carousel>
      </v-card-text>
    </v-card>
  </div>
</template>
<script setup>
import { ref, defineProps, computed } from "vue";
import { convertToPrettyDimension } from "@/utils/convertToPrettyDimension";
import { getProjectStatusColor } from "@/utils/getProjectStatusColor";
import { useDisplay } from "vuetify";
import { useProjects } from "@/composables/projectComposable";

const { smAndDown } = useDisplay();
const isMobile = smAndDown;

const props = defineProps({
  dash: { type: Boolean, default: false },
});

const placeholderImage = computed(
  () => new URL("@/assets/placeholder.webp", import.meta.url).href,
);

const placeholderImage2 = computed(
  () => new URL("@/assets/placeholder2.webp", import.meta.url).href,
);

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

const { projects, isLoading } = useProjects();
</script>

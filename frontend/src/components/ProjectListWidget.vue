<template>
  <div>
    <v-card variant="outlined" :elevation="4" class="bg-secondary"
      ><v-card-title>Projects</v-card-title>
      <v-card-text
        ><v-carousel hide-delimiter-background v-if="!isLoading" height="330">
          <v-carousel-item
            v-for="(project, i) in projects.projects"
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
                      ><span
                        class="text-bold text-primary bg-white text-body-2"
                        >{{
                          convertToPrettyDimension(
                            project.height_in,
                            project.width_in,
                            project.depth_in,
                            false,
                          )
                        }}</span
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
          <v-carousel-item
            :key="-1"
            :src="placeholderImage2"
            cover
            v-if="projects.projects.length == 0"
          >
            <v-card width="100%" height="100%" variant="outlined"
              ><v-card-text
                class="text-primary font-weight-bold text-h5 font-italic"
                >No Projects - Yet!</v-card-text
              ></v-card
            >
          </v-carousel-item>
        </v-carousel>
      </v-card-text>
    </v-card>
  </div>
</template>
<script setup>
import { computed, onMounted } from "vue";
import { convertToPrettyDimension } from "@/utils/convertToPrettyDimension";
import { getProjectStatusColor } from "@/utils/getProjectStatusColor";
import { useDisplay } from "vuetify";
import { useProjects } from "@/composables/projectComposable";
import { useMainStore } from "@/stores/main";

const { smAndDown } = useDisplay();
const isMobile = smAndDown;
const mainstore = useMainStore();
const placeholderImage = computed(
  () => new URL("@/assets/placeholder.webp", import.meta.url).href,
);

const placeholderImage2 = computed(
  () => new URL("@/assets/placeholder2.webp", import.meta.url).href,
);

const { projects, isLoading } = useProjects(true);

onMounted(() => {
  mainstore.updatePagination({
    page: 1,
    page_size: 0,
    dash: true,
  });
});
</script>

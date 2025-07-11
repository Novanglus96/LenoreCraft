<template>
  <v-app>
    <v-sheet class="background-image">
      <AppNavigationVue />
      <VueQueryDevtools />
      <div>
        <v-main>
          <v-container fluid>
            <router-view />
          </v-container>
        </v-main>

        <v-snackbar
          v-model="mainstore.snackbar"
          :color="mainstore.snackbarColor"
          :timeout="mainstore.snackbarTimeout"
          content-class="centered-text"
        >
          {{ mainstore.snackbarText }}
        </v-snackbar>
        <v-snackbar
          v-model="showBanner"
          color="secondary"
          location="top"
          timeout="-1"
          :multi-line="true"
        >
          There's been an update to the application. Click refresh to get the
          new changes!
          <template v-slot:actions>
            <v-btn color="primary" variant="text" @click="showBanner = false">
              Close
            </v-btn>
            <v-btn color="primary" variant="text" @click="reloadPage"
              >Refresh</v-btn
            >
          </template>
        </v-snackbar>
      </div>
    </v-sheet>
  </v-app>
</template>

<script setup>
import AppNavigationVue from "./views/AppNavigationVue.vue";
import { useMainStore } from "@/stores/main";
import { onMounted, computed, ref, watch, onUnmounted } from "vue";
import { useVersion } from "@/composables/versionComposable";
import { VueQueryDevtools } from "@tanstack/vue-query-devtools";

const reloadPage = () => {
  window.location.reload();
};
const mainstore = useMainStore();
const { prefetchVersion, version } = useVersion();
const showBanner = ref(false);

const checkVersion = computed(() => {
  return version.value && version.value.version_number !== "0.0.7";
});

const updateBanner = () => {
  showBanner.value = checkVersion.value;
};

onMounted(() => {
  prefetchVersion();

  // Check version initially
  updateBanner();

  const handleVisibilityChange = () => {
    if (!document.hidden) {
      prefetchVersion().then(() => {
        updateBanner();
      });
    }
  };

  document.addEventListener("visibilitychange", handleVisibilityChange);

  // Clean up the event listener when the component is unmounted
  onUnmounted(() => {
    document.removeEventListener("visibilitychange", handleVisibilityChange);
  });
});

// Watch for changes in the computed property
watch(checkVersion, newValue => {
  showBanner.value = newValue;
});
</script>
<style scoped>
.background-image {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%; /* Full screen height */
  background-image: url("@/assets/background.jpg"); /* Replace with your image path */
  background-size: cover;
  background-position: center;
  background-attachment: fixed; /* For the parallax effect */
  overflow: auto; /* Enables scrolling */
  scrollbar-width: none;
  -ms-overflow-style: none;
}

.background-image::-webkit-scrollbar {
  width: 0; /* Remove scrollbar space for Chrome, Safari, and Edge */
  height: 0;
  display: none; /* Completely hide the scrollbar */
}

html {
  scroll-behavior: smooth;
}
</style>

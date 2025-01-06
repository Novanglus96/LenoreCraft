<template>
  <v-app>
    <VueQueryDevtools />
    <AppNavigationVue />
    <v-main>
      <v-container class="bg-primary h-100" fluid>
        <router-view />
      </v-container>
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
        There's been an update to the application. Click refresh to get the new
        changes!
        <template v-slot:actions>
          <v-btn color="primary" variant="text" @click="showBanner = false">
            Close
          </v-btn>
          <v-btn color="primary" variant="text" @click="reloadPage"
            >Refresh</v-btn
          >
        </template>
      </v-snackbar>
    </v-main>
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
  return version.value && version.value.version_number !== "0.0.0";
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

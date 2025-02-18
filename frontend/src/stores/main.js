import { defineStore } from "pinia";

export const useMainStore = defineStore("main", {
  state: () => ({
    snackbarText: "",
    snackbarColor: "",
    snackbar: false,
    snackbarTimeout: 1500,
    projectlist_pagination: {
      page: 1,
      page_size: 2,
      dash: false,
    },
  }),
  getters: {},
  actions: {
    async showSnackbar(text, color) {
      this.snackbarText = text;
      this.snackbarColor = color;
      this.snackbar = true;
    },
    updatePagination(pagination) {
      this.projectlist_pagination = {
        ...this.projectlist_pagination,
        ...pagination,
      };
    },
  },
  persist: true,
});

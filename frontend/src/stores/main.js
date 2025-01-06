import { defineStore } from "pinia";

export const useMainStore = defineStore("main", {
  state: () => ({
    snackbarText: "",
    snackbarColor: "",
    snackbar: false,
    snackbarTimeout: 1500,
  }),
  getters: {},
  actions: {
    async showSnackbar(text, color) {
      this.snackbarText = text;
      this.snackbarColor = color;
      this.snackbar = true;
    },
  },
  persist: true,
});

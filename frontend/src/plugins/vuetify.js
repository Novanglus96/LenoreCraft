import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import { aliases, mdi } from "vuetify/iconsets/mdi";
import "@mdi/font/css/materialdesignicons.css";
import { VDateInput } from "vuetify/labs/VDateInput"; // Import the lab component

const myCustomLightTheme = {
  dark: false,
  colors: {
    primary: "#664200",
    secondary: "#fff2bf",
    accent: "#ffe480",
    error: "#FF3407",
    warning: "#ffc107",
    info: "#795548",
    success: "#4caf50",
    selected: "#7fb17f",
    background: "transparent",
  },
};

export default createVuetify({
  theme: {
    defaultTheme: "myCustomLightTheme",
    variations: {
      colors: ["primary", "secondary", "accent"],
      lighten: 3,
      darken: 3,
    },
    themes: {
      myCustomLightTheme,
    },
  },
  icons: {
    defaultSet: "mdi",
    aliases,
    sets: {
      mdi,
    },
  },
  components: {
    ...components, // Spread the default Vuetify components
    VDateInput, // Add the lab component
  },
  directives,
});

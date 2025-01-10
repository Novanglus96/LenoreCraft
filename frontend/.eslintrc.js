export default {
  root: true,
  env: {
    node: true,
  },
  extends: ["plugin:vue/vue3-essential", "eslint:recommended", "prettier"],
  parserOptions: {
    parser: "@babel/eslint-parser",
  },
  rules: {
    "no-console": import.meta.env.MODE === "production" ? "warn" : "off",
    "no-debugger": import.meta.env.MODE === "production" ? "warn" : "off",
    "vue/valid-v-slot": [
      "error",
      {
        allowModifiers: true,
      },
    ],
  },
};

export function useApiKey() {
  const runtimeKey = window.__APP_CONFIG__?.VITE_API_KEY;

  // Ignore the placeholder value
  if (runtimeKey && runtimeKey !== "__VITE_API_KEY__") {
    return runtimeKey;
  }

  return import.meta.env.VITE_API_KEY;
}

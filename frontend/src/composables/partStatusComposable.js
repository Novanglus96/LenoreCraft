import { useQuery, useQueryClient } from "@tanstack/vue-query";
import axios from "axios";
import { useMainStore } from "@/stores/main";

const apiClient = axios.create({
  baseURL: "/api/v1",
  withCredentials: false,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
    Authorization: `Bearer ${
      window.VITE_API_KEY === "__VITE_API_KEY__"
        ? import.meta.env.VITE_API_KEY // Fallback to the environment variable if the value is the default placeholder
        : window.VITE_API_KEY // Otherwise, use the value in window.VITE_API_KEY
    }`,
  },
});

function handleApiError(error, message) {
  const mainstore = useMainStore();
  if (error.response) {
    console.error("Response error:", error.response.data);
    console.error("Status code:", error.response.status);
    console.error("Headers", error.response.headers);
  } else if (error.request) {
    console.error("No response received:", error.request);
  } else {
    console.error("Error during request setup:", error.message);
  }
  mainstore.showSnackbar(message + " : " + error.response.data.detail, "error");
  throw error;
}

async function getPartStatusesFunction() {
  try {
    const response = await apiClient.get("/part/part_status/list");
    return response.data;
  } catch (error) {
    handleApiError(error, "PartStatuses not fetched: ");
  }
}

export function usePartStatuses() {
  const queryClient = useQueryClient();
  const { data: part_statuses, isLoading } = useQuery({
    queryKey: ["part_statuses"],
    queryFn: () => getPartStatusesFunction(),
    select: response => response,
    client: queryClient,
  });

  return {
    isLoading,
    part_statuses,
  };
}

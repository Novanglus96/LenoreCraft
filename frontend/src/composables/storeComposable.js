import { useQuery, useQueryClient, useMutation } from "@tanstack/vue-query";
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

async function getStoresFunction() {
  try {
    const response = await apiClient.get("/material/store/list");
    return response.data;
  } catch (error) {
    handleApiError(error, "Stores not fetched: ");
  }
}

async function createStoreFunction(newStore) {
  const mainstore = useMainStore();
  try {
    const response = await apiClient.post("/material/store/create", newStore);
    mainstore.showSnackbar("Store created successfully!", "success");
    return response.data;
  } catch (error) {
    handleApiError(error, "Store not created: ");
  }
}

async function deleteStoreFunction(deletedStore) {
  const mainstore = useMainStore();
  try {
    const response = await apiClient.delete(
      "/material/store/delete/" + deletedStore,
    );
    mainstore.showSnackbar("Store deleted successfully!", "success");
    return response.data;
  } catch (error) {
    handleApiError(error, "Store not deleted: ");
  }
}

async function updateStoreFunction(updatedStore) {
  try {
    const response = await apiClient.patch(
      "/material/store/update/" + updatedStore.id,
      updatedStore,
    );
    return response.data;
  } catch (error) {
    handleApiError(error, "Store not updated: ");
  }
}

export function useStores() {
  const queryClient = useQueryClient();
  const { data: stores, isLoading } = useQuery({
    queryKey: ["stores"],
    queryFn: () => getStoresFunction(),
    select: response => response,
    client: queryClient,
  });

  const createStoreMutation = useMutation({
    mutationFn: createStoreFunction,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["stores"] });
    },
  });

  const updateStoreMutation = useMutation({
    mutationFn: updateStoreFunction,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["stores"] });
    },
  });

  const deleteStoreMutation = useMutation({
    mutationFn: deleteStoreFunction,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["stores"] });
    },
  });

  async function addStore(newStore) {
    createStoreMutation.mutate(newStore);
  }

  async function editStore(updatedStore) {
    updateStoreMutation.mutate(updatedStore);
  }

  async function removeStore(deletedStore) {
    deleteStoreMutation.mutate(deletedStore);
  }

  return {
    isLoading,
    stores,
    addStore,
    editStore,
    removeStore,
  };
}

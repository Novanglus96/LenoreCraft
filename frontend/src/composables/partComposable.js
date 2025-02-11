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

async function getPartsFunction() {
  try {
    const response = await apiClient.get("/part/part/list");
    return response.data;
  } catch (error) {
    handleApiError(error, "Parts not fetched: ");
  }
}

async function createPartFunction(newPart) {
  const mainstore = useMainStore();
  try {
    const response = await apiClient.post("/part/part/create", newPart);
    mainstore.showSnackbar("Part created successfully!", "success");
    return response.data;
  } catch (error) {
    handleApiError(error, "Part not created: ");
  }
}

async function deletePartFunction(deletedPart) {
  const mainstore = useMainStore();
  try {
    const response = await apiClient.delete("/part/part/delete/" + deletedPart);
    mainstore.showSnackbar("Part deleted successfully!", "success");
    return response.data;
  } catch (error) {
    handleApiError(error, "Part not deleted: ");
  }
}

async function updatePartFunction(updatedPart) {
  try {
    const response = await apiClient.patch(
      "/part/part/update/" + updatedPart.id,
      updatedPart,
    );
    return response.data;
  } catch (error) {
    handleApiError(error, "Part not updated: ");
  }
}

export function useParts() {
  const queryClient = useQueryClient();
  const { data: parts, isLoading } = useQuery({
    queryKey: ["parts"],
    queryFn: () => getPartsFunction(),
    select: response => response,
    client: queryClient,
  });

  const createPartMutation = useMutation({
    mutationFn: createPartFunction,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["parts"] });
    },
  });

  const updatePartMutation = useMutation({
    mutationFn: updatePartFunction,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["parts"] });
    },
  });

  const deletePartMutation = useMutation({
    mutationFn: deletePartFunction,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["parts"] });
    },
  });

  async function addPart(newPart) {
    createPartMutation.mutate(newPart);
  }

  async function editPart(updatedPart) {
    updatePartMutation.mutate(updatedPart);
  }

  async function removePart(deletedPart) {
    deletePartMutation.mutate(deletedPart);
  }

  return {
    isLoading,
    parts,
    addPart,
    editPart,
    removePart,
  };
}

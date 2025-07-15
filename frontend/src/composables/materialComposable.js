import { useQuery, useQueryClient, useMutation } from "@tanstack/vue-query";
import axios from "axios";
import { useMainStore } from "@/stores/main";
import { useApiKey } from "./ueApiKey";

const apiKey = useApiKey();

const apiClient = axios.create({
  baseURL: "/api/v1",
  withCredentials: false,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
    Authorization: `Bearer ${apiKey}`,
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

async function getMaterialsFunction() {
  try {
    const response = await apiClient.get("/material/material/list");
    return response.data;
  } catch (error) {
    handleApiError(error, "Materials not fetched: ");
  }
}

async function createMaterialFunction(newMaterial) {
  const mainstore = useMainStore();
  try {
    const response = await apiClient.post(
      "/material/material/create",
      newMaterial,
    );
    mainstore.showSnackbar("Material created successfully!", "success");
    return response.data;
  } catch (error) {
    handleApiError(error, "Material not created: ");
  }
}

async function deleteMaterialFunction(deletedMaterial) {
  const mainstore = useMainStore();
  try {
    const response = await apiClient.delete(
      "/material/material/delete/" + deletedMaterial,
    );
    mainstore.showSnackbar("Material deleted successfully!", "success");
    return response.data;
  } catch (error) {
    handleApiError(error, "Material not deleted: ");
  }
}

async function updateMaterialFunction(updatedMaterial) {
  try {
    const response = await apiClient.patch(
      "/material/material/update/" + updatedMaterial.id,
      updatedMaterial,
    );
    return response.data;
  } catch (error) {
    handleApiError(error, "Material not updated: ");
  }
}

export function useMaterials() {
  const queryClient = useQueryClient();
  const { data: materials, isLoading } = useQuery({
    queryKey: ["materials"],
    queryFn: () => getMaterialsFunction(),
    select: response => response,
    client: queryClient,
  });

  const createMaterialMutation = useMutation({
    mutationFn: createMaterialFunction,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["materials"] });
    },
  });

  const updateMaterialMutation = useMutation({
    mutationFn: updateMaterialFunction,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["materials"] });
    },
  });

  const deleteMaterialMutation = useMutation({
    mutationFn: deleteMaterialFunction,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["materials"] });
    },
  });

  async function addMaterial(newMaterial) {
    createMaterialMutation.mutate(newMaterial);
  }

  async function editMaterial(updatedMaterial) {
    updateMaterialMutation.mutate(updatedMaterial);
  }

  async function removeMaterial(deletedMaterial) {
    deleteMaterialMutation.mutate(deletedMaterial);
  }

  return {
    isLoading,
    materials,
    addMaterial,
    editMaterial,
    removeMaterial,
  };
}

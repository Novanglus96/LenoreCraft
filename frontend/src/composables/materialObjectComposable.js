import { useQuery, useQueryClient, useMutation } from "@tanstack/vue-query";
import axios from "axios";
import { useMainStore } from "@/stores/main";

const apiClient = axios.create({
  baseURL: "/api/v1",
  withCredentials: false,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
    Authorization: `Bearer ${window.__APP_CONFIG__?.VITE_API_KEY}`,
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

async function getMaterialObjectsFunction() {
  try {
    const response = await apiClient.get("/material/material_object/list");
    return response.data;
  } catch (error) {
    handleApiError(error, "MaterialObjects not fetched: ");
  }
}

async function createMaterialObjectFunction(newMaterialObject) {
  const mainstore = useMainStore();
  try {
    const response = await apiClient.post(
      "/material/material_object/create",
      newMaterialObject,
    );
    mainstore.showSnackbar("MaterialObject created successfully!", "success");
    return response.data;
  } catch (error) {
    handleApiError(error, "MaterialObject not created: ");
  }
}

async function deleteMaterialObjectFunction(deletedMaterialObject) {
  const mainstore = useMainStore();
  try {
    const response = await apiClient.delete(
      "/material/material_object/delete/" + deletedMaterialObject,
    );
    mainstore.showSnackbar("MaterialObject deleted successfully!", "success");
    return response.data;
  } catch (error) {
    handleApiError(error, "MaterialObject not deleted: ");
  }
}

async function updateMaterialObjectFunction(updatedMaterialObject) {
  try {
    const response = await apiClient.patch(
      "/material/material_object/update/" + updatedMaterialObject.id,
      updatedMaterialObject,
    );
    return response.data;
  } catch (error) {
    handleApiError(error, "MaterialObject not updated: ");
  }
}

export function useMaterialObjects() {
  const queryClient = useQueryClient();
  const { data: material_objects, isLoading } = useQuery({
    queryKey: ["material_objects"],
    queryFn: () => getMaterialObjectsFunction(),
    select: response => response,
    client: queryClient,
  });

  const createMaterialObjectMutation = useMutation({
    mutationFn: createMaterialObjectFunction,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["material_objects"] });
    },
  });

  const updateMaterialObjectMutation = useMutation({
    mutationFn: updateMaterialObjectFunction,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["material_objects"] });
    },
  });

  const deleteMaterialObjectMutation = useMutation({
    mutationFn: deleteMaterialObjectFunction,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["material_objects"] });
    },
  });

  async function addMaterialObject(newMaterialObject) {
    createMaterialObjectMutation.mutate(newMaterialObject);
  }

  async function editMaterialObject(updatedMaterialObject) {
    updateMaterialObjectMutation.mutate(updatedMaterialObject);
  }

  async function removeMaterialObject(deletedMaterialObject) {
    deleteMaterialObjectMutation.mutate(deletedMaterialObject);
  }

  return {
    isLoading,
    material_objects,
    addMaterialObject,
    editMaterialObject,
    removeMaterialObject,
  };
}

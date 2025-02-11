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

async function getProjectsFunction() {
  try {
    const response = await apiClient.get("/project/project/list");
    return response.data;
  } catch (error) {
    handleApiError(error, "Projects not fetched: ");
  }
}

async function createProjectFunction(newProject) {
  const mainstore = useMainStore();
  try {
    const response = await apiClient.post(
      "/project/project/create",
      newProject,
    );
    mainstore.showSnackbar("Project created successfully!", "success");
    return response.data;
  } catch (error) {
    handleApiError(error, "Project not created: ");
  }
}

async function deleteProjectFunction(deletedProject) {
  const mainstore = useMainStore();
  try {
    const response = await apiClient.delete(
      "/project/project/delete/" + deletedProject,
    );
    mainstore.showSnackbar("Project deleted successfully!", "success");
    return response.data;
  } catch (error) {
    handleApiError(error, "Project not deleted: ");
  }
}

async function updateProjectFunction(updatedProject) {
  try {
    const response = await apiClient.patch(
      "/project/project/update/" + updatedProject.id,
      updatedProject,
    );
    return response.data;
  } catch (error) {
    handleApiError(error, "Project not updated: ");
  }
}

export function useProjects() {
  const queryClient = useQueryClient();
  const { data: projects, isLoading } = useQuery({
    queryKey: ["projects"],
    queryFn: () => getProjectsFunction(),
    select: response => response,
    client: queryClient,
  });

  const createProjectMutation = useMutation({
    mutationFn: createProjectFunction,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["projects"] });
    },
  });

  const updateProjectMutation = useMutation({
    mutationFn: updateProjectFunction,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["projects"] });
    },
  });

  const deleteProjectMutation = useMutation({
    mutationFn: deleteProjectFunction,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["projects"] });
    },
  });

  async function addProject(newProject) {
    createProjectMutation.mutate(newProject);
  }

  async function editProject(updatedProject) {
    updateProjectMutation.mutate(updatedProject);
  }

  async function removeProject(deletedProject) {
    deleteProjectMutation.mutate(deletedProject);
  }

  return {
    isLoading,
    projects,
    addProject,
    editProject,
    removeProject,
  };
}

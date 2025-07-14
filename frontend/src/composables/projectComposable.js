import {
  useQuery,
  useQueryClient,
  useMutation,
  keepPreviousData,
} from "@tanstack/vue-query";
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

async function getProjectsFunction(pagination) {
  try {
    const response = await apiClient.get(
      "/project/project/list?dash=" +
        pagination.dash +
        "&page=" +
        pagination.page +
        "&page_size=" +
        pagination.page_size,
    );
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
  const mainstore = useMainStore();
  const {
    data: projects,
    isLoading,
    isFetching,
  } = useQuery({
    queryKey: ["projects", mainstore.projectlist_pagination],
    queryFn: () => getProjectsFunction(mainstore.projectlist_pagination),
    placeholderData: keepPreviousData,
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
    isFetching,
    projects,
    addProject,
    editProject,
    removeProject,
  };
}

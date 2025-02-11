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

async function getTasksFunction() {
  try {
    const response = await apiClient.get("/task/task/list");
    return response.data;
  } catch (error) {
    handleApiError(error, "Tasks not fetched: ");
  }
}

async function createTaskFunction(newTask) {
  const mainstore = useMainStore();
  try {
    const response = await apiClient.post("/task/task/create", newTask);
    mainstore.showSnackbar("Task created successfully!", "success");
    return response.data;
  } catch (error) {
    handleApiError(error, "Task not created: ");
  }
}

async function deleteTaskFunction(deletedTask) {
  const mainstore = useMainStore();
  try {
    const response = await apiClient.delete("/task/task/delete/" + deletedTask);
    mainstore.showSnackbar("Task deleted successfully!", "success");
    return response.data;
  } catch (error) {
    handleApiError(error, "Task not deleted: ");
  }
}

async function updateTaskFunction(updatedTask) {
  try {
    const response = await apiClient.patch(
      "/task/task/update/" + updatedTask.id,
      updatedTask,
    );
    return response.data;
  } catch (error) {
    handleApiError(error, "Task not updated: ");
  }
}

export function useTasks() {
  const queryClient = useQueryClient();
  const { data: tasks, isLoading } = useQuery({
    queryKey: ["tasks"],
    queryFn: () => getTasksFunction(),
    select: response => response,
    client: queryClient,
  });

  const createTaskMutation = useMutation({
    mutationFn: createTaskFunction,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["tasks"] });
    },
  });

  const updateTaskMutation = useMutation({
    mutationFn: updateTaskFunction,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["tasks"] });
    },
  });

  const deleteTaskMutation = useMutation({
    mutationFn: deleteTaskFunction,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["tasks"] });
    },
  });

  async function addTask(newTask) {
    createTaskMutation.mutate(newTask);
  }

  async function editTask(updatedTask) {
    updateTaskMutation.mutate(updatedTask);
  }

  async function removeTask(deletedTask) {
    deleteTaskMutation.mutate(deletedTask);
  }

  return {
    isLoading,
    tasks,
    addTask,
    editTask,
    removeTask,
  };
}

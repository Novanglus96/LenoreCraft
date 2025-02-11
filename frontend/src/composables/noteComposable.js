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

async function getNotesFunction() {
  try {
    const response = await apiClient.get("/note/note/list");
    return response.data;
  } catch (error) {
    handleApiError(error, "Notes not fetched: ");
  }
}

async function createNoteFunction(newNote) {
  const mainstore = useMainStore();
  try {
    const response = await apiClient.post("/note/note/create", newNote);
    mainstore.showSnackbar("Note created successfully!", "success");
    return response.data;
  } catch (error) {
    handleApiError(error, "Note not created: ");
  }
}

async function deleteNoteFunction(deletedNote) {
  const mainstore = useMainStore();
  try {
    const response = await apiClient.delete("/note/note/delete/" + deletedNote);
    mainstore.showSnackbar("Note deleted successfully!", "success");
    return response.data;
  } catch (error) {
    handleApiError(error, "Note not deleted: ");
  }
}

async function updateNoteFunction(updatedNote) {
  try {
    const response = await apiClient.patch(
      "/note/note/update/" + updatedNote.id,
      updatedNote,
    );
    return response.data;
  } catch (error) {
    handleApiError(error, "Note not updated: ");
  }
}

export function useNotes() {
  const queryClient = useQueryClient();
  const { data: notes, isLoading } = useQuery({
    queryKey: ["notes"],
    queryFn: () => getNotesFunction(),
    select: response => response,
    client: queryClient,
  });

  const createNoteMutation = useMutation({
    mutationFn: createNoteFunction,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["notes"] });
    },
  });

  const updateNoteMutation = useMutation({
    mutationFn: updateNoteFunction,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["notes"] });
    },
  });

  const deleteNoteMutation = useMutation({
    mutationFn: deleteNoteFunction,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["notes"] });
    },
  });

  async function addNote(newNote) {
    createNoteMutation.mutate(newNote);
  }

  async function editNote(updatedNote) {
    updateNoteMutation.mutate(updatedNote);
  }

  async function removeNote(deletedNote) {
    deleteNoteMutation.mutate(deletedNote);
  }

  return {
    isLoading,
    notes,
    addNote,
    editNote,
    removeNote,
  };
}

export function getTaskStatusColor(task_status) {
  if (task_status) {
    if (task_status.id === 1) {
      // Not Started
      return "white";
    } else if (task_status.id === 2) {
      // In Progress
      return "yellow";
    } else if (task_status.id === 3) {
      // On Hold
      return "blue";
    } else if (task_status.id === 4) {
      // Completed
      return "green";
    } else if (task_status.id === 5) {
      // Cancelled
      return "red";
    }
  } else {
    return "black";
  }
}

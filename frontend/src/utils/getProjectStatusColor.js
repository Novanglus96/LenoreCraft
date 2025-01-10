export function getProjectStatusColor(project_status) {
  if (project_status) {
    if (project_status.id === 1) {
      // In Progress
      return "yellow";
    } else if (project_status.id === 2) {
      // On Hold
      return "blue";
    } else if (project_status.id === 3) {
      // Completed
      return "green";
    } else if (project_status.id === 4) {
      // Cancelled
      return "red";
    }
  } else {
    return "black";
  }
}

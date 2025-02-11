from ninja import Schema
from task.api.schemas.task_status import TaskStatusOut
from project.api.schemas.project import ProjectOut
from project.api.schemas.project_phase import ProjectPhaseOut
from part.api.schemas.part import PartOut
from datetime import date
from typing import List, Optional, Dict, Any, TYPE_CHECKING


# The class TaskOut is a schema for representing Task information
class TaskOut(Schema):
    """
    Schema to represent a Task

    Attributes:
        id (int): The id of the Task.  Required.
        task_name (str): The name of the task. Required. Unique. 254 limit.
        task_status (TaskStatusOut): A reference to a Task Status. Required.
        start_date (Optional[date]): The date this task started. Defaults to None.
        due_date (Optional[date]): The date this task is due. Defaults to None.
        completed_date (Optional[date]): The date this task completed. Defaults to None.
        project (Optional[ProjectOut]): A referece to a Project. Defaults to None.
        phase (Optional[ProjectPhaseOut]): A reference to a Project Phase. Defaults to None.
        step (Optional[int]): The number representing the order of the step. Defaults to None.
        part (Optional[PartOut]): A reference to a Part. Defaults to None.
    """

    id: int
    task_name: str
    task_status: TaskStatusOut
    start_date: Optional[date] = None
    due_date: Optional[date] = None
    completed_date: Optional[date] = None
    project: Optional[ProjectOut] = None
    phase: Optional[ProjectPhaseOut] = None
    step: Optional[int] = None
    part: Optional[PartOut] = None


# The class TaskIn is a schema for validating Task information.
class TaskIn(Schema):
    """
    Schema to validate a Task

    Attributes:
        task_name (str): The name of the task. Required. Unique. 254 limit.
        task_status_id (int): A reference to a Task Status by id. Required.
        start_date (Optional[date]): The date this task started. Defaults to None.
        due_date (Optional[date]): The date this task is due. Defaults to None.
        completed_date (Optional[date]): The date this task completed. Defaults to None.
        project_id (Optional[int]): A referece to a Project by id. Defaults to None.
        phase_id (Optional[int]): A reference to a Project Phase by id. Defaults to None.
        step (Optional[int]): The number representing the order of the step. Defaults to None.
        part (Optional[int]): A reference to a Part by id. Defaults to None.
    """

    task_name: str
    task_status_id: int
    start_date: Optional[date] = None
    due_date: Optional[date] = None
    completed_date: Optional[date] = None
    project_id: Optional[int] = None
    phase_id: Optional[int] = None
    step: Optional[int] = None
    part_id: Optional[int] = None

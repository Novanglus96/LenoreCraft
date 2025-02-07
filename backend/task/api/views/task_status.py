from ninja import Router, Query
from django.db import IntegrityError
from ninja.errors import HttpError
from task.models import TaskStatus
from task.api.schemas.task_status import TaskStatusOut
from django.shortcuts import get_object_or_404
from typing import List
from django.db.models import (
    Case,
    When,
    Q,
    IntegerField,
    Value,
    F,
    CharField,
    Sum,
    Subquery,
    OuterRef,
    FloatField,
    Window,
    ExpressionWrapper,
    DecimalField,
    Func,
    Count,
)
from django.db.models.functions import Concat, Coalesce, Abs
from typing import List, Optional, Dict, Any

task_status_router = Router(tags=["TaskStatus"])


@task_status_router.get(
    "/get/{task_status_id}",
    response=TaskStatusOut,
)
def get_task_status(request, task_status_id: int):
    """
    The function `get_task_status` retrieves the TaskStatus by id

    Endpoint:
        - **Path**: `/api/v1/task/task_status/get/{task_status_id}`
        - **Method**: `GET`
        - **Response Model**: `TaskStatusOut`

    Args:
        request (HttpRequest): The HTTP request object.
        task_status_id (int): The id of the TaskStatus to retrieve.

    Returns:
        (TaskStatusOut): The TaskStatus object

    Raises:
        Http404: If the TaskStatus with the specified ID does not exist.
    """

    try:
        task_status = get_object_or_404(TaskStatus, id=task_status_id)
        return task_status
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")


@task_status_router.get("/list", response=List[TaskStatusOut])
def list_task_statuses(request):
    """
    The function `list_task_statuses` retrieves a list of task_statuses,
    ordered by id ascending.

    Endpoint:
        - **Path**: `/api/v1/task/task_status/list`
        - **Method**: `GET`
        - **Response Model**: `TaskStatusOut`

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        (TaskStatusOut): a list of TaskStatus objects
    """

    try:
        qs = TaskStatus.objects.all().order_by("id")
        return qs
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")

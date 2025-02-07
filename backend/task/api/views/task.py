from ninja import Router, Query
from django.db import IntegrityError
from ninja.errors import HttpError
from task.models import Task
from task.api.schemas.task import (
    TaskIn,
    TaskOut,
)
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

task_router = Router(tags=["Task"])


@task_router.post("/create")
def create_task(request, payload: TaskIn):
    """
    The function `create_task` creates a Task

    Endpoint:
        - **Path**: `/api/v1/task/task/create`
        - **Method**: `POST`

    Args:
        request ():
        payload (TaskIn): An object using schema of TaskIn.

    Returns:
        id (int): returns the id of the created Task
    """

    try:
        task = Task.objects.create(**payload.dict())
        return {"id": task.id}
    except IntegrityError as integrity_error:
        # Check if the integrity error is due to a duplicate
        if "unique constraint" in str(integrity_error).lower():
            raise HttpError(400, "Task already exists")
        else:
            # Log other types of integry errors
            raise HttpError(400, "DB integrity error")
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record creation error")


@task_router.put("/update/{task_id}")
def update_task(request, task_id: int, payload: TaskIn):
    """
    The function `update_task` updates the Task specified by id.

    Endpoint:
        - **Path**: `/api/v1/task/task/get/{task_id}`
        - **Method**: `PUT`

    Args:
        request (HttpRequest): The HTTP request object.
        task_id (int): the id of the Task to update
        payload (TaskIn): a Task object

    Returns:
        success (bool): True

    Raises:
        Http404: If the Task with the specified ID does not exist.
    """

    try:
        task = get_object_or_404(Task, id=task_id)
        task.task_name = payload.task_name
        task.save()
        return {"success": True}
    except IntegrityError as integrity_error:
        # Check if the integrity error is due to a duplicate
        if "unique constraint" in str(integrity_error).lower():
            raise HttpError(400, "Task already exists")
        else:
            # Log other types of integry errors
            raise HttpError(400, "DB integrity error")
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record update error")


@task_router.get(
    "/get/{task_id}",
    response=TaskOut,
)
def get_task(request, task_id: int):
    """
    The function `get_task` retrieves the Task by id

    Endpoint:
        - **Path**: `/api/v1/task/task/get/{task_id}`
        - **Method**: `GET`
        - **Response Model**: `TaskOut`

    Args:
        request (HttpRequest): The HTTP request object.
        task_id (int): The id of the Task to retrieve.

    Returns:
        (TaskOut): The Task object

    Raises:
        Http404: If the Task with the specified ID does not exist.
    """

    try:
        task = get_object_or_404(Task, id=task_id)
        return task
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")


@task_router.get("/list", response=List[TaskOut])
def list_tasks(request):
    """
    The function `list_tasks` retrieves a list of tasks,
    ordered by task_name ascending.

    Endpoint:
        - **Path**: `/api/v1/task/task/list`
        - **Method**: `GET`
        - **Response Model**: `TaskOut`

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        (TaskOut): a list of Task objects
    """

    try:
        qs = Task.objects.all().order_by("task_name")
        return qs
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")


@task_router.delete("/delete/{task_id}")
def delete_task(request, task_id: int):
    """
    The function `delete_task` deletes the Task specified by id.

    Endpoint:
        - **Path**: `/api/v1/task/task/delete/{task_id}`
        - **Method**: `DELETE`

    Args:
        request (HttpRequest): The HTTP request object.
        task_id (int): the id of the Task to delete

    Returns:
        success (bool): True

    Raises:
        Http404: If the Task with the specified ID does not exist.
    """

    try:
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return {"success": True}
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")

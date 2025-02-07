from ninja import Router, Query
from django.db import IntegrityError
from ninja.errors import HttpError
from project.models import ProjectStatus
from project.api.schemas.project_status import ProjectStatusOut
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

project_status_router = Router(tags=["ProjectStatus"])


@project_status_router.get(
    "/get/{project_status_id}",
    response=ProjectStatusOut,
)
def get_project_status(request, project_status_id: int):
    """
    The function `get_project_status` retrieves the ProjectStatus by id

    Endpoint:
        - **Path**: `/api/v1/project/project_status/get/{project_status_id}`
        - **Method**: `GET`
        - **Response Model**: `ProjectStatusOut`

    Args:
        request (HttpRequest): The HTTP request object.
        project_status_id (int): The id of the ProjectStatus to retrieve.

    Returns:
        (ProjectStatusOut): The ProjectStatus object

    Raises:
        Http404: If the ProjectStatus with the specified ID does not exist.
    """

    try:
        project_status = get_object_or_404(ProjectStatus, id=project_status_id)
        return project_status
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")


@project_status_router.get("/list", response=List[ProjectStatusOut])
def list_project_statuses(request):
    """
    The function `list_project_statuses` retrieves a list of project_statuses,
    ordered by project_status_name ascending.

    Endpoint:
        - **Path**: `/api/v1/project/project_status/list`
        - **Method**: `GET`
        - **Response Model**: `ProjectStatusOut`

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        (ProjectStatusOut): a list of ProjectStatus objects
    """

    try:
        qs = ProjectStatus.objects.all().order_by("project_status_name")
        return qs
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")

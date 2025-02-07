from ninja import Router, Query
from django.db import IntegrityError
from ninja.errors import HttpError
from project.models import ProjectPhase
from project.api.schemas.project_phase import ProjectPhaseOut
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

project_phase_router = Router(tags=["ProjectPhase"])


@project_phase_router.get(
    "/get/{project_phase_id}",
    response=ProjectPhaseOut,
)
def get_project_phase(request, project_phase_id: int):
    """
    The function `get_project_phase` retrieves the ProjectPhase by id

    Endpoint:
        - **Path**: `/api/v1/project/project_phase/get/{project_phase_id}`
        - **Method**: `GET`
        - **Response Model**: `ProjectPhaseOut`

    Args:
        request (HttpRequest): The HTTP request object.
        project_phase_id (int): The id of the ProjectPhase to retrieve.

    Returns:
        (ProjectPhaseOut): The ProjectPhase object

    Raises:
        Http404: If the ProjectPhase with the specified ID does not exist.
    """

    try:
        project_phase = get_object_or_404(ProjectPhase, id=project_phase_id)
        return project_phase
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")


@project_phase_router.get("/list", response=List[ProjectPhaseOut])
def list_project_phases(request):
    """
    The function `list_project_phases` retrieves a list of project_phases,
    ordered by id ascending.

    Endpoint:
        - **Path**: `/api/v1/project/project_phase/list`
        - **Method**: `GET`
        - **Response Model**: `ProjectPhaseOut`

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        (ProjectPhaseOut): a list of ProjectPhase objects
    """

    try:
        qs = ProjectPhase.objects.all().order_by("id")
        return qs
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")

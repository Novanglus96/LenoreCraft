from ninja import Router, Query
from django.db import IntegrityError
from ninja.errors import HttpError
from project.models import Project
from project.api.schemas.project import ProjectIn, ProjectOut, PaginatedProjects
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
from administration.api.dependencies.paginate_list import paginate_list

project_router = Router(tags=["Project"])


@project_router.post("/create")
def create_project(request, payload: ProjectIn):
    """
    The function `create_project` creates a Project

    Endpoint:
        - **Path**: `/api/v1/project/project/create`
        - **Method**: `POST`

    Args:
        request ():
        payload (ProjectIn): An object using schema of ProjectIn.

    Returns:
        id (int): returns the id of the created Project
    """

    try:
        project = Project.objects.create(**payload.dict())
        return {"id": project.id}
    except IntegrityError as integrity_error:
        # Check if the integrity error is due to a duplicate
        if "unique constraint" in str(integrity_error).lower():
            raise HttpError(400, "Project already exists")
        else:
            # Log other types of integry errors
            raise HttpError(400, "DB integrity error")
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record creation error")


@project_router.put("/update/{project_id}")
def update_project(request, project_id: int, payload: ProjectIn):
    """
    The function `update_project` updates the Project specified by id.

    Endpoint:
        - **Path**: `/api/v1/project/project/get/{project_id}`
        - **Method**: `PUT`

    Args:
        request (HttpRequest): The HTTP request object.
        project_id (int): the id of the Project to update
        payload (ProjectIn): a Project object

    Returns:
        success (bool): True

    Raises:
        Http404: If the Project with the specified ID does not exist.
    """

    try:
        project = get_object_or_404(Project, id=project_id)
        project.project_name = payload.project_name
        project.save()
        return {"success": True}
    except IntegrityError as integrity_error:
        # Check if the integrity error is due to a duplicate
        if "unique constraint" in str(integrity_error).lower():
            raise HttpError(400, "Project already exists")
        else:
            # Log other types of integry errors
            raise HttpError(400, "DB integrity error")
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record update error")


@project_router.get(
    "/get/{project_id}",
    response=ProjectOut,
)
def get_project(request, project_id: int):
    """
    The function `get_project` retrieves the Project by id

    Endpoint:
        - **Path**: `/api/v1/project/project/get/{project_id}`
        - **Method**: `GET`
        - **Response Model**: `ProjectOut`

    Args:
        request (HttpRequest): The HTTP request object.
        project_id (int): The id of the Project to retrieve.

    Returns:
        (ProjectOut): The Project object

    Raises:
        Http404: If the Project with the specified ID does not exist.
    """

    try:
        project = get_object_or_404(Project, id=project_id)
        return project
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")


@project_router.get("/list", response=PaginatedProjects)
def list_projects(
    request,
    page: Optional[int] = 1,
    page_size: Optional[int] = 10,
    dash: Optional[bool] = False,
):
    """
    The function `list_projects` retrieves a list of projects,
    ordered by project_name ascending.

    Endpoint:
        - **Path**: `/api/v1/project/project/list`
        - **Method**: `GET`
        - **Response Model**: `ProjectOut`

    Args:
        request (HttpRequest): The HTTP request object.
        dash (bool): Filters projects that are not in progress
            or on hold. Defaults to False.

    Returns:
        (ProjectOut): a list of Project objects
    """

    try:
        qs = None
        if dash:
            qs = (
                Project.objects.all()
                .filter(project_status__id__lt=3)
                .order_by("project_status__id", "due_date", "project_name")
            )
        else:
            qs = Project.objects.all().order_by(
                "project_status__id", "due_date", "project_name"
            )

        # Paginate projects
        paginated_list, total_records, total_pages = paginate_list(
            qs, page_size, page
        )
        paginated_obj = PaginatedProjects(
            projects=paginated_list,
            current_page=page,
            total_pages=total_pages,
            total_records=total_records,
        )

        return paginated_obj
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")


@project_router.delete("/delete/{project_id}")
def delete_project(request, project_id: int):
    """
    The function `delete_project` deletes the Project specified by id.

    Endpoint:
        - **Path**: `/api/v1/project/project/delete/{project_id}`
        - **Method**: `DELETE`

    Args:
        request (HttpRequest): The HTTP request object.
        project_id (int): the id of the Project to delete

    Returns:
        success (bool): True

    Raises:
        Http404: If the Project with the specified ID does not exist.
    """

    try:
        project = get_object_or_404(Project, id=project_id)
        project.delete()
        return {"success": True}
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")

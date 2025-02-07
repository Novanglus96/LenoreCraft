from ninja import Router, Query
from django.db import IntegrityError
from ninja.errors import HttpError
from part.models import Part
from part.api.schemas.part import (
    PartIn,
    PartOut,
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

part_router = Router(tags=["Part"])


@part_router.post("/create")
def create_part(request, payload: PartIn):
    """
    The function `create_part` creates a Part

    Endpoint:
        - **Path**: `/api/v1/part/part/create`
        - **Method**: `POST`

    Args:
        request ():
        payload (PartIn): An object using schema of PartIn.

    Returns:
        id (int): returns the id of the created Part
    """

    try:
        part = Part.objects.create(**payload.dict())
        return {"id": part.id}
    except IntegrityError as integrity_error:
        # Check if the integrity error is due to a duplicate
        if "unique constraint" in str(integrity_error).lower():
            raise HttpError(400, "Part already exists")
        else:
            # Log other types of integry errors
            raise HttpError(400, "DB integrity error")
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record creation error")


@part_router.put("/update/{part_id}")
def update_part(request, part_id: int, payload: PartIn):
    """
    The function `update_part` updates the Part specified by id.

    Endpoint:
        - **Path**: `/api/v1/part/part/get/{part_id}`
        - **Method**: `PUT`

    Args:
        request (HttpRequest): The HTTP request object.
        part_id (int): the id of the Part to update
        payload (PartIn): a Part object

    Returns:
        success (bool): True

    Raises:
        Http404: If the Part with the specified ID does not exist.
    """

    try:
        part = get_object_or_404(Part, id=part_id)
        part.part_name = payload.part_name
        part.save()
        return {"success": True}
    except IntegrityError as integrity_error:
        # Check if the integrity error is due to a duplicate
        if "unique constraint" in str(integrity_error).lower():
            raise HttpError(400, "Part already exists")
        else:
            # Log other types of integry errors
            raise HttpError(400, "DB integrity error")
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record update error")


@part_router.get(
    "/get/{part_id}",
    response=PartOut,
)
def get_part(request, part_id: int):
    """
    The function `get_part` retrieves the Part by id

    Endpoint:
        - **Path**: `/api/v1/part/part/get/{part_id}`
        - **Method**: `GET`
        - **Response Model**: `PartOut`

    Args:
        request (HttpRequest): The HTTP request object.
        part_id (int): The id of the Part to retrieve.

    Returns:
        (PartOut): The Part object

    Raises:
        Http404: If the Part with the specified ID does not exist.
    """

    try:
        part = get_object_or_404(Part, id=part_id)
        return part
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")


@part_router.get("/list", response=List[PartOut])
def list_parts(request):
    """
    The function `list_parts` retrieves a list of parts,
    ordered by part_name ascending.

    Endpoint:
        - **Path**: `/api/v1/part/part/list`
        - **Method**: `GET`
        - **Response Model**: `PartOut`

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        (PartOut): a list of Part objects
    """

    try:
        qs = Part.objects.all().order_by("part_name")
        return qs
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")


@part_router.delete("/delete/{part_id}")
def delete_part(request, part_id: int):
    """
    The function `delete_part` deletes the Part specified by id.

    Endpoint:
        - **Path**: `/api/v1/part/part/delete/{part_id}`
        - **Method**: `DELETE`

    Args:
        request (HttpRequest): The HTTP request object.
        part_id (int): the id of the Part to delete

    Returns:
        success (bool): True

    Raises:
        Http404: If the Part with the specified ID does not exist.
    """

    try:
        part = get_object_or_404(Part, id=part_id)
        part.delete()
        return {"success": True}
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")

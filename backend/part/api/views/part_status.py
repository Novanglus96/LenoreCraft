from ninja import Router, Query
from django.db import IntegrityError
from ninja.errors import HttpError
from part.models import PartStatus
from part.api.schemas.part_status import PartStatusOut
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

part_status_router = Router(tags=["PartStatus"])


@part_status_router.get(
    "/get/{part_status_id}",
    response=PartStatusOut,
)
def get_part_status(request, part_status_id: int):
    """
    The function `get_part_status` retrieves the PartStatus by id

    Endpoint:
        - **Path**: `/api/v1/part/part_status/get/{part_status_id}`
        - **Method**: `GET`
        - **Response Model**: `PartStatusOut`

    Args:
        request (HttpRequest): The HTTP request object.
        part_status_id (int): The id of the PartStatus to retrieve.

    Returns:
        (PartStatusOut): The PartStatus object

    Raises:
        Http404: If the PartStatus with the specified ID does not exist.
    """

    try:
        part_status = get_object_or_404(PartStatus, id=part_status_id)
        return part_status
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")


@part_status_router.get("/list", response=List[PartStatusOut])
def list_part_statuses(request):
    """
    The function `list_part_statuses` retrieves a list of part_statuses,
    ordered by id ascending.

    Endpoint:
        - **Path**: `/api/v1/part/part_status/list`
        - **Method**: `GET`
        - **Response Model**: `PartStatusOut`

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        (PartStatusOut): a list of PartStatus objects
    """

    try:
        qs = PartStatus.objects.all().order_by("id")
        return qs
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")

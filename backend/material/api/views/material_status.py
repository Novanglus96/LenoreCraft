from ninja import Router, Query
from django.db import IntegrityError
from ninja.errors import HttpError
from material.models import MaterialStatus
from material.api.schemas.material_status import MaterialStatusOut
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

material_status_router = Router(tags=["Material Status"])


@material_status_router.get(
    "/get/{material_status_id}",
    response=MaterialStatusOut,
)
def get_material_status(request, material_status_id: int):
    """
    The function `get_material_status` retrieves the MaterialStatus by id

    Endpoint:
        - **Path**: `/api/v1/material/material_status/get/{material_status_id}`
        - **Method**: `GET`
        - **Response Model**: `MaterialStatusOut`

    Args:
        request (HttpRequest): The HTTP request object.
        material_status_id (int): The id of the MaterialStatus to retrieve.

    Returns:
        (MaterialStatusOut): The MaterialStatus object

    Raises:
        Http404: If the MaterialStatus with the specified ID does not exist.
    """

    try:
        material_status = get_object_or_404(
            MaterialStatus, id=material_status_id
        )
        return material_status
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")


@material_status_router.get("/list", response=List[MaterialStatusOut])
def list_material_statuses(request):
    """
    The function `list_material_statuses` retrieves a list of material_statuses,
    ordered by id ascending.

    Endpoint:
        - **Path**: `/api/v1/material/material_status/list`
        - **Method**: `GET`
        - **Response Model**: `MaterialStatusOut`

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        (MaterialStatusOut): a list of MaterialStatus objects
    """

    try:
        qs = MaterialStatus.objects.all().order_by("id")
        return qs
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")

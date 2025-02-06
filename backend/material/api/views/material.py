from ninja import Router, Query
from django.db import IntegrityError
from ninja.errors import HttpError
from material.models import Material
from material.api.schemas.material import (
    MaterialIn,
    MaterialOut,
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

material_router = Router(tags=["Material"])


@material_router.post("/create")
def create_material(request, payload: MaterialIn):
    """
    The function `create_material` creates a Material

    Endpoint:
        - **Path**: `/api/v1/material/material/create`
        - **Method**: `POST`

    Args:
        request ():
        payload (MaterialIn): An object using schema of MaterialIn.

    Returns:
        id (int): returns the id of the created Material
    """

    try:
        material = Material.objects.create(**payload.dict())
        return {"id": material.id}
    except IntegrityError as integrity_error:
        # Check if the integrity error is due to a duplicate
        if "unique constraint" in str(integrity_error).lower():
            raise HttpError(400, "Material already exists")
        else:
            # Log other types of integry errors
            raise HttpError(400, "DB integrity error")
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record creation error")


@material_router.put("/update/{material_id}")
def update_material(request, material_id: int, payload: MaterialIn):
    """
    The function `update_material` updates the Material specified by id.

    Endpoint:
        - **Path**: `/api/v1/material/material/get/{material_id}`
        - **Method**: `PUT`

    Args:
        request (HttpRequest): The HTTP request object.
        material_id (int): the id of the Material to update
        payload (MaterialIn): a Material object

    Returns:
        success (bool): True

    Raises:
        Http404: If the Material with the specified ID does not exist.
    """

    try:
        material = get_object_or_404(Material, id=material_id)
        material.material_name = payload.material_object.material_object_name
        material.save()
        return {"success": True}
    except IntegrityError as integrity_error:
        # Check if the integrity error is due to a duplicate
        if "unique constraint" in str(integrity_error).lower():
            raise HttpError(400, "Material already exists")
        else:
            # Log other types of integry errors
            raise HttpError(400, "DB integrity error")
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record update error")


@material_router.get(
    "/get/{material_id}",
    response=MaterialOut,
)
def get_material(request, material_id: int):
    """
    The function `get_material` retrieves the Material by id

    Endpoint:
        - **Path**: `/api/v1/material/material/get/{material_id}`
        - **Method**: `GET`
        - **Response Model**: `MaterialOut`

    Args:
        request (HttpRequest): The HTTP request object.
        material_id (int): The id of the Material to retrieve.

    Returns:
        (MaterialOut): The Material object

    Raises:
        Http404: If the Material with the specified ID does not exist.
    """

    try:
        material = get_object_or_404(Material, id=material_id)
        return material
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")


@material_router.get("/list", response=List[MaterialOut])
def list_materials(request):
    """
    The function `list_materials` retrieves a list of materials,
    ordered by material_name ascending.

    Endpoint:
        - **Path**: `/api/v1/material/material/list`
        - **Method**: `GET`
        - **Response Model**: `MaterialOut`

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        (MaterialOut): a list of Material objects
    """

    try:
        qs = Material.objects.all().order_by(
            "material_object.material_object_name"
        )
        return qs
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")


@material_router.delete("/delete/{material_id}")
def delete_material(request, material_id: int):
    """
    The function `delete_material` deletes the Material specified by id.

    Endpoint:
        - **Path**: `/api/v1/material/material/delete/{material_id}`
        - **Method**: `DELETE`

    Args:
        request (HttpRequest): The HTTP request object.
        material_id (int): the id of the Material to delete

    Returns:
        success (bool): True

    Raises:
        Http404: If the Material with the specified ID does not exist.
    """

    try:
        material = get_object_or_404(Material, id=material_id)
        material.delete()
        return {"success": True}
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")

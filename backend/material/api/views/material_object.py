from ninja import Router, Query
from django.db import IntegrityError
from ninja.errors import HttpError
from material.models import MaterialObject
from material.api.schemas.material_object import (
    MaterialObjectIn,
    MaterialObjectOut,
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

material_object_router = Router(tags=["MaterialObject"])


@material_object_router.post("/create")
def create_material_object(request, payload: MaterialObjectIn):
    """
    The function `create_material_object` creates a MaterialObject

    Endpoint:
        - **Path**: `/api/v1/material/material_object/create`
        - **Method**: `POST`

    Args:
        request ():
        payload (MaterialObjectIn): An object using schema of MaterialObjectIn.

    Returns:
        id (int): returns the id of the created MaterialObject
    """

    try:
        material_object = MaterialObject.objects.create(**payload.dict())
        return {"id": material_object.id}
    except IntegrityError as integrity_error:
        # Check if the integrity error is due to a duplicate
        if "unique constraint" in str(integrity_error).lower():
            raise HttpError(400, "MaterialObject already exists")
        else:
            # Log other types of integry errors
            raise HttpError(400, "DB integrity error")
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record creation error")


@material_object_router.put("/update/{material_object_id}")
def update_material_object(
    request, material_object_id: int, payload: MaterialObjectIn
):
    """
    The function `update_material_object` updates the MaterialObject specified by id.

    Endpoint:
        - **Path**: `/api/v1/material/material_object/get/{material_object_id}`
        - **Method**: `PUT`

    Args:
        request (HttpRequest): The HTTP request object.
        material_object_id (int): the id of the MaterialObject to update
        payload (MaterialObjectIn): a MaterialObject object

    Returns:
        success (bool): True

    Raises:
        Http404: If the MaterialObject with the specified ID does not exist.
    """

    try:
        material_object = get_object_or_404(
            MaterialObject, id=material_object_id
        )
        material_object.material_object_name = payload.material_object_name
        material_object.save()
        return {"success": True}
    except IntegrityError as integrity_error:
        # Check if the integrity error is due to a duplicate
        if "unique constraint" in str(integrity_error).lower():
            raise HttpError(400, "MaterialObject already exists")
        else:
            # Log other types of integry errors
            raise HttpError(400, "DB integrity error")
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record update error")


@material_object_router.get(
    "/get/{material_object_id}",
    response=MaterialObjectOut,
)
def get_material_object(request, material_object_id: int):
    """
    The function `get_material_object` retrieves the MaterialObject by id

    Endpoint:
        - **Path**: `/api/v1/material/material_object/get/{material_object_id}`
        - **Method**: `GET`
        - **Response Model**: `MaterialObjectOut`

    Args:
        request (HttpRequest): The HTTP request object.
        material_object_id (int): The id of the MaterialObject to retrieve.

    Returns:
        (MaterialObjectOut): The MaterialObject object

    Raises:
        Http404: If the MaterialObject with the specified ID does not exist.
    """

    try:
        material_object = get_object_or_404(
            MaterialObject, id=material_object_id
        )
        return material_object
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")


@material_object_router.get("/list", response=List[MaterialObjectOut])
def list_material_objects(request):
    """
    The function `list_material_objects` retrieves a list of material_objects,
    ordered by material_object_name ascending.

    Endpoint:
        - **Path**: `/api/v1/material/material_object/list`
        - **Method**: `GET`
        - **Response Model**: `MaterialObjectOut`

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        (MaterialObjectOut): a list of MaterialObject objects
    """

    try:
        qs = MaterialObject.objects.all().order_by("material_object_name")
        return qs
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")


@material_object_router.delete("/delete/{material_object_id}")
def delete_material_object(request, material_object_id: int):
    """
    The function `delete_material_object` deletes the MaterialObject specified by id.

    Endpoint:
        - **Path**: `/api/v1/material/material_object/delete/{material_object_id}`
        - **Method**: `DELETE`

    Args:
        request (HttpRequest): The HTTP request object.
        material_object_id (int): the id of the MaterialObject to delete

    Returns:
        success (bool): True

    Raises:
        Http404: If the MaterialObject with the specified ID does not exist.
    """

    try:
        material_object = get_object_or_404(
            MaterialObject, id=material_object_id
        )
        material_object.delete()
        return {"success": True}
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")

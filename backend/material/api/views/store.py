from ninja import Router, Query
from django.db import IntegrityError
from ninja.errors import HttpError
from material.models import Store
from material.api.schemas.store import (
    StoreIn,
    StoreOut,
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

store_router = Router(tags=["Stores"])


@store_router.post("/create")
def create_store(request, payload: StoreIn):
    """
    The function `create_store` creates a store

    Endpoint:
        - **Path**: `/api/v1/store/create`
        - **Method**: `POST`

    Args:
        request ():
        payload (StoreIn): An object using schema of StoreIn.

    Returns:
        id (int): returns the id of the created store
    """

    try:
        store = Store.objects.create(**payload.dict())
        return {"id": store.id}
    except IntegrityError as integrity_error:
        # Check if the integrity error is due to a duplicate
        if "unique constraint" in str(integrity_error).lower():
            raise HttpError(400, "Store already exists")
        else:
            # Log other types of integry errors
            raise HttpError(400, "DB integrity error")
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record creation error")


@store_router.put("/update/{store_id}")
def update_store(request, store_id: int, payload: StoreIn):
    """
    The function `update_store` updates the store specified by id.

    Endpoint:
        - **Path**: `/api/v1/store/get/{store_id}`
        - **Method**: `PUT`

    Args:
        request (HttpRequest): The HTTP request object.
        store_id (int): the id of the store to update
        payload (StoreIn): a store object

    Returns:
        success (bool): True

    Raises:
        Http404: If the store with the specified ID does not exist.
    """

    try:
        store = get_object_or_404(Store, id=store_id)
        store.store_name = payload.store_name
        store.save()
        return {"success": True}
    except IntegrityError as integrity_error:
        # Check if the integrity error is due to a duplicate
        if "unique constraint" in str(integrity_error).lower():
            raise HttpError(400, "Store already exists")
        else:
            # Log other types of integry errors
            raise HttpError(400, "DB integrity error")
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record update error")


@store_router.get(
    "/get/{store_id}",
    response=StoreOut,
)
def get_store(request, store_id: int):
    """
    The function `get_store` retrieves the store by id

    Endpoint:
        - **Path**: `/api/v1/store/get/{store_id}`
        - **Method**: `GET`
        - **Response Model**: `StoreOut`

    Args:
        request (HttpRequest): The HTTP request object.
        store_id (int): The id of the store to retrieve.

    Returns:
        (StoreOut): The store object

    Raises:
        Http404: If the store with the specified ID does not exist.
    """

    try:
        store = get_object_or_404(Store, id=store_id)
        return store
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")


@store_router.get("/list", response=List[StoreOut])
def list_stores(request):
    """
    The function `list_stores` retrieves a list of storees,
    ordered by store_name ascending.

    Endpoint:
        - **Path**: `/api/v1/store/list`
        - **Method**: `GET`
        - **Response Model**: `StoreOut`

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        (StoreOut): a list of store objects
    """

    try:
        qs = Store.objects.all().order_by("store_name")
        return qs
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")


@store_router.delete("/delete/{store_id}")
def delete_store(request, store_id: int):
    """
    The function `delete_store` deletes the store specified by id.

    Endpoint:
        - **Path**: `/api/v1/store/delete/{store_id}`
        - **Method**: `DELETE`

    Args:
        request (HttpRequest): The HTTP request object.
        store_id (int): the id of the store to delete

    Returns:
        success (bool): True

    Raises:
        Http404: If the store with the specified ID does not exist.
    """

    try:
        store = get_object_or_404(Store, id=store_id)
        store.delete()
        return {"success": True}
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")

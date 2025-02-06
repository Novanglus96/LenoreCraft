from ninja import Router, Query
from django.db import IntegrityError
from ninja.errors import HttpError
from material.models import WoodSpecies
from material.api.schemas.wood_species import WoodSpeciesOut
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

wood_species_router = Router(tags=["WoodSpecies"])


@wood_species_router.get(
    "/get/{wood_species_id}",
    response=WoodSpeciesOut,
)
def get_wood_species(request, wood_species_id: int):
    """
    The function `get_wood_species` retrieves the WoodSpecies by id

    Endpoint:
        - **Path**: `/api/v1/material/wood_species/get/{wood_species_id}`
        - **Method**: `GET`
        - **Response Model**: `WoodSpeciesOut`

    Args:
        request (HttpRequest): The HTTP request object.
        wood_species_id (int): The id of the WoodSpecies to retrieve.

    Returns:
        (WoodSpeciesOut): The WoodSpecies object

    Raises:
        Http404: If the WoodSpecies with the specified ID does not exist.
    """

    try:
        wood_species = get_object_or_404(WoodSpecies, id=wood_species_id)
        return wood_species
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")


@wood_species_router.get("/list", response=List[WoodSpeciesOut])
def list_wood_species(request):
    """
    The function `list_wood_species` retrieves a list of wood_species,
    ordered by id ascending.

    Endpoint:
        - **Path**: `/api/v1/material/wood_species/list`
        - **Method**: `GET`
        - **Response Model**: `WoodSpeciesOut`

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        (WoodSpeciesOut): a list of WoodSpecies objects
    """

    try:
        qs = WoodSpecies.objects.all().order_by("id")
        return qs
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")

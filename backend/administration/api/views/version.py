from ninja import Router, Query
from django.db import IntegrityError
from ninja.errors import HttpError
from administration.models import Version
from administration.api.schemas.version import VersionOut
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

version_router = Router(tags=["Version"])


@version_router.get("/list", response=VersionOut)
def list_version(request):
    """
    The function `list_version` retrieves the app version number
    from the backend.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        VersionOut: a version object
    """

    try:
        qs = get_object_or_404(Version, id=1)
        return qs
    except Exception as e:
        raise HttpError(500, "Record retrieval error")

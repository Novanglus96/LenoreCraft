from ninja import Router, Query
from django.db import IntegrityError
from ninja.errors import HttpError
from note.models import Note
from note.api.schemas.note import (
    NoteIn,
    NoteOut,
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

note_router = Router(tags=["Note"])


@note_router.post("/create")
def create_note(request, payload: NoteIn):
    """
    The function `create_note` creates a Note

    Endpoint:
        - **Path**: `/api/v1/note/note/create`
        - **Method**: `POST`

    Args:
        request ():
        payload (NoteIn): An object using schema of NoteIn.

    Returns:
        id (int): returns the id of the created Note
    """

    try:
        note = Note.objects.create(**payload.dict())
        return {"id": note.id}
    except IntegrityError as integrity_error:
        # Check if the integrity error is due to a duplicate
        if "unique constraint" in str(integrity_error).lower():
            raise HttpError(400, "Note already exists")
        else:
            # Log other types of integry errors
            raise HttpError(400, "DB integrity error")
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record creation error")


@note_router.put("/update/{note_id}")
def update_note(request, note_id: int, payload: NoteIn):
    """
    The function `update_note` updates the Note specified by id.

    Endpoint:
        - **Path**: `/api/v1/note/note/get/{note_id}`
        - **Method**: `PUT`

    Args:
        request (HttpRequest): The HTTP request object.
        note_id (int): the id of the Note to update
        payload (NoteIn): a Note object

    Returns:
        success (bool): True

    Raises:
        Http404: If the Note with the specified ID does not exist.
    """

    try:
        note = get_object_or_404(Note, id=note_id)
        note.save()
        return {"success": True}
    except IntegrityError as integrity_error:
        # Check if the integrity error is due to a duplicate
        if "unique constraint" in str(integrity_error).lower():
            raise HttpError(400, "Note already exists")
        else:
            # Log other types of integry errors
            raise HttpError(400, "DB integrity error")
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record update error")


@note_router.get(
    "/get/{note_id}",
    response=NoteOut,
)
def get_note(request, note_id: int):
    """
    The function `get_note` retrieves the Note by id

    Endpoint:
        - **Path**: `/api/v1/note/note/get/{note_id}`
        - **Method**: `GET`
        - **Response Model**: `NoteOut`

    Args:
        request (HttpRequest): The HTTP request object.
        note_id (int): The id of the Note to retrieve.

    Returns:
        (NoteOut): The Note object

    Raises:
        Http404: If the Note with the specified ID does not exist.
    """

    try:
        note = get_object_or_404(Note, id=note_id)
        return note
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")


@note_router.get("/list", response=List[NoteOut])
def list_notes(request):
    """
    The function `list_notes` retrieves a list of notes,
    ordered by note_date descending.

    Endpoint:
        - **Path**: `/api/v1/note/note/list`
        - **Method**: `GET`
        - **Response Model**: `NoteOut`

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        (NoteOut): a list of Note objects
    """

    try:
        qs = Note.objects.all().order_by("-note_date")
        return qs
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")


@note_router.delete("/delete/{note_id}")
def delete_note(request, note_id: int):
    """
    The function `delete_note` deletes the Note specified by id.

    Endpoint:
        - **Path**: `/api/v1/note/note/delete/{note_id}`
        - **Method**: `DELETE`

    Args:
        request (HttpRequest): The HTTP request object.
        note_id (int): the id of the Note to delete

    Returns:
        success (bool): True

    Raises:
        Http404: If the Note with the specified ID does not exist.
    """

    try:
        note = get_object_or_404(Note, id=note_id)
        note.delete()
        return {"success": True}
    except Exception as e:
        # Log other types of exceptions
        raise HttpError(500, "Record retrieval error")

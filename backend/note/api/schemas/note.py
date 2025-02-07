from ninja import Schema
from typing import List, Optional, Dict, Any, TYPE_CHECKING
from datetime import date
from pydantic import HttpUrl, Field
from administration.api.dependencies.current_date import current_date
from project.api.schemas.project import ProjectOut


# The class NoteOut is a schema for representing Note information
class NoteOut(Schema):
    """
    Schema to represent a Note

    Attributes:
        id (int): The id of the Note.  Required.
        note (str): The text of the note. Required. 508 limit.
        note_date (date): The date of this note. Required. Defaults to
            current date.
        attachment (Optional[HttpUrl]): An attachment for this note. Defaults
            to None.
        project (Optional[ProjectOut]): A reference to a Project. Defaults to
            None.
    """

    id: int
    note_date: date
    note: str
    attachment: Optional[HttpUrl] = None
    project: Optional[ProjectOut] = None


# The class NoteIn is a schema for validating Note information.
class NoteIn(Schema):
    """
    Schema to validate a Note

    Attributes:
        note_date (date): The date of this note. Required. Defaults to
            current date.
        note (str): The text of the note. Required. 508 limit.
        project_id (Optional[int]): A reference to a Project by ID. Defaults to
            None.
    """

    note_date: date
    note: str
    project_id: Optional[int] = None

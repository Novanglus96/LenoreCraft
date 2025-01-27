from django.db import models
from project.models import Project
import pytz
import os
import datetime
from django.utils import timezone


# Create your models here.
def attachment_name(instance, filename):
    return f"attachments/{filename}"


def current_date():
    today = timezone.now()
    tz_timezone = pytz.timezone(os.environ.get("TIMEZONE"))
    today_tz = today.astimezone(tz_timezone).date()
    return today_tz


class Note(models.Model):
    """
    Model representing a note.

    Fields:
    - note_date (DateField): the date of the note
    - note (CharField): The text of the note
    - attachment (FileField): Any attachment associated with this note
    - project (ForeignKey): A reference to a Project
    """

    note_date = models.DateField(default=current_date)
    note = models.CharField(max_length=508)
    attachment = models.FileField(upload_to=attachment_name)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.note_date.strftime("%Y-%m-%d")

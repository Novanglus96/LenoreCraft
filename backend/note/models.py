from django.db import models
from project.models import Project
import pytz
import os
import datetime
from django.utils import timezone


# Create your models here.
def attachment_name(instance, filename):
    """
    Takes a file instance and returns the attachment path with
    the file name.

    Args:
        instance ():
        filename (String): The name of the file

    Returns:
        (String): The path to attachments with the filename
    """
    return f"attachments/{filename}"


def current_date():
    """
    Gets a timezone adjusted date for todays date.

    Returns:
        (Date): Timezone adjusted date
    """
    today = timezone.now()
    tz_timezone = pytz.timezone(os.environ.get("TIMEZONE"))
    today_tz = today.astimezone(tz_timezone).date()
    return today_tz


class Note(models.Model):
    """
    Model representing a note.

    Attributes:
        note_date (DateField): The date of the note. Required.
        note (CharField): The text of the note. Required.
        attachment (Optional[FileField]): Any attachment associated with this
            note. Dafaults to None.
        project (Optional[ForeignKey]): A reference to a Project. Defaults to
            None.
    """

    note_date = models.DateField(default=current_date)
    note = models.CharField(max_length=508)
    attachment = models.FileField(
        upload_to=attachment_name, null=True, blank=True, default=None
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True, blank=True, default=None
    )

    def __str__(self):
        """
        Returns:
            (String): The Note Date
        """
        return self.note_date.strftime("%Y-%m-%d")

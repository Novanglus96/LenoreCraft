from django.db import models


# Create your models here.
def image_name(instance, filename):
    return f"images/{filename}"


class ProjectStatus(models.Model):
    """

    Model representing a status for projects.

    Attributes:
        project_status (CharField): The text status of a project. Required.  Unique.

    """

    project_status = models.CharField(max_length=254, unique=True)

    class Meta:
        verbose_name_plural = "Project statuses"

    def __str__(self):
        return self.project_status


class Project(models.Model):
    """

    Model representing a project.

    Attributes:
        project_name (CharField): The name of the poject. Required. Unique. 254 limit.
        project_status (ProjectStatus): A reference to a Project Status. Required.
        project_image (Optional[FileField]): An image for the project. Defaults to None.
        start_date (Optional[DateField]): The date this project started. Defaults to None.
        due_date (Optional[DateField]): The date this project is due. Defaults to None.
        completed_date (Optioanl[DateField]): The date this project completed. Defaults to None.
        depth_in (Optional[DecimalField]): The depth in inches. Defaults to 0.
        width_in (Optional[DecimalField]): The width in inches. Defaults to 0.
        height_in (Optional[DecimalField]): The height in inches. Defaults to 0.

    """

    project_name = models.CharField(max_length=254, unique=True)
    project_status = models.ForeignKey(
        ProjectStatus, null=True, on_delete=models.SET_NULL
    )
    project_image = models.FileField(
        upload_to=image_name, default=None, null=True, blank=True
    )
    start_date = models.DateField(null=True, blank=True, default=None)
    due_date = models.DateField(null=True, blank=True, default=None)
    completed_date = models.DateField(null=True, blank=True, default=None)
    depth_in = models.DecimalField(
        max_digits=10, decimal_places=5, null=True, blank=True, default=0
    )
    width_in = models.DecimalField(
        max_digits=10, decimal_places=5, null=True, blank=True, default=0
    )
    height_in = models.DecimalField(
        max_digits=10, decimal_places=5, null=True, blank=True, default=0
    )

    def __str__(self):
        return self.project_name


class ProjectPhase(models.Model):
    """

    Model representing a phase for projects.

    Attributes:
        project_phase (CharField): The text phase of a project. Required. Unique.

    """

    project_phase = models.CharField(max_length=254, unique=True)

    def __str__(self):
        return self.project_phase

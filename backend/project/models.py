from django.db import models


# Create your models here.
def image_name(instance, filename):
    return f"images/{filename}"


class ProjectStatus(models.Model):
    """
    Model representing a status for projects.

    Fields:
    - project_status (CharField): The text status of a project.
    """

    project_status = models.CharField(max_length=254, unique=True)

    class Meta:
        verbose_name_plural = "Project statuses"

    def __str__(self):
        return self.project_status


class Project(models.Model):
    """
    Model representing a project.

    Fields:
    - project_name (CharField): The name of the poject, limited to 254 characters,
    and must be unique.
    - project_status (ForeignKey): A reference to a Project Status.
    - project_image (FileField): An image for the project
    - start_date (DateField): The date this project started
    - due_date (DateField): The date this project is due
    - completed_date (DateField): The date this project completed
    - depth_in (DecimalField): The depth in inches
    - width_in (DecimalField): The width in inches
    - height_in (DecimalField): The height in inches
    """

    project_name = models.CharField(max_length=254, unique=True)
    project_status = models.ForeignKey(
        ProjectStatus, null=True, on_delete=models.SET_NULL
    )
    project_image = models.FileField(upload_to=image_name)
    start_date = models.DateField(null=True, blank=True, default=None)
    due_date = models.DateField(null=True, blank=True, default=None)
    completed_date = models.DateField(null=True, blank=True, default=None)
    depth_in = models.DecimalField(max_digits=10, decimal_places=5)
    width_in = models.DecimalField(max_digits=10, decimal_places=5)
    height_in = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return self.project_name


class ProjectPhase(models.Model):
    """
    Model representing a phase for projects.

    Fields:
    - project_phase (CharField): The text phase of a project.
    """

    project_phase = models.CharField(max_length=254, unique=True)

    def __str__(self):
        return self.project_phase

from django.db import models
from project.models import Project

# Create your models here.


class PartStatus(models.Model):
    """
    Model representing a status for parts.

    Fields:
    - part_status (CharField): The text status of a task.
    """

    part_status = models.CharField(max_length=254, unique=True)

    class Meta:
        verbose_name_plural = "Part statuses"

    def __str__(self):
        return self.part_status


class Part(models.Model):
    """
    Model representing a part.

    Fields:
    - quantity (IntegerField): The quantity of this part
    - part_name (CharField): The name of the part, limited to 254 characters,
    and must be unique.
    - part_status (ForeignKey): A reference to a Part Status.
    - rough_thickness_in (DecimalField): The rough thickness of the part in inches
    - rough_width_in (DecimalField): The rough width of the part in inches
    - rough_length_in (DecimalField): The rough length of the part in inches
    - finished_thickness_in (DecimalField): The finished thickness of the part in inches
    - finished_width_in (DecimalField): The finished width of the part in inches
    - finished_length_in (DecimalField): The finished length of the part in inches
    - project (Foreignkey): A referece to a Project
    """

    quantity = models.IntegerField()
    part_name = models.CharField(max_length=254, unique=True)
    part_status = models.ForeignKey(
        PartStatus, null=True, on_delete=models.SET_NULL
    )
    rough_thickness_in = models.DecimalField(max_digits=10, decimal_places=5)
    rough_width_in = models.DecimalField(max_digits=10, decimal_places=5)
    rough_length_in = models.DecimalField(max_digits=10, decimal_places=5)
    finished_thickness_in = models.DecimalField(max_digits=10, decimal_places=5)
    finished_width_in = models.DecimalField(max_digits=10, decimal_places=5)
    finished_length_in = models.DecimalField(max_digits=10, decimal_places=5)
    project = models.ForeignKey(
        Project, null=True, on_delete=models.SET_NULL, blank=True, default=None
    )

    def __str__(self):
        return self.part_name

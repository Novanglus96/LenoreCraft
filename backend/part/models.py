from django.db import models
from project.models import Project

# Create your models here.


class PartStatus(models.Model):
    """

    Model representing a status for parts.

    Attributes:
        part_status (CharField): The text status of a part. Required.

    """

    part_status = models.CharField(max_length=254, unique=True)

    class Meta:
        verbose_name_plural = "Part statuses"

    def __str__(self):
        return self.part_status


class Part(models.Model):
    """

    Model representing a part.

    Attributes:
        quantity (IntegerField): The quantity of this part. Required.
        part_name (CharField): The name of the part. Required. 254 limit.
        part_status (PartStatus): A reference to a Part Status. Required.
        rough_thickness_in (DecimalField): The rough thickness of the part in inches.
            Required.
        rough_width_in (DecimalField): The rough width of the part in inches. Required.
        rough_length_in (DecimalField): The rough length of the part in inches. Required.
        finished_thickness_in (DecimalField): The finished thickness of the part in inches.
            Required.
        finished_width_in (DecimalField): The finished width of the part in inches. Required.
        finished_length_in (DecimalField): The finished length of the part in inches. Required.
        project (Project): A referece to a Project. Required.

    """

    quantity = models.IntegerField()
    part_name = models.CharField(max_length=254)
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

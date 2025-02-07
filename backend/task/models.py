from django.db import models
from project.models import Project, ProjectPhase
from part.models import Part

# Create your models here.


class TaskStatus(models.Model):
    """

    Model representing a status for projects.

    Attributes:
        task_status (CharField): The text status of a task. Required.

    """

    task_status = models.CharField(max_length=254, unique=True)

    class Meta:
        verbose_name_plural = "Task statuses"

    def __str__(self):
        return self.task_status


class Task(models.Model):
    """

    Model representing a task.

    Attributes:
        task_name (CharField): The name of the task. Required. Unique. 254 limit.
        task_status (TaskStatus): A reference to a Task Status. Required.
        start_date (Optional[DateField]): The date this task started. Defaults to None.
        due_date (Optional[DateField]): The date this task is due. Defaults to None.
        completed_date (Optional[DateField]): The date this task completed. Defaults to None.
        project (Optional[Project]): A referece to a Project. Defaults to None.
        phase (Optional[ProjectPhase]): A reference to a Project Phase. Defaults to None.
        step (Optional[IntegerField]): The number representing the order of the step. Defaults to None.
        part (Optioanl[Part]): A reference to a Part. Defaults to None.

    """

    task_name = models.CharField(max_length=254, unique=True)
    task_status = models.ForeignKey(
        TaskStatus, null=True, on_delete=models.SET_NULL
    )
    start_date = models.DateField(null=True, blank=True, default=None)
    due_date = models.DateField(null=True, blank=True, default=None)
    completed_date = models.DateField(null=True, blank=True, default=None)
    project = models.ForeignKey(
        Project, null=True, on_delete=models.SET_NULL, blank=True, default=None
    )
    phase = models.ForeignKey(
        ProjectPhase,
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        default=None,
    )
    step = models.IntegerField(blank=True, null=True, default=None)
    part = models.ForeignKey(
        Part, null=True, on_delete=models.SET_NULL, blank=True, default=None
    )

    def __str__(self):
        return self.task_name

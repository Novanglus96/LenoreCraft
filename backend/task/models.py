from django.db import models
from project.models import Project

# Create your models here.


class TaskStatus(models.Model):
    """
    Model representing a status for projects.

    Fields:
    - task_status (CharField): The text status of a task.
    """

    task_status = models.CharField(max_length=254, unique=True)

    class Meta:
        verbose_name_plural = "Task statuses"

    def __str__(self):
        return self.task_status


class Task(models.Model):
    """
    Model representing a task.

    Fields:
    - task_name (CharField): The name of the task, limited to 254 characters,
    and must be unique.
    - task_status (ForeignKey): A reference to a Task Status.
    - start_date (DateField): The date this task started
    - due_date (DateField): The date this task is due
    - completed_date (DateField): The date this task completed
    - project (Foreignkey): A referece to a Project
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

    def __str__(self):
        return self.task_name

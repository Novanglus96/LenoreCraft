from django.contrib import admin
from .models import TaskStatus, Task
from django.http import HttpResponse
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class TaskStatusAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id", "task_status"]

    list_display_links = ["task_status"]

    ordering = ["id"]


class TaskAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        "id",
        "task_name",
        "task_status",
        "start_date",
        "due_date",
        "completed_date",
        "project",
    ]

    list_display_links = ["task_name"]

    ordering = ["id"]


admin.site.register(TaskStatus, TaskStatusAdmin)
admin.site.register(Task, TaskAdmin)

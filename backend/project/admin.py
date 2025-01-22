from django.contrib import admin
from .models import ProjectStatus, Project, ProjectPhase
from django.http import HttpResponse
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class ProjectPhaseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id", "project_phase"]

    list_display_links = ["project_phase"]

    ordering = ["id"]


class ProjectStatusAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id", "project_status"]

    list_display_links = ["project_status"]

    ordering = ["id"]


class ProjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        "id",
        "project_name",
        "project_status",
        "start_date",
        "due_date",
        "completed_date",
        "depth_in",
        "width_in",
        "height_in",
    ]

    list_display_links = ["project_name"]

    ordering = ["id"]


admin.site.register(ProjectStatus, ProjectStatusAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectPhase, ProjectPhaseAdmin)

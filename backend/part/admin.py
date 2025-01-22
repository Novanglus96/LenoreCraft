from django.contrib import admin
from .models import Part, PartStatus
from django.http import HttpResponse
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class PartStatusAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id", "part_status"]

    list_display_links = ["part_status"]

    ordering = ["id"]


class PartAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        "id",
        "quantity",
        "part_name",
        "part_status",
        "rough_thickness_in",
        "rough_width_in",
        "rough_length_in",
        "finished_thickness_in",
        "finished_width_in",
        "finished_length_in",
        "project",
    ]

    list_display_links = ["part_name"]

    ordering = ["id"]


admin.site.register(PartStatus, PartStatusAdmin)
admin.site.register(Part, PartAdmin)

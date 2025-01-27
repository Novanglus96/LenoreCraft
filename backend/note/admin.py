from django.contrib import admin
from .models import Note
from django.http import HttpResponse
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class NoteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id", "note_date", "project"]

    list_display_links = ["note_date"]

    ordering = ["-note_date"]


admin.site.register(Note, NoteAdmin)

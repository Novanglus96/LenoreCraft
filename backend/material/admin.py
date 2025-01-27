from django.contrib import admin
from .models import Store, WoodSpecies, MaterialStatus, MaterialObject, Material
from django.http import HttpResponse
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class StoreAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id", "store_name"]

    list_display_links = ["store_name"]

    ordering = ["store_name"]


class WoodSpeciesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id", "wood_species_name"]

    list_display_links = ["wood_species_name"]

    ordering = ["wood_species_name"]


class MaterialStatusAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id", "material_status"]

    list_display_links = ["material_status"]

    ordering = ["id"]


class MaterialObjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        "id",
        "material_object_name",
        "thickness_in",
        "width_in",
        "length_in",
        "wood_species",
        "store",
        "store_aisle",
        "store_bin",
        "store_price",
    ]

    list_display_links = ["material_object_name"]

    ordering = ["id"]


class MaterialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id", "quantity", "material_object", "project"]

    list_display_links = ["material_object"]

    ordering = ["id"]


admin.site.register(Store, StoreAdmin)
admin.site.register(WoodSpecies, WoodSpeciesAdmin)
admin.site.register(MaterialStatus, MaterialStatusAdmin)
admin.site.register(MaterialObject, MaterialObjectAdmin)
admin.site.register(Material, MaterialAdmin)

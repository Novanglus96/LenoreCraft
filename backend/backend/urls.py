"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from administration.api.dependencies.auth import GlobalAuth

# Import routers from apps
from administration.api.routers.version import version_router
from material.api.routers.store import store_router
from material.api.routers.material_status import material_status_router
from material.api.routers.wood_species import wood_species_router
from material.api.routers.material_object import material_object_router
from material.api.routers.material import material_router
from project.api.routers.project_status import project_status_router
from project.api.routers.project import project_router
from project.api.routers.project_phase import project_phase_router
from note.api.routers.note import note_router
from part.api.routers.part_status import part_status_router
from part.api.routers.part import part_router
from task.api.routers.task_status import task_status_router
from task.api.routers.task import task_router

api = NinjaAPI(auth=GlobalAuth())
api.title = "LenoreCraft API"
api.version = "0.0.10"
api.description = "API documentation for LenoreCraft"

# Add routers to the API
api.add_router("/administration/version", version_router)
api.add_router("/material/store", store_router)
api.add_router("/material/material_status", material_status_router)
api.add_router("/material/wood_species", wood_species_router)
api.add_router("/material/material_object", material_object_router)
api.add_router("/material/material", material_router)
api.add_router("/project/project_status", project_status_router)
api.add_router("/project/project", project_router)
api.add_router("/project/project_phase", project_phase_router)
api.add_router("/note/note", note_router)
api.add_router("/part/part_status", part_status_router)
api.add_router("/part/part", part_router)
api.add_router("/task/task_status", task_status_router)
api.add_router("/task/task", task_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", api.urls),
]

admin.site.site_title = "LenoreCraft site admin (DEV)"
admin.site.site_header = "LenoreCraft administration"
admin.site.index_title = "Site administration"

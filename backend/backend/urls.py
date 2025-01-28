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

api = NinjaAPI(auth=GlobalAuth())
api.title = "LenoreCraft API"
api.version = "0.0.002"
api.description = "API documentation for LenoreCraft"

# Add routers to the API
api.add_router("/administration/version", version_router)
api.add_router("/material/store", store_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", api.urls),
]

admin.site.site_title = "LenoreCraft site admin (DEV)"
admin.site.site_header = "LenoreCraft administration"
admin.site.index_title = "Site administration"

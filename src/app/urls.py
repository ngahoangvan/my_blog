"""project-backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version="v1",
        description="Initial API for Jacob's blog",
        terms_of_service="",
        contact=openapi.Contact(email="jacob.hoangv@gmail.com"),
        license=openapi.License(name="Project exclusive license"),
    ),
    public=True,
    permission_classes=[permissions.IsAdminUser],
)

urlpatterns = [
    # App
    path("admin/", admin.site.urls),
    path("auth/", include("authentication.urls")),
    path("users/", include("users.urls")),
    path("skills/", include("skill.urls")),
    path("homepage/", include("homepage.urls")),
    # Swagger
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="Schema Swagger UI"),
    path("redoc", schema_view.with_ui("redoc", cache_timeout=0), name="Schema Redoc"),
]

urlpatterns += staticfiles_urlpatterns()

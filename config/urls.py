"""Root URL configuration for Afrilott."""

from django.urls import include, path

urlpatterns = [
    path("", include("website.urls")),
]

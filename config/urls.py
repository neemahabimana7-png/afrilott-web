"""Root URL configuration for Afrilott."""

from django.urls import include, path

urlpatterns = [
    path("healthz/", include("website.health_urls")),
    path("", include("website.urls")),
]

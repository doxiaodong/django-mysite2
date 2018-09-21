"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path(settings.API_URL, include('api.urls', namespace='api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('markdown/', include('django_markdown.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

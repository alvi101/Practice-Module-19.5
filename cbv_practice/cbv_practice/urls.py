from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.HomeView.as_view(), name='home'),
    path("musician/", include('musician.urls')),
    path("albums/", include('album.urls')),
]

from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.AddAlbum.as_view(), name='add_album'),
    path("edit/<int:pk>/", views.UpdateAlbum.as_view(), name='edit_album'),
]

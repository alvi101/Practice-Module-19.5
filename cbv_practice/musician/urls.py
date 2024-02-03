from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.UserSignup.as_view(), name='register'),
    path("login/", views.user_login.as_view(), name='login'),
    path("logout/", views.user_logout, name='logout'),
    path("profile/", views.UserProfileView.as_view(), name='profile'),
    path("profile/edit/<int:pk>/", views.UpdateUser.as_view(), name='edit_profile'),
]

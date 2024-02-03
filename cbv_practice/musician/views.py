from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here


class UserSignup(CreateView):
    template_name = 'signup.html'
    form_class = RegisterForm
    context_object_name = 'form'
    success_url = reverse_lazy('home')


class user_login(LoginView):
    template_name = 'login.html'


@method_decorator(login_required, name='dispatch')
class UserProfileView(DetailView):
    model = User
    template_name = 'profile.html'

    def get_object(self):
        return self.request.user


@method_decorator(login_required, name='dispatch')
class UpdateUser(UpdateView):
    model = User
    template_name = 'edit_user.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('profile')
    fields = ['username', 'first_name', 'last_name']


def user_logout(request):
    logout(request)
    return redirect('home')

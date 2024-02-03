from django.shortcuts import render
from django.http import HttpResponse
from album.models import Album
from django.views.generic import ListView


def home(request):
    return render(request, 'home.html')


class HomeView(ListView):
    template_name = 'home.html'
    model = Album
    context_object_name = 'albums'

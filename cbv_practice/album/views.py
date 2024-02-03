from django.shortcuts import render
from django.views.generic import CreateView
from .forms import AlbumForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from .models import Album


# Create your views here.

@method_decorator(login_required, name='dispatch')
class AddAlbum(CreateView):
    form_class = AlbumForm
    template_name = 'add_category.html'
    context_object_name = 'form'
    success_url = reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class UpdateAlbum(UpdateView):
    model = Album
    template_name = 'update_album.html'
    pk_url_kwarg = 'pk'
    form_class = AlbumForm
    success_url = reverse_lazy('home')

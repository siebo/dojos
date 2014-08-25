from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.views.generic import CreateView

from .models import Dojo

class ListDojosView(ListView):
    model = Dojo
    template_name = 'dojo_list.html'

class CreateDojoView(CreateView):
    model = Dojo
    template_name = 'edit_dojo.html'

    def get_success_url(self):
        return reverse('dojos-list')
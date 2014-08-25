from django.shortcuts import render
from django.views.generic import ListView 
from .models import Dojo

class ListDojosView(ListView):
    model = Dojo
    
    template_name = 'dojo_list.html'

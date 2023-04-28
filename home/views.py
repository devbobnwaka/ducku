from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.

 
class Index(TemplateView):
    template_name = 'home/index.html'

class AboutUs(TemplateView):
    template_name = 'home/about.html'

class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home/home.html'
from django.forms import models
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import DetailView   
from django.urls import reverse
from main_app.models.blog_model import Blog
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from main_app.models.city_model import City

@method_decorator(login_required, name='dispatch')
class City_View(DetailView):
    model = City
    template_name = 'city/city_show.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        return context

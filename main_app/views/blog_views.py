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


class Blog_Create(CreateView):
    model = Blog
    fields = ['title', 'img', 'post', 'profile', 'city', 'reccomendation']
    template_name = 'user/blog_create.html'
    success_url = '/user/profile'

    def get_initial(self):
        return {'profile': self.kwargs.get("pk")}
        

class Blog_View(DetailView):
    model = Blog 
    template_name='user/blog_show.html'

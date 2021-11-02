from django.forms import models
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
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

@method_decorator(login_required, name='dispatch')
class Blog_View(DetailView):
    model = Blog 
    template_name='blog/blog_show.html'


class Blog_Create(CreateView):
    model = Blog
    fields = ['title', 'img', 'post', 'profile', 'city', 'reccomendation']
    template_name = 'blog/blog_create.html'
    success_url = '/user/profile'

    def get_initial(self):
        return {'profile': self.kwargs.get("pk")}

class Blog_Update(UpdateView):
    model = Blog
    fields = ['title', 'img', 'post', 'reccomendation']
    template_name = 'blog/blog_update.html'
    success_url = '/city'


class Blog_Delete(DeleteView):
    model = Blog
    template_name = 'blog/blog_delete_confirmation.html'
    success_url = '/city'

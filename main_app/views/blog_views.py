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
from main_app.forms import CommentForm
from main_app.models.blog_model import Blog, Comment, Profile 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django import forms


@method_decorator(login_required, name='dispatch')
class Blog_View(DetailView):
    model = Blog 
    template_name='blog/blog_show.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'blog': self.get_object(), 'profile': self.request.user.profile})
        return context

    def post(self, request, *args, **kwargs):
        profile = request.user.profile
        new_comment = Comment(content=request.POST.get('content'), blog=self.get_object(), profile=profile)
        new_comment.save()
        return self.get(self, request, *args, **kwargs)

    def comments(request):
        comments_count = Comment.objects.all()
        return render(request, {'comments_count': comments_count})


class Blog_Create(CreateView):
    model = Blog
    fields = ['title', 'img', 'post', 'profile', 'city', 'reccomendation']
    template_name = 'blog/blog_create.html'
    success_url = '/user/profile'

    def get_initial(self):
        return {'profile': self.kwargs.get("pk"), 'reccomendation' : 1}

class Blog_Update(UpdateView):
    model = Blog
    fields = ['title', 'img', 'post', 'reccomendation']
    template_name = 'blog/blog_update.html'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('blog', kwargs={'pk': pk})


class Blog_Delete(DeleteView):
    model = Blog
    template_name = 'blog/blog_delete_confirmation.html'
    success_url = '/city'

    def get_success_url(self):
        pk = self.object.city.pk
        return reverse('city', kwargs={'pk': pk})


    


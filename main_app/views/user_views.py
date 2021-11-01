from django.forms import models
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, DeleteView  
from django.urls import reverse
from ..models.blog_model import Blog
from ..models.user_model import Profile 
from main_app.models.user_model import User, Profile 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form ssubmit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

class Profile_View(TemplateView):
    #get the users pk and pass it to the url's 
    template_name='user/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] =  Profile.objects.filter(user = self.request.user)
        context['blogs'] = Blog.objects.all()
        return context

class Profile_Update(UpdateView):
    model = Profile
    fields = ['name', 'img', 'cur_city']
    template_name = 'user/profile_update.html'

    def get_success_url(self):
        return reverse('profile')


class Profile_Delete(DeleteView):
    model = Profile
    template_name = 'user/profile_delete_confirmation.html'
    success_url = '/'




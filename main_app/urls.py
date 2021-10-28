from django.urls import path
from . import views
from .models import *
from .views import *

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/',views.Signup.as_view(),name= "signup")
    
    ]
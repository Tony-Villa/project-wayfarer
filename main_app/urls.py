from django.urls import path
from . import views
import .models 

urlpatterns = [
    path('', views.Home.as_view(), name='home')
    ]
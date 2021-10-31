from django.urls import path
from . import views
from .models import *
from .views import *


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/',views.Signup.as_view(),name= "signup"),
    path('user/profile/', views.Profile_View.as_view(), name='profile'),
    path('user/profile/<int:pk>/update', views.Profile_Update.as_view(), name='profile_update'),
    path('user/profile/<int:pk>/delete', views.Profile_Delete.as_view(), name='profile_delete'),
    ]
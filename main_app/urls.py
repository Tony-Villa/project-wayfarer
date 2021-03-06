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
    path('user/profile/<int:pk>/newblog', views.Blog_Create.as_view(), name='blog_create'),
    path('blog/<int:pk>', views.Blog_View.as_view(), name='blog'),
    
    path('blog/<int:pk>/update', views.Blog_Update.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete', views.Blog_Delete.as_view(), name='blog_delete'),
    path('city', views.City_List.as_view(), name='cities'),
    path('city/<int:pk>', views.City_View.as_view(), name='city'),
    path('city/newcity', views.City_Create.as_view(), name='city_create'),
    ]
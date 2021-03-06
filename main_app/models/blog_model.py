from django.db import models
from .user_model import Profile, User
from .rec_model import Reccomendation
from .city_model import City
from django.contrib import admin
from django.db.models.deletion import CASCADE

class Blog(models.Model):
    title = models.CharField(max_length=200, blank=False)
    post = models.TextField(max_length=4000, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    img = models.CharField(max_length=1024, default='https://images.unsplash.com/photo-1601922047316-70884dbbde2f?ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8Y2hpY2FnbyUyMG5pZ2h0fGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=60')
    city = models.ForeignKey(City, on_delete=CASCADE, related_name='cities')
    profile = models.ForeignKey(Profile, on_delete=CASCADE, related_name='profiles')
    reccomendation = models.ManyToManyField(Reccomendation)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=CASCADE, related_name='blogs')
    profile = models.ForeignKey(Profile, on_delete=CASCADE, related_name='comment_profiles')

    def __str__(self):
        return f"${self.profile.name}'s Comment: ${self.content}"
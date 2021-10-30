from django.db import models 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.deletion import CASCADE

class Blog(models.Model):
    title = models.CharField(max_length=200, required=True)
    post = models.TextField(max_length=4000, required=True)
    created_at = models.DateTimeField(auto_now_add=True)
    img = models.CharField(max_length=1024, default='')
    city = models.ForeignKey(City, on_delete=CASCADE, related_name='cities')
    reccomendation = models.ManyToManyField(Reccomendation)
    profile = models.ManyToManyField(Profile)

    def __str__(self):
        return self.title

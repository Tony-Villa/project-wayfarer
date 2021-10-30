from django.db import models
from .user_model import Profile 


class Comment(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    profile = models.ManyToManyField(Profile)
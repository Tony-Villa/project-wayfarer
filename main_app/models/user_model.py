from django.db import models 
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length = 1024)
    cur_city = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return(self.name)

    class Meta:
        ordering = ['name']
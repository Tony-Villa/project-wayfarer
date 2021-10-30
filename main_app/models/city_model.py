from django.db import models
from django.db.models.fields import CharField
 

class City(models.Model):
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=1024)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name 
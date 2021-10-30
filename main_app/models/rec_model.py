from django.db import models 
from django.contrib.auth.models import User


class Reccomendation(models.Model):
    spot_one = models.CharField(max_length=255)
    spot_two = models.CharField(max_length=255)
    spot_three = models.CharField(max_length=255)

    def __str__(self):
        return self.spot_one
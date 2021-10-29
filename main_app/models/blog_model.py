from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ManyToManyField 
from .user_model import Profile

class City:
    def __init__(self, name, img, country):
        self.name = name
        self.img = img
        self.country = country

city = [
    City('Los Angeles', 'https://media.timeout.com/images/105718842/750/562/image.jpg','USA')
]

class Comment:
    def __init__(self, content, created_at, profile):
        self.content = content
        self.created_at = created_at
        self.profile = profile
        

comment = [
    Comment('This place is dope','10/28/21','ZachP')
]

class Recommendation:
    def __init__(self, spot_one, spot_two, spot_three):
        self.spot1 = spot_one
        self.spot2 = spot_two
        self.spot3 = spot_three

recommendation = [
    Recommendation('bar','park','restaurant')
]


class Blog(models.Model):
    title = models.CharField(max_length=200)
    post = models.TextField(max_length=4000)
    img = models.CharField(max_length=1024, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    # city = models.ForeignKey(City, on_delete=CASCADE, related_name='cities')
    # profile = models.ManyToManyField(Profile)
    # recs = ManyToManyField(Recs)
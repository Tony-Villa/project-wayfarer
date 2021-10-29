from django.db import models 

City = {
    'name': 'Los Angeles'
}


class Blog(models.Model):
    title: models.CharField(max=200,min=1)
    post: models.TextField(max=4000)
    img: models.CharField(max=1024, default=City.img)

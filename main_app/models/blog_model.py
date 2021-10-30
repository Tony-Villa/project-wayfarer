from django.db import models
from .user_model import Profile
from .rec_model import Reccomendation
from .city_model import City
from .comment_model import Comment
from django.db.models.deletion import CASCADE

class Blog(models.Model):
    title = models.CharField(max_length=200, blank=False)
    post = models.TextField(max_length=4000, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    img = models.CharField(max_length=1024, default='')
    city = models.ForeignKey(City, on_delete=CASCADE, related_name='cities')
    comment = models.ForeignKey(Comment, on_delete=CASCADE, related_name='comments')
    profile = models.ManyToManyField(Profile)
    reccomendation = models.ManyToManyField(Reccomendation)

    def __str__(self):
        return self.title

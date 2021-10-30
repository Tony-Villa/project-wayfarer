from django.contrib import admin
from .models import Profile, Blog, Reccomendation, Comment, City 

# Register your models here.
admin.site.register(Profile)
admin.site.register(Blog)
admin.site.register(Reccomendation)
admin.site.register(Comment)
admin.site.register(City)
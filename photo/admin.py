from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Profile, Image, Comment, Likes,Follow,WelcomeEmailRecipients

admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Likes)
admin.site.register(Follow)
admin.site.register(WelcomeEmailRecipients)

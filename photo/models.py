from django.db import models
from cloudinary.models import CloudinaryField

class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=80)
    caption = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comments= models.ManyToManyField('Comment', blank=True)

class Profile(models.Model):
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length=500, blank=True)
class Comment(models.Model):
    comment = models.TextField(max_length=500)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ForeignKey('Image', on_delete=models.CASCADE)
       
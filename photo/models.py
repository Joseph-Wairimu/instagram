from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=80)
    caption = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self, new_caption):
        self.caption = new_caption
        self.save()
    


class Profile(models.Model):
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self, new_bio):
        self.bio = new_bio
        self.save()

        

class Comment(models.Model):
    comment = models.TextField(max_length=500)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ForeignKey('Image', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    


class Likes(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ForeignKey('Image', on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)       


class Follow(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    follower = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='following')   

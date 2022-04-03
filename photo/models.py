from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Image(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE,related_name='author')
    image = CloudinaryField('image', blank=True,null=True)
    name = models.CharField(max_length=80)
    caption = HTMLField()
    date_uploaded = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(User, default=None,blank= True,related_name='liked')
    dislikes = models.IntegerField(default=0)
  
    def __str__(self):
        return f'{self.author.username}'
    

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self, new_caption):
        self.caption = new_caption
        self.save()
    
    def __str__(self):
        return self.name

    @classmethod
    def search_by_name(cls, search_term):
        images = cls.objects.filter( author__username__icontains=search_term)
        return images
    @property
    def num_likes(self):
        return self.liked.all().count    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
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
    image = models.ForeignKey('Image',related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.image.caption,self.name}'

LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike'),
)


class Likes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,default='Like',max_length=10)

    def __str__(self):
        return str(self.image)     


class Follow(models.Model):
   
    follower = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='following')   

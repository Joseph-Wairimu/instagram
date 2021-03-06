from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Image, Profile, Comment, Likes, Follow

class RegisterForm(UserCreationForm):
    email= forms.EmailField()

    class Meta:
        model= User
        fields=["username","email","password1","password2"]

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['author', 'date_uploaded']
        widgets = {
            'likes': forms.CheckboxSelectMultiple(),
        }
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user','profile_pic','bio']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


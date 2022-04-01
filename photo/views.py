from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def welcome(request):
  
    return render(request, 'home.html')

def register(response):
    form= UserCreationForm()
    return render(response, 'register/register.html',{'form':form})    
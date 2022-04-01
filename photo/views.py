from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def welcome(request):
  
    return render(request, 'home.html')

def register(request):
  
    return render(request, 'register/register.html')    
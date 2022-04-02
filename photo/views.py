from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Image, Profile, Comment, Likes, Follow

# Create your views here.
def welcome(request):

    return render(request, 'home.html')


def home(request):
    images = Image.objects.all()
    return render(request, 'index.html',{'images': images[::-1], })

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

           
            
            return redirect('/welcome')
    else:
        form = RegisterForm()
    return render(response, 'register/register.html', {'form': form})

     
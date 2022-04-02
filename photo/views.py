from django.shortcuts import render, redirect
from .forms import RegisterForm, NewImageForm
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


def new_article(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = current_user
            article.save()
        return redirect('home')

    else:
        form = NewImageForm()
    return render(request, 'new_post.html', {"form": form})     
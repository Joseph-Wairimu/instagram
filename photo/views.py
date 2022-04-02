from django.shortcuts import render, redirect
from .forms import RegisterForm, NewImageForm,ProfileUpdateForm
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

def profile(request):
   user = request.user
   user = Profile.objects.get_or_create(user= request.user)
    
   if request.method == 'POST':
         form = ProfileUpdateForm(request.POST, request.FILES)
         if form.is_valid():
              profile = form.save(commit=False)
              profile.user = user
              profile.save()
         return redirect('profile')
   else:
            form = ProfileUpdateForm()
   return render(request, 'profile.html', {"form": form})

   
    

    
       
from django.shortcuts import render, redirect
from .forms import RegisterForm, NewImageForm,ProfileUpdateForm, CommentForm
from .models import Image, Profile, Comment, Likes, Follow,WelcomeEmailRecipients
from .email import send_welcome_email

# Create your views here.
def welcome(request):
    return render(request, 'home.html')


def home(request):
    images = Image.objects.all()
    return render(request, 'index.html',{'images': images[::-1], 'comments': comment})

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
           
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            recipient = WelcomeEmailRecipients(username =username,email =email)
            recipient.save()
            # send_welcome_email(username,email)  
            form.save()
           
            
            return redirect('login')
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
    current_user = request.user
    followers = Follow.objects.filter(follower=current_user)
    # profile = Profile.objects.get(user=current_user)
    images = Image.objects.filter(author=current_user)
    return render(request, 'profile.html', {"images": images, "profile": profile,"followers": followers})


def update_profile(request):

   user = request.user
   user = Profile.objects.get_or_create(user= request.user)
   bio = Profile.objects.get(user= request.user)
   profile_pic = Profile.objects.get(user= request.user)
   if request.method == 'POST':
         form = ProfileUpdateForm(request.POST, request.FILES)
         if form.is_valid():
              profile = form.save(commit=False)
              profile.user = user
              profile.save()
         return redirect('profile')
   else:
            form = ProfileUpdateForm()
   return render(request, 'new_profile.html', {"form": form, "user": user, "bio": bio, "profile_pic": profile_pic})

   
    

def search_results(request):

    if 'author' in request.GET and request.GET["author"]:
        search_term = request.GET.get("author")
        searched_articles = Image.search_by_name( search_term)
        message = f"{ search_term}"

        return render(request, 'search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


def comment(request,id):
    image = Image.objects.get(id=id)
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.image = image
            comment.save()
        return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'comment.html', {"form": form})  

def like_post(request):
    user = request.user
    if request.method == 'POST':
        news_item_id = request.POST.get('news_item_id')
        phone_post = Image.objects.get(id= news_item_id)

        if user in phone_post.liked.all():
            phone_post.liked.remove(user)
        else:
            phone_post.liked.add(user)

        like, created = Likes.objects.get_or_create(user=user, image_id = news_item_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()

    return redirect('home')


def followers(request,id):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    followers = Follow.objects.filter(user=current_user)
    return render(request, 'followers.html', {"followers": followers, "profile": profile})
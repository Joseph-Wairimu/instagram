from django.shortcuts import render

# Create your views here.
def welcome(request):
  
    return render(request, 'home.html')

def register(request):
  
    return render(request, 'register/register.html')    
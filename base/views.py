from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.


def landing(request):
    return render(request, 'base/landing.html')

def logout(request):
    logout(request)
    return redirect('home')

def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    return render(request, 'base/login.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'base/signup.html')


@login_required
def home(request):
    return render(request, 'base/home.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


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
    print(request.user)
    return render(request, 'base/home.html')
    
@login_required
def createClothe(request):
    return render(request, 'base/clothe_form.html')

@login_required
def history(request):
    return render(request, 'base/history.html')

@login_required
def configuration(request):
    return render(request, 'base/configuration.html')

@login_required
def profile(request):
    return render(request, 'base/profile.html')
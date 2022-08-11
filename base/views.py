from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def landing(request):
    return render(request, 'base/landing.html')


def login(request):
    return render(request, 'base/login.html')

def signup(request):
    return render(request, 'base/signup.html')


@login_required
def home(request):
    return render(request, 'base/home.html')

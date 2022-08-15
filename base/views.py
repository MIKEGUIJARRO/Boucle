from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q
from .models import Cloth
from .forms import ClothForm
from .choices import CATEGORY_CHOICES


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
    user = request.user
    clothes = Cloth.objects.filter(owner=user)
    # https://stackoverflow.com/questions/4320679/django-display-choice-value
    clothes_count = clothes.count()
    context = {'data': clothes, 'clothes_count': clothes_count}
    return render(request, 'base/home.html', context)


@login_required
def createClothe(request):
    categories = []
    for category in CATEGORY_CHOICES:
        categories.append({'number': category[0], 'value': category[1]})
    print(categories)
    if(request.method == 'POST'):
        # Create clothes
        Cloth.objects.create(
            owner=request.user,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            category=request.POST.get('category'),
        )
        return redirect('home')
    context = {'categories': categories}
    return render(request, 'base/clothe_form.html', context)


@login_required
def history(request):
    return render(request, 'base/history.html')


@login_required
def configuration(request):
    return render(request, 'base/configuration.html')


@login_required
def profile(request):
    return render(request, 'base/profile.html')

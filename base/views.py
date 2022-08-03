from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'message': 'hola mundo!'}
    return render(request, 'base/home.html', context)

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html')


def recipes(request):
    return HttpResponse('Recipes')


def blog(request):
    return HttpResponse('Blog')


def contact(request):
    return HttpResponse('Contact')

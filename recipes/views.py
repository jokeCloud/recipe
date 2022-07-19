from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html')


def recipes(request):
    return render(request, 'recipes/recipes.html')

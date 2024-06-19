from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "content/index.html")


def movies(request):
    return render(request, "content/movies.html")





from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<html><body><h1>!!! नमस्कार भारत !!!</h1></body></html>")
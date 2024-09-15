from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, request


def hello_world(request):
    return HttpResponse("<h1>Hello, world!</h1>")
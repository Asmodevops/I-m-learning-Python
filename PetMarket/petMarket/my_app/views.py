from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('<h2>My_App</h2>')

def page1(request):
    return HttpResponse('<h2>Page1</h2>')

def page2(request):
    return HttpResponse('<h2>Page2</h2>')


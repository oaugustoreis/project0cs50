from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"hello/index.html")
    return HttpResponse ("Hello!")
def augusto(request):
    return HttpResponse ("Hello, Augusto!")
def greet(request, name):
    return render(request)

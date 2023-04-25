from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def productList(request):
    return HttpResponse("<h1>Hello World</h1>")

def homePage1(request):
    return render(request,'layout.html')
def homePage(request):
    return render(request,'listing/home.html')
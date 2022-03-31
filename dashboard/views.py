from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

def dashboard(request):
    return render(request,"index.html")

def contact(request):
    return render(request,"contact.html")

def singlepage(request):
    return render(request,"single-page.html")


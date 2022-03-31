from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

def mainhome(request):
    return render(request,"mainhome.html")
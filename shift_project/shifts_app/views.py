from django.shortcuts import render
from django.http import HttpResponse

def shift(request):
   return render(request, 'shifts_app/shift.html')

 #Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def display(request)
  return HttpResponse()
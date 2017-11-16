from django.shortcuts import render

def shift(request):
    return render(request, 'shifts_app/shift.html')

# Create your views here.
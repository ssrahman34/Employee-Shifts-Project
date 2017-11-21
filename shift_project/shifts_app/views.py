from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from shifts_app import Shift

def shift(request):
   return render(request, 'shifts_app/shift.html')

 #Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def display(request):
    template = loader.get_template('shifts_app/detail.html')

    shiftObjects = Shift.objects.all()
    index = 0
    ListID = [] #initialize an empty list
    ListStart=[]
    ListEnd=[]
    string = ""
    result = ""
    endResult = []

    for s in shiftObjects:
        index = index+1
        string= "Shift"+" "+str(index)+"<br>"
        sid = str(s.id)
        #ListID += s.id
        start = s.start_datetime.strftime("%B %d, %Y")
        end = s.end_datetime.strftime("%B %d, %Y")
        final = string+" "+"ID:"+sid + " " + "Start:"+start+" "+"End:"+end+ "\r\n" + "<br>"+"<br>"
        result+=final
        endResult += final
    return HttpResponse(result)

def shifts_display(request):
    template = loader.get_template('shifts_app/shifts_display.html')
    index = 0
    shiftObjects = Shift.objects.all()
    result = ""
    context = {
        'shiftObjects': shiftObjects,
    }
    for s in Shift.objects.all():
        index = index+1
        string= "Shift"+" "+str(index)+"<br>"
        result +=string
    return render(request, 'shifts_app/shifts_display.html',context)
    #call display first and then create a URL using that and put that url into the urls.py

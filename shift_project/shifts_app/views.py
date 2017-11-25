from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from shifts_app import Shift
from shifts_app import Run
#from shifts_app.shift_group import ShiftGroup
from django.utils import timezone
import datetime

def shift(request):
   return render(request, 'shifts_app/shift.html')

 #Create your views here.

def index(request):
    return HttpResponse("Hello. You're at the shift index.")

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
        temp = ""

        start = s.start_datetime.strftime("%B %d, %Y")
        end = s.end_datetime.strftime("%B %d, %Y")
        #issue!! Cannot iterate through runs_related list. cannot access individual run using it!
        final = string+" "+"ID:"+sid + " " + "Start:"+start+" "+"End:"+end + " " +"<br>" +"Runs: ["+str(s.runs_related)+"]" + "<br>" + "<br>"
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
        string= "Shift"+" "+str(index)+"runlist: "+"<br>"
        result +=string      
    return render(request, 'shifts_app/shifts_display.html',context)
    #call display first and then create a URL using that and put that url into the urls.py

def group(request):
    template = loader.get_template('shifts_app/group.html')
    index = 1
    Jan= []
    Feb= []
    Mar= []
    Apr= []
    May= []
    Jun= []
    Jul= []
    Aug= []
    Sep= []
    Oct= []
    Nov= []
    Dec= []
    while (index < 31):
        Jan += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 1, index))
        Mar += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 3, index))
        Apr += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 4, index))
        May += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 5, index))
        Jun += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 6, index))
        Jul += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 7, index))
        Aug += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 8, index))
        Sep += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 9, index))
        Oct += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 10, index))
        Nov += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 11, index))
        Dec += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 12, index))
        index+=1
    index = 1
    while (index < 29):
        Feb += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 2, index))
        index+=1


    context = {
        'Jan': Jan,
        'Feb': Feb,
        'Mar': Mar,
        'Apr': Apr,
        'May': May,
        'Jun': Jun,
        'Jul': Jul,
        'Aug': Aug,
        'Sep': Sep,
        'Oct': Oct,
        'Nov': Nov,
        'Dec': Dec,
    }
    """    template = loader.get_template('shifts_app/group.html')
    shiftGroup = ShiftGroup()
    shiftGroup.calculate()


    context = {
        'Jan': shiftGroup.Jan,
        'Feb': shiftGroup.Feb,
        'Mar': shiftGroup.Mar,
        'Apr': shiftGroup.Apr,
        'May': shiftGroup.May,
        'Jun': shiftGroup.Jun,
        'Jul': shiftGroup.Jul,
        'Aug': shiftGroup.Aug,
        'Sep': shiftGroup.Sep,
        'Oct': shiftGroup.Oct,
        'Nov': shiftGroup.Nov,
        'Dec': shiftGroup.Dec,
    }
"""

    return render(request, 'shifts_app/group.html',context)


def week(request):
    #template = loader.get_template('shifts_app/group.html')

    firstHalf = []
    secHalf = []
    weekend = []
    test1 = []
    test2 = []
    weekend += Shift.objects.filter(start_datetime__week_day=0) #saturday
    weekend += Shift.objects.filter(start_datetime__week_day=1) #sunday

    firstHalf += Shift.objects.filter(start_datetime__week_day=2) #All Monday
    firstHalf += Shift.objects.filter(start_datetime__week_day=3) #All Tuesday
    firstHalf += Shift.objects.filter(start_datetime__week_day=4)#,timestamp__hour__lt=12) #Wednesday until 12:00
    #test1 = Shift.objects.filter(start_datetime__week_day=4).filter(start_datetime__hour = 11)
    wed = Shift.objects.filter(start_datetime__week_day=4)
    for each in wed:
        start = each.start_datetime.strftime("%-H")
        if start < 12:
            test1.append(each)
        else:
            test2.append(each) # if it is past 12
            
    #secondHalf += Shift.objects.filter(start_datetime__week_day=4,timestamp__hour__gte=12) #Wed after 12


    secHalf +=  Shift.objects.filter(start_datetime__week_day=5) #All Thursday   
    secHalf += Shift.objects.filter(start_datetime__week_day=5) #All Thursday
    secHalf += Shift.objects.filter(start_datetime__week_day=6) #All Friday

    context = {
        'firstHalf': firstHalf,
        'secHalf' : secHalf,
        'weekend' : weekend,
        'test1' : test1,
        'test2' :test2
 
    }
    return render(request, 'shifts_app/week.html',context)

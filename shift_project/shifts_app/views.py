from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from shifts_app import Shift
from shifts_app import Run
from.forms import RunForm
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
    """template = loader.get_template('shifts_app/group.html')
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
    }"""
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

class IndexView(generic.ListView):
    template_name = 'shifts_app/index.html'

    def get_queryset(self):
        return Shift.objects.all()

class DetailView(generic.DetailView):
    model = Shift
    template_name = 'shifts_app/detail.html'


class ShiftCreate(CreateView):
    model = Shift 
    #what attributes do you  want user to specify?
    fields = ['start_datetime', 'end_datetime'] #only 2

#class RunCreate(CreateView):
 #   model = Run
    #what attributes do you  want user to specify?
  #  fields = ['user_id','start_datetime', 'end_datetime'] #only 2
    
   # success_url = reverse_lazy('shift:index')
def create_run(request, shift_id):
    form = RunForm(request.POST or None, request.FILES or None)
    shift = get_object_or_404(Shift, pk=shift_id)
    if form.is_valid():
        shift_runs = shift.runs_related.all()
        for s in shift_runs:
            if s.user_id == form.cleaned_data.get("user_id"):
                context = {
                    'user_id': user_id,
                    'form': form,
                    'error_message': 'You already added that song',
                }
                return render(request, 'shifts_app/run_form.html', context)
        run = form.save(commit=False)
        run.shift = shift
        run.save()
        return render(request, 'shifts_app/detail.html', {'shift': shift})
    context = {
        'shift': shift,
        'form': form,
    }
    return render(request, 'shifts_app/run_form.html', context)

class ShiftUpdate(UpdateView):
    model = Shift 
    #what attributes do you  want user to specify?
    fields = ['start_datetime', 'end_datetime'] #only 2

class ShiftDelete(DeleteView):
    model = Shift
    #when you successfuly delete a shift
    success_url = reverse_lazy('shift:index')

def covered(request,shift_id):
    shift = get_object_or_404(Shift, pk=shift_id)
    print("entered coverage funciton")
    #selected_run = get_object_or_404(Run, pk=run_id)
    #selected_run.is_covered = False
    #selected_run.save()
    #return render(request, 'shifts_app/detail.html')
    #success_url = reverse_lazy('shift:index')
    #return success_url
    #make sure this is a valid run id
    try:
        selected_run = shift.runs_related.all().get(pk=request.POST['run'])
    except(KeyError, Run.DoesNotExist):
        return render(request, 'shifts_app/detail.html',{
            'shift': shift,
            'error_message': "You did not select a valid run",
        }) 
    else:
        selected_run.is_covered = True
        selected_run.save()
        return render(request, 'shifts_app/detail.html', {'shift': shift})
def user(request):
    ids = []
    made_it = ""
    form = RunForm(request.POST or None, request.FILES or None)
    #if form.is_valid():

    for shift in Shift.objects.all():
        shift_runs = shift.runs_related.all()
        for s in shift_runs:
            if s.user_id in ids:
                continue
            else :
                ids.append(s.user_id)
    context= {
        'ids':ids,
        'made_it':made_it,
        'form': form,
        }
    return render(request, 'shifts_app/users.html', context)

class DetailView(generic.DetailView):
    model = Run
    template_name = 'shifts_app/run_detail.html'
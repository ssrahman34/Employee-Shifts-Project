from django.shortcuts import render,get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from shifts_app import Shift
from shifts_app import Run
from shifts_app.his import His


from.forms import RunForm
from shifts_app.shift_group import ShiftGroup, ShiftGroupManager
from django.utils import timezone
import datetime

def shift(request):
   return render(request, 'shifts_app/shift.html')

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
    sgm = ShiftGroupManager()
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
    Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec = sgm.getMonths(Shift.objects.all())
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

def create_run(request, shift_id):
    form = RunForm(request.POST or None, request.FILES or None)
    shift = get_object_or_404(Shift, pk=shift_id)
    if form.is_valid():
        shift_runs = shift.runs_related.all()
        for s in shift_runs:
            continue
        run = form.save(commit=False)
        if run.start_datetime.date() < shift.start_datetime.date() or run.end_datetime.date() > shift.end_datetime.date():
            message = "<html><link rel='stylesheet' href='//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css'><span class = 'text-danger large'><h2 class='text-center'>You cannot create a Run outside the Shift start and end bounds</h2><span></html>"
            return HttpResponse(message)
        if run.start_datetime.time() < shift.start_datetime.time() or run.end_datetime.time() > shift.end_datetime.time():
            message = "<html><link rel='stylesheet' href='//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css'><span class = 'text-danger large'><h2 class='text-center'>You cannot create a Run outside the Shift start and end bounds</h2><span></html>"
            return HttpResponse(message)
        run.shift = shift
        run.save()
        return render(request, 'shifts_app/detail.html', {'shift': shift})
    context = {
        'shift': shift,
        'form': form,
    }
    return render(request, 'shifts_app/run_form.html', context)

def edit_run(request, shift_id, run_id):
    instance = get_object_or_404(Run, id = run_id)
    print("old user Id " + str(instance.user_id))
    oldId = instance.user_id
    form = RunForm(request.POST or None, instance=instance)
    
    shift = get_object_or_404(Shift, pk=shift_id)
    if form.is_valid():
        shift_runs = shift.runs_related.all()
        for s in shift_runs:
            if s.id == form.cleaned_data.get("run.id"):
                print("new ud" + str(user_id))
                context = {
                    'user_id': user_id,
                    'form': form,
                    'shift' : shift,
                    'error_message': 'You already added that Run',
                }
                return render(request, 'shifts_app/run_update.html', context)
        run = form.save(commit=False)
        if run.start_datetime.date() < shift.start_datetime.date() or run.end_datetime.date() > shift.end_datetime.date():
            message = "<html><link rel='stylesheet' href='//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css'><span class = 'text-danger large'><h2 class='text-center'>You cannot create a Run outside the Shift start and end bounds</h2><span></html>"
            return HttpResponse(message)
        if run.start_datetime.time() < shift.start_datetime.time() or run.end_datetime.time() > shift.end_datetime.time():
            message = "<html><link rel='stylesheet' href='//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css'><span class = 'text-danger large'><h2 class='text-center'>You cannot create a Run outside the Shift start and end bounds</h2><span></html>"
            return HttpResponse(message)
        if run.user_id != oldId:
            print(run.history)
            if run.history is None:
                 h2 = His(user_ids = oldId) #delcare a new His with the first element
                 h2.save()
                 run.history = h2
            else:
                h2 = His(user_ids = str(run.history.user_ids) + "," + str(oldId)) #create a new History
                h2.save()
                run.history = h2
        #print(run.history.user_ids)
        run.shift = shift
        run.save()
        return render(request, 'shifts_app/detail.html', {'shift': shift})
    context = {
        'shift': shift,
        'form': form,
    }
    return render(request, 'shifts_app/run_update.html', context)

def history_runs(request):
    result = "<html><link rel='stylesheet' href='//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css'><h4>USER ID HISTORY PAGE<h4></html>"
    result += "<br>"
    result += "<html><h4>Right most number is the most recent User<h4></html>"
    result += "<br></br>"
    #ids = []
    template_name = 'shifts_app/history_runs.html'
    for shift in Shift.objects.all():
        shift_runs = shift.runs_related.all() #get all shifts
        for run in shift_runs:
            if run.history is not None:
                #ids += run.id
                result += "Shift ID: "+ str(shift.id)
                result += "Run ID: "+ str(run.id)
                result += " User History: " + run.history.user_ids
                result += "<br>"
    context= {
        'result':result,
       #'ids':ids
        }
    #return render(request, 'shifts_app/history_runs.html', context)
    return HttpResponse(result)
    


def run_update(request, shift_id,run_id):
    print("inpudate")
    instance = get_object_or_404(Run, id = run_id)
    form = RunForm(request.POST or None, instance=instance)
    shift = get_object_or_404(Shift, pk=shift_id)
    if form.is_valid():
        shift_runs = shift.runs_related.all()
        for s in shift_runs:
            if s.id == form.cleaned_data.get("run.id"):
                context = {
                    'user_id': user_id,
                    'form': form,
                    'shift' : shift,
                    'error_message': 'You already added that Run',
                }
                return render(request, 'shifts_app/run_updateID.html', context)
        run = form.save(commit=False)
        run.shift = shift
        run.save()
        return render(request, 'shifts_app/detail.html', {'shift': shift})
    context = {
        'shift': shift,
        'form': form,
    }
    return render(request, 'shifts_app/run_updateID.html', context)

def run_delete(request,shift_id, run_id):
    instance = get_object_or_404(Run, id = run_id)
    instance.delete()
    messages.success(request, "Successfully Deleted Run")
    return redirect('shift:index')
    #return redirect('shift:detail',id=shift_id)

class ShiftUpdate(UpdateView):
    model = Shift 
    #what attributes do you  want user to specify?
    fields = ['start_datetime', 'end_datetime'] #only 2
    template_name_suffix = '_update_form'


class ShiftDelete(DeleteView):
    model = Shift
    #when you successfuly delete a shift
    success_url = reverse_lazy('shift:index')

def covered(request,run_id, usr_id):
    #we want to relapce run.user_id with usr_id
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

def Userview(request, usr_id):
    template_name = 'shifts_app/run_detail.html'
    result = ""
    check = usr_id
    for shift in Shift.objects.all():
        shift_runs = shift.runs_related.all() #get all shifts
        for run in shift_runs:
            check = "runs user ID" +str(run.user_id)
            check2 = "INPUT ID" + str(usr_id)
            if str(run.user_id) == usr_id:
                check = "YES checkied"
                result += "For User #" + usr_id + " | Shift Id: "+ str(shift.id)+ " | Run Id:" + str(run.id)+ "   |   Run's Start Date : " + str(run.start_datetime.date()) + " | Run's Start Time : " + str(run.start_datetime.time()) + "   |   Run's End Date : " + str(run.end_datetime.date()) + " | Run's End Time : " + str(run.end_datetime.time())
    context= {
        'result':result,
        'check':check,
        'check2':check2,
    }
    return render(request, 'shifts_app/run_detail.html', context)


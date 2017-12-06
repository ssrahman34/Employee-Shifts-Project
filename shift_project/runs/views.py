from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from shifts_app import Shift
from shifts_app import Run
from shifts_app.forms import RunForm
#from shifts_app.shift_group import ShiftGroup
from django.utils import timezone
import datetime

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
        
    return render(request, 'users.html', context)

class DetailView(generic.DetailView):
    model = Run
    template_name = 'run_detail.html'
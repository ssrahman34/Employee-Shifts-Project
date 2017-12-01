from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.timezone import utc, make_aware, get_default_timezone
import datetime
#from shifts_app.shift import Shift
#from shifts_app import Run
#from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader


class ShiftGroup(models.Model):
   #self.shifts_realted accesses the specific shift
    def __str__(self):
        return self.name
    """ def getMonths(self):
        for shift in self.shifts_related.all():
            if (self.start_datetime.month() == "January"):
                January += shift """
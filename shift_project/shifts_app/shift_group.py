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


class ShiftGroupManager(models.Manager):
   #self.shifts_realted accesses the specific shift
    def __str__(self):
        return self.name
    def getMonths(self, list1):
        print(list1)
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
            Jan += list1.filter(start_datetime__contains=datetime.date(2017, 1, index))
            Mar += list1.filter(start_datetime__contains=datetime.date(2017, 3, index))
            Apr += list1.filter(start_datetime__contains=datetime.date(2017, 4, index))
            May += list1.filter(start_datetime__contains=datetime.date(2017, 5, index))
            Jun += list1.filter(start_datetime__contains=datetime.date(2017, 6, index))
            Jul += list1.filter(start_datetime__contains=datetime.date(2017, 7, index))
            Aug += list1.filter(start_datetime__contains=datetime.date(2017, 8, index))
            Sep += list1.filter(start_datetime__contains=datetime.date(2017, 9, index))
            Oct += list1.filter(start_datetime__contains=datetime.date(2017, 10, index))
            Nov += list1.filter(start_datetime__contains=datetime.date(2017, 11, index))
            Dec += list1.filter(start_datetime__contains=datetime.date(2017, 12, index))
            index+=1
        index = 1
        while (index < 29):
            Feb += list1.filter(start_datetime__contains=datetime.date(2017, 2, index))
            index+=1
        return (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec)

class ShiftGroup(models.Model):
    db_table="shiftGroup"
    objects = ShiftGroupManager()
    def __str__(self):
        return self

    class Meta:
        app_label = "shifts_app"
      

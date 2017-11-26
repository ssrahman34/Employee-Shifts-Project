from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.timezone import utc, make_aware, get_default_timezone
import datetime
from shifts_app.shift import Shift
#from shifts_app import Run
#from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader


class ShiftGroup(models.Model):

    Jan= models.ManyToManyField("Shift", null = True, blank= True, related_name="shiftsJanRelated") 
    Feb= models.ManyToManyField("Shift", null = True, blank= True, related_name="shiftsFebRelated") 
    Mar= models.ManyToManyField("Shift", null = True, blank= True, related_name="shiftsMarRelated") 
    Apr= models.ManyToManyField("Shift", null = True, blank= True, related_name="shiftsAprRelated") 
    May= models.ManyToManyField("Shift", null = True, blank= True, related_name="shiftsMayRelated") 
    Jun= models.ManyToManyField("Shift", null = True, blank= True, related_name="shiftsJunRelated") 
    Jul= models.ManyToManyField("Shift", null = True, blank= True, related_name="shiftsJulRelated") 
    Aug= models.ManyToManyField("Shift", null = True, blank= True, related_name="shiftsAugRelated") 
    Sep= models.ManyToManyField("Shift", null = True, blank= True, related_name="shiftsSepRelated") 
    Oct= models.ManyToManyField("Shift", null = True, blank= True, related_name="shiftsOctRelated") 
    Nov= models.ManyToManyField("Shift", null = True, blank= True, related_name="shiftsNovRelated") 
    Dec= models.ManyToManyField("Shift", null = True, blank= True, related_name="shiftsDecRelated") 


    @classmethod
    def assign(Jan1, Feb1, Mar1, Apr1, May1, Jun1,Jul1,Aug1 ,Sep1 ,Oct1,Nov1,Dec1):
        Jan = Jan1
        Feb = Feb1
        Mar = Mar1
        Apr = Apr1
        May = May1
        Jun = Jun1
        Jul= Jul1
        Aug = Aug1
        Sep = Sep1
        Oct = Oct1
        Nov = Nov1
        Dec = Dec1
        #return self #incse
    def calculate(cls):
        index = 1
        Jan1= []
        Feb1= []
        Mar1= []
        Apr1= []
        May1= []
        Jun1= []
        Jul1= []
        Aug1= []
        Sep1= []
        Oct1= []
        Nov1= []
        Dec1= []
        while (index < 31):
            Jan1 += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 1, index))
            Mar1 += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 3, index))
            Apr1 += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 4, index))
            May1 += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 5, index))
            Jun1 += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 6, index))
            Jul1 += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 7, index))
            Aug1 += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 8, index))
            Sep1 += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 9, index))
            Oct1 += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 10, index))
            Nov1 += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 11, index))
            Dec1 += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 12, index))
            index+=1
        index = 1
        while (index < 29):
            Feb1 += Shift.objects.filter(start_datetime__contains=datetime.date(2017, 2, index))
            index+=1
        ShiftGroup.assign(Jan1, Feb1, Mar1, Apr1, May1, Jun1, Jul1, Aug1, Sep1, Oct1, Dec1)
from django.db import models
from django import forms
from django.db.models import Q
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.utils.timezone import utc, make_aware, get_default_timezone
import datetime
from shifts_app.run import Run
#from shifts_app.shift_group import ShiftGroup
#https://docs.djangoproject.com/en/1.11/topics/db/queries/


class ShiftManager(models.Manager):

    def create_shift(self, start_datetime, end_datetime, run_times_list):

    #run_times_list have data for each run -> a list of lists            
        shift = Shift(start_datetime= start_datetime, end_datetime= end_datetime) #assign to given parameters
        shift.save()
        for eachList in run_times_list:
            i = 0
            s = 0
            e = 0
            for elem in eachList:
                if(i == 0):
                    user_id=elem
                    i = 1
                    continue
                if (s == 0):
                    start_datetime=elem
                    s = 1
                    continue
                if (e == 0):
                    end_datetime = elem
                    e = 1
                r = Run.create(user_id, start_datetime, end_datetime, shift)
                r.save() #saveRun
                print(user_id, start_datetime, end_datetime)

    def get_shifts_in_datetime_range(self, start_datetime, end_datetime):
        if (self.start_datetime >= start_datetime and self.end_datetime <= end_datetime):
            return self
          


class Shift(models.Model):

    db_table="shift"
    objects = ShiftManager()

    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    

    def get_absolute_url(self):
        return reverse('shift:detail',kwargs = {'pk': self.pk})#When we create a new Shift it will add to database and give it some PK and take it to the view with whatever #the pK is
    def __str__(self):
        return str(self.id) +'-'+ str(self.start_datetime) + '-' +str(self.end_datetime)

    class Meta:
        app_label = "shifts_app"

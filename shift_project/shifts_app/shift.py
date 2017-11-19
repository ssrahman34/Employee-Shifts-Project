from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.timezone import utc, make_aware, get_default_timezone
import datetime

#from shifts_app.shift_group import ShiftGroup

class ShiftManager(models.Manager):

    def create_shift(self, start_datetime, end_datetime, run_times_list):
        #run_times_list = Run.ForeignKey(self, null = True, blank= True,related_name="runs_related")
        #shift=self.create(start_datetime = start_datetime, end_datetime = end_datetime)
        shifta = Shift(start_datetime= start_datetime, end_datetime= end_datetime) #assign to given parameters
        shifta.save()
        #return shift

    def get_shifts_in_datetime_range(self, start_datetime, end_datetime):
        if (self.start_datetime >= start_datetime and self.end_datetime <= end_datetime):
            return self
          

class Shift(models.Model):

    db_table="shift"
    objects = ShiftManager()

    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    def __str__(self):
        return self

    class Meta:
        app_label = "shifts_app"

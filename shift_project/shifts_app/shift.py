from django.db import models
from django.db.models import Q
from django.utils.timezone import utc, make_aware, get_default_timezone
import datetime

#from shifts_app.shift_group import ShiftGroup

class ShiftManager(models.Manager):

    def create_shift(self, start_datetime, end_datetime, run_times_list):
        #run_times_list -> [{start_time=time, end_time=time},{...},{...}]
        pass


    def get_shifts_in_datetime_range(self, start_datetime, end_datetime):
        #if (self.start_datetime >= start_datetime && self.end_datetime <= end_datetime):
          #return self
          pass

class Shift(models.Model):

    #runs_related

    db_table="shift"
    objects = ShiftManager()

    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    def __str__(self):
        return self

    class Meta:
        app_label = "shifts_app"

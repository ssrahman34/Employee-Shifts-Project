from django.db import models
from django.core.urlresolvers import reverse

#from shifts_app.shift import Shift
"""class RunManager(models.Manager):
  def create_run(self, user_id, start_datetime, end_datetime, shift): #pass in shift
        run = Run(user_id = user_id, start_datetime= start_datetime, end_datetime= end_datetime, shift = shift) #assign to given parameters
        
        run.save()"""


class Run(models.Model):

    db_table="run"

    shift = models.ForeignKey("Shift", null = True, blank= True, related_name="runs_related") 
    #tells django each run is realted to a single shift
    user_id = models.IntegerField(default=0, blank=True)

    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    @classmethod
    def create(cls, user_id, start_datetime, end_datetime, shift):
        run = cls(user_id=user_id, start_datetime=start_datetime, end_datetime=end_datetime, shift=shift)
        run.save()
        return run

    class Meta:
        app_label = "shifts_app"
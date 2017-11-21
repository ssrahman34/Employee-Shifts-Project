from django.db import models

#from shifts_app.shift import Shift


class Run(models.Model):

    db_table="run"

    #shift = models.ForeignKey(Shift, null = True, blank= True, related_name="runs_related") 
    #tells django each run is realted to a single shift
    user_id = models.IntegerField(default=0, blank=True)

    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    def create(cls,user_id, start_datetime, end_datetime):
        run = cls(user_id=user_id, start_datetime=start_datetime, end_datetime=end_datetime)
        run.save()
        return run

    class Meta:
        app_label = "shifts_app"
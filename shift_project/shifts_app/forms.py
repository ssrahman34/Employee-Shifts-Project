from django import forms
from shifts_app.run import Run

class RunForm(forms.ModelForm):
    class Meta:
        model = Run
        fields = ['user_id', 'start_datetime', 'end_datetime']
        #default_validators = [validators.validate_run],
        
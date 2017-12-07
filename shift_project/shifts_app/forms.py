from django import forms
from shifts_app.run import Run

class RunForm(forms.ModelForm):
    class Meta:
        model = Run
        fields = ['user_id', 'start_datetime', 'end_datetime']
        #default_validators = [validators.validate_run],
    def clean(self):
        cleaned_data = super(RunForm, self).clean()
        start_time = cleaned_data['start_datetime']
        end_time = cleaned_data['end_datetime']
        if start_time and end_time:
            if end_time.time() < start_time.time():
                raise forms.ValidationError("*Note: End time cannot be earlier than start time! Please try again.")
        return cleaned_data
        
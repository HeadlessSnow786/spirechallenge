from django import forms

from .models import StartPoint

class StartPointCreate(forms.ModelForm):
    class Meta:
        model = StartPoint
        fields = [
            'time', 
            'startlat', 
            'startlong', 
            'endlat', 
            'endlong'
        ]
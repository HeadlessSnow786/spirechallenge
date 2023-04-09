from django import forms
from .models import Coordinates

class CoordForm(forms.ModelForm):
    class Meta:
        model = Coordinates
        fields = [
            'start_latitude',
            'start_longitude',
            'end_latitude',
            'end_longitude',
            'time'
            ]

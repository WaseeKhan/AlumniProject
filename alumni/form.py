from django import forms
from .models import *


class AddAlumniForm(forms.ModelForm):
    class Meta:
        model = AddAlumni
        batch = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)
        fields = ['name', 'batch', 'phone', 'email', 'profession', 'location', 'icoInsta', 'dp']

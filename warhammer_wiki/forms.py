from django import forms
from .models import Factions

class CreateNewFaction(forms.ModelForm):    
    class Meta:
        model = Factions
        fields = ['name', 'description']
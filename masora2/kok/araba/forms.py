from django import forms
from .models import Car

class Arabaform(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('Model', 'Ulke', 'Fiyat', 'Km', 'Tarih')
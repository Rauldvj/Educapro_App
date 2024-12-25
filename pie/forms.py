from django import forms
from .models import RegistroPie

class ListPieForm(forms.ModelForm):
    class Meta:
        model = RegistroPie
        fields = ['estudiante', 'apoderado_titular']

class AddRegistroPieForm(forms.ModelForm):
    class Meta:
        model = RegistroPie
        fields = ['estudiante', 'apoderado_titular']



from django import forms
from .models import ArchivoTecnico

class ArchivoTecnicoForm(forms.ModelForm):
    class Meta:
        model = ArchivoTecnico
        fields = ['titulo', 'descripcion', 'archivo']

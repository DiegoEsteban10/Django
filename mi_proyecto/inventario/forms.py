from django import forms
from .models import Curso
from django.core.exceptions import ValidationError
from datetime import date

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

    def clean_cupos(self):
        cupos = self.cleaned_data['cupos']
        if cupos <= 0:
            raise ValidationError("Los cupos deben ser mayores a cero.")
        return cupos

    def clean_fecha_inicio(self):
        fecha = self.cleaned_data['fecha_inicio']
        if fecha < date.today():
            raise ValidationError("La fecha de inicio no puede ser anterior a hoy.")
        return fecha

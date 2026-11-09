from django import forms 
from .models import Empleados

class Registrar_empleado_form(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = ('title','text')
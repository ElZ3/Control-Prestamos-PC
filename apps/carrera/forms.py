from django import forms
from .models import Carrera

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['codigo', 'nombre', 'descripcion', 'estado']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: MAT123'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la carrera'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }
        # Personalizamos el mensaje cuando el campo se deja vacío
        error_messages = {
            'codigo': {'required': 'El campo codigo es requerido.'},
            'nombre': {'required': 'El campo nombre es requerido.'},
            'descripcion': {'required': 'El campo descripción es requerido.'},
        }
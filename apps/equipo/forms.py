from datetime import date
from django import forms
from .models import Equipo

class EquipoForm(forms.ModelForm):

    class Meta:
        model = Equipo

        fields = [
            'codigo',
            'marca',
            'modelo',
            'estado',
            'fecha_mantenimiento',
            'observaciones'
        ]

        widgets = {

            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: PCA100'
            }),

            'marca': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'modelo': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'estado': forms.Select(attrs={
                'class': 'form-select'
            }),

            'fecha_mantenimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'min': date.today().isoformat()
            }),

            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2
            }),
        }

        # Mensajes de error personalizados para campos vacíos (requeridos por defecto)
        error_messages = {
            'codigo': {'required': 'El campo Código es obligatorio.'},
            'marca': {'required': 'El campo Marca es obligatorio.'},
            'modelo': {'required': 'El campo Modelo es obligatorio.'},
            'estado': {'required': 'El campo Estado es obligatorio.'},
            'fecha_mantenimiento': {'required': 'La fecha de mantenimiento es obligatoria.'},
        }
        
    def clean_fecha_mantenimiento(self):

        fecha = self.cleaned_data.get('fecha_mantenimiento')

        if fecha and fecha < date.today():

            raise forms.ValidationError(
                'No se permiten fechas anteriores a hoy.'
            )

        return fecha

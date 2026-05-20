"""
====================================================================
SISTEMA DE GESTIÓN DE PRÉSTAMO DE LAPTOPS (RESO-LAP)
====================================================================
Descripción: Aplicación backend en Django para el control, asignación y devolución de laptops.
Organización: ESTUDIO DAFARO
Contacto:     EstudioDafaro@techedu.sv | +503 2301-0000
Año de Creación: 2026
País: El Salvador

Licencia: Creative Commons Atribución-NoComercial-SinDerivadas 4.0 Internacional
          (CC BY-NC-ND 4.0)
© 2026 Estudio Dafaro. Algunos derechos reservados.

Usted es libre de: Compartir y utilizar este software bajo las siguientes condiciones:
  - Atribución: Debe dar crédito a Estudio Dafaro.
  - No Comercial: No puede utilizar este material con fines comerciales.
  - Sin Derivadas: Si remezcla, transforma o crea a partir del material,
    no puede distribuir el material modificado.

Para ver una copia de esta licencia, visita: http://creativecommons.org/licenses/by-nc-nd/4.0/
====================================================================
"""

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

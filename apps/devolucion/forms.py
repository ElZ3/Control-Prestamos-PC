"""
====================================================================
SISTEMA DE GESTIÓN DE PRÉSTAMO DE LAPTOPS (RESO-LAP)
====================================================================
Descripción: Aplicación backend en Django para el control, 
             asignación y devolución de laptops.
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
from django import forms
from apps.prestamo.models import Prestamo

class DevolucionForm(forms.ModelForm):

    class Meta:
        model = Prestamo
        fields = [
            'condicion_devolucion',
            'presenta_danos',
            'observacion_devolucion'
        ]
        widgets = {
            'observacion_devolucion': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_observacion_devolucion(self):
        obs = self.cleaned_data.get('observacion_devolucion')
        if not obs:
            raise forms.ValidationError("La observación es obligatoria.")
        return obs
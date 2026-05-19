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
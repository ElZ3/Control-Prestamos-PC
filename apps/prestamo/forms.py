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

from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError

from .models import Prestamo
from apps.usuario.models import Usuario
from apps.equipo.models import Equipo


class PrestamoForm(forms.ModelForm):

    class Meta:
        model = Prestamo

        # ❌ QUITAMOS estado del formulario
        fields = [
            'usuario',
            'equipo',
            'fecha_limite',
            'condicion_entrega',
            'observacion_entrega'
        ]

        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-select'}),
            'equipo': forms.Select(attrs={'class': 'form-select'}),

            'fecha_limite': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'min': timezone.now().date().isoformat()
                }
            ),

            'condicion_entrega': forms.Select(attrs={'class': 'form-select'}),

            'observacion_entrega': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': 'Observaciones al momento de entrega...'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 👤 SOLO USUARIOS ACTIVOS (estudiantes + docentes)
        usuarios_base = Usuario.objects.filter(
            estado='ACTIVO',
            rol__in=[
                Usuario.Roles.ESTUDIANTE,
                Usuario.Roles.DOCENTE
            ]
        )

        # 🚫 EXCLUIR usuarios con préstamo ACTIVO
        usuarios_ocupados = Prestamo.objects.filter(
            estado='ACTIVO'
        ).values_list('usuario_id', flat=True)

        self.fields['usuario'].queryset = usuarios_base.exclude(
            id__in=usuarios_ocupados
        )

        # 💻 SOLO EQUIPOS DISPONIBLES
        self.fields['equipo'].queryset = Equipo.objects.filter(
            estado='ACTIVO'
        )

    def clean_fecha_limite(self):
        fecha = self.cleaned_data.get('fecha_limite')
        hoy = timezone.now().date()

        if fecha < hoy:
            raise ValidationError("La fecha límite no puede ser anterior a hoy.")

        return fecha
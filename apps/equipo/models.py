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

from django.db import models
from django.core.validators import RegexValidator
from datetime import date

class Equipo(models.Model):
    ESTADOS_CHOICES = [
        ('DISPONIBLE', 'Disponible'),
        ('EN_USO', 'En uso'),
        ('MANTENIMIENTO', 'En mantenimiento'),
        ('INACTIVO', 'Inactivo'),
    ]

    creado_por = models.ForeignKey(
        'usuario.Usuario',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='equipos_creados'
    )

    codigo = models.CharField(
        max_length=20,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[A-Z]+\d+$',
                message='El código debe tener el formato tipo PCA100 (letras seguidas de números).'
            )
        ]
    )
    marca = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9\s]+$',
                message='Solo se permiten letras y números.'
            )
        ]
    )
    modelo = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9\s]+$',
                message='Solo se permiten letras y números.'
            )
        ]
    )
    fecha_mantenimiento = models.DateField(verbose_name='Fecha de Inicio Mantenimiento')
    
    estado = models.CharField(
        max_length=20, 
        choices=ESTADOS_CHOICES, 
        default='DISPONIBLE'
    )
    observaciones = models.TextField(blank=True, null=True)

    @property
    def mantenimiento_vencido(self):

        if not self.fecha_mantenimiento:
            return False

        dias = (date.today() - self.fecha_mantenimiento).days

        return dias >= 30


    @property
    def necesita_mantenimiento_hoy(self):

        return (
            self.fecha_mantenimiento == date.today()
            and self.estado != 'MANTENIMIENTO'
        )


    def __str__(self):
        return f"{self.codigo} - {self.marca} {self.modelo}"
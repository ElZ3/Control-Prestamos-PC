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
from django.db import models
from django.core.validators import RegexValidator

class Carrera(models.Model):
    ESTADO_CHOICES = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    ]
    
    creado_por = models.ForeignKey(
    'usuario.Usuario',
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='carreras_creadas'
    )

    codigo = models.CharField(
        max_length=6,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[A-Z]{3}\d{3}$',
                message='El código debe tener 3 letras mayúsculas seguidas de 3 números (Ej: MAT123).'
            )
        ],
        verbose_name='Código'
    )
    nombre = models.CharField(
        max_length=150,
        validators=[
            RegexValidator(
               regex=r'^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9\s]+$',
                message='El nombre solo permite letras, números y espacios.'
            )
        ]
    )
    descripcion = models.TextField(
        validators=[
            RegexValidator(
                # Permite letras, números, espacios y signos de puntuación básicos
                regex=r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s\.,;\-]+$',
                message='La descripción solo puede contener letras, números y signos de puntuación.'
            )
        ],
        verbose_name='Descripción'
    )
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='ACTIVO'
    )

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
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
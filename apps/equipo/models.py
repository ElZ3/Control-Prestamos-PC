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
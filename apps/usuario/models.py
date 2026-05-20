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
import re
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError
from apps.carrera.models import Carrera

##################################    
# +================================+
#
# MODELO: ADMINISTRADOR
#
# +================================+
##################################

# =========================
# VALIDACIONES
# =========================

def validate_solo_letras(value):
    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', value):
        raise ValidationError('Este campo solo debe contener letras.')

def validate_carnet(value):
    if not re.match(r'^\d{4}-[A-Z]{2}-\d{3}$', value):
        raise ValidationError('Formato requerido: 2023-AA-123.')

def validate_dui(value):
    if not re.match(r'^\d{9}$', value):
        raise ValidationError('El DUI debe contener exactamente 9 números.')

def validate_telefono(value):
    if not re.match(r'^\d{8}$', value):
        raise ValidationError('El teléfono debe tener exactamente 8 dígitos.')

def validate_email_catolica(value):
    if not value.lower().endswith('@catolica.edu.sv'):
        raise ValidationError('Debe ser correo institucional (@catolica.edu.sv).')

def validate_password_strength(value):
    if len(value) < 8:
        raise ValidationError("Mínimo 8 caracteres, debe incluir letras, debe incluir números y debe incluir carácter especial.")
    if not re.search(r"[a-zA-Z]", value):
        raise ValidationError("Debe incluir letras.")
    if not re.search(r"[0-9]", value):
        raise ValidationError("Debe incluir números.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
        raise ValidationError("Debe incluir carácter especial.")

# --- MANAGER ---
class UsuarioManager(BaseUserManager):
    def create_user(self, carnet, password=None, **extra_fields):
        if not carnet:
            raise ValueError('El carnet es obligatorio')

        extra_fields.setdefault('is_active', True)

        user = self.model(
            carnet=carnet,
            username=carnet,
            **extra_fields
        )

        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, carnet, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('rol', 'superadministrador')

        return self.create_user(carnet, password, **extra_fields)

# --- MODELO ---
class Usuario(AbstractUser):
    ROLES = (
        ('administrador', 'Administrador'),
        ('superadministrador', 'Superadministrador'),
    )
    
    creado_por = models.ForeignKey(
    'usuario.Usuario',
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='usuario_creados'
    )

    carnet = models.CharField(max_length=12, unique=True, validators=[validate_carnet])
    nombre = models.CharField(max_length=100, validators=[validate_solo_letras])
    apellido = models.CharField(max_length=100, validators=[validate_solo_letras])
    correo = models.EmailField(unique=True, validators=[validate_email_catolica])   
    telefono = models.CharField(max_length=8, validators=[validate_telefono])
    dui = models.CharField(max_length=9, unique=True, validators=[validate_dui])
    rol = models.CharField(max_length=20, choices=ROLES, default='administrador')

    objects = UsuarioManager()

    USERNAME_FIELD = 'carnet'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'correo', 'dui', 'telefono']

    def save(self, *args, **kwargs):
        self.username = self.carnet
        super().save(*args, **kwargs)

    def tiene_registros(self):
        # Lógica para verificar si tiene registros en el sistema
        return False
    
##################################    
# +================================+
#
# MODELO: PRESTATARIO
#
# +================================+
##################################

class Prestatario(models.Model):
    TIPOS = (
        ('ESTUDIANTE', 'Estudiante'),
        ('DOCENTE', 'Docente'),
    )

    ESTADOS = (
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    )
    
    creado_por = models.ForeignKey(
    'usuario.Usuario',
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='prestatarios_creados'
    )

    carnet = models.CharField(max_length=12, unique=True, validators=[validate_carnet])
    nombre = models.CharField(max_length=100, validators=[validate_solo_letras])
    apellido = models.CharField(max_length=100, validators=[validate_solo_letras])
    correo = models.EmailField(unique=True, validators=[validate_email_catolica])
    dui = models.CharField(max_length=9, unique=True, validators=[validate_dui])
    tipo = models.CharField(max_length=15, choices=TIPOS, default='ESTUDIANTE')
    estado = models.CharField(max_length=10, choices=ESTADOS, default='ACTIVO')

    carrera = models.ForeignKey(
        'carrera.Carrera',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    def tiene_prestamos(self):
        # Aquí irá la lógica cuando crees el módulo de préstamos
        # Ejemplo: return self.prestamo_set.exists()
        return False # Falso por defecto para poder probar la eliminación

    def __str__(self):
        return f"{self.carnet} - {self.nombre} {self.apellido}"
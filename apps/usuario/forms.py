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
from .models import Usuario, Prestatario
from .models import validate_password_strength, validate_dui
from apps.carrera.models import Carrera

##################################    
# +================================+
#
# FORM: ADMINISTRADOR
#
# +================================+
##################################

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese contraseña'
        }),
        required=True,
        label="Contraseña",
        help_text="Mínimo 8 caracteres, letras, números y un carácter especial.",
        error_messages={
            'required': 'La contraseña es obligatoria.'
        }
    )

    class Meta:
        model = Usuario
        fields = ['carnet', 'nombre', 'apellido', 'correo', 'telefono', 'dui', 'rol', 'is_active']
        widgets = {
            'carnet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2000-AB-200'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'dui': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sin guiones'}),
            'rol': forms.Select(attrs={'class': 'form-select'}),
            'is_active': forms.Select(choices=[(True, 'Activo'), (False, 'Inactivo')], attrs={'class': 'form-select'}),
        }
        
        error_messages = {
            'carnet': {
                'required': 'El carnet es obligatorio.',
                'unique': 'Este carnet ya está registrado.'
            },
            'nombre': {
                'required': 'El nombre es obligatorio.'
            },
            'apellido': {
                'required': 'El apellido es obligatorio.'
            },
            'correo': {
                'required': 'El correo es obligatorio.',
                'unique': 'Este correo ya está en uso.'
            },
            'telefono': {
                'required': 'El teléfono es obligatorio.'
            },
            'dui': {
                'required': 'El DUI es obligatorio.',
                'unique': 'Este DUI ya existe.'
            },
            'rol': {
                'required': 'Debe seleccionar un rol.'
            },
            'is_active': {
                'required': 'Debe seleccionar un estado.'
            }
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Si existe instancia → es edición
        if self.instance and self.instance.pk:
            self.fields['password'].required = False
            self.fields['password'].help_text = "Déjalo vacío si no deseas cambiar la contraseña."
            self.fields['password'].widget.attrs['placeholder'] = "Nueva contraseña (opcional)"



    def clean_password(self):
        password = self.cleaned_data.get("password")
        if password:
            validate_password_strength(password)
        return password

    def clean_dui(self):
        dui = self.cleaned_data.get("dui")
        validate_dui(dui)
        return dui

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user
    
##################################    
# +================================+
#
# FORM: PRESTATARIO
#
# +================================+
##################################

class PrestatarioForm(forms.ModelForm):

    carrera = forms.ModelChoiceField(
        queryset=Carrera.objects.filter(estado='ACTIVO'),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'select-carrera'
        }),
        empty_label="--- Seleccione una carrera ---"
    )

    class Meta:
        model = Prestatario

        fields = [
            'tipo',
            'carrera',
            'carnet',
            'dui',
            'nombre',
            'apellido',
            'correo',
            'estado'
        ]

        widgets = {
            'tipo': forms.Select(attrs={
                'class': 'form-select',
                'id': 'select-rol'
            }),

            'carnet': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '2000-AB-200'
            }),

            'dui': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sin guiones'
            }),

            'nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'apellido': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': '@catolica.edu.sv'
            }),

            'estado': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

        error_messages = {
            'carnet': {
                'required': 'El carnet es obligatorio.',
                'unique': 'Este carnet ya está registrado.'
            },

            'dui': {
                'required': 'El DUI es obligatorio.',
                'unique': 'Este DUI ya existe.'
            },

            'nombre': {
                'required': 'El nombre es obligatorio.'
            },

            'apellido': {
                'required': 'El apellido es obligatorio.'
            },

            'correo': {
                'required': 'El correo es obligatorio.',
                'unique': 'Este correo ya está en uso.'
            },

            'estado': {
                'required': 'Debe seleccionar un estado.'
            }
        }

    def clean(self):
        cleaned_data = super().clean()

        tipo = cleaned_data.get("tipo")
        carrera = cleaned_data.get("carrera")

        # Si es estudiante -> carrera obligatoria
        if tipo == 'ESTUDIANTE' and not carrera:
            self.add_error(
                'carrera',
                'El campo Carrera es obligatorio para los estudiantes.'
            )

        # Si es docente -> eliminar carrera
        if tipo == 'DOCENTE':
            cleaned_data['carrera'] = None

        return cleaned_data
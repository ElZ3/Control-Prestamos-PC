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

from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta

# DATOS SIMULADOS PARA EL PROTOTIPO
PRESTAMOS_MOCK = [
    {
        'pk': 101,
        'usuario': {'first_name': 'Carlos', 'last_name': 'Méndez'},
        'equipo': {'codigo': 'LAP-001', 'marca': 'Dell'},
        'fecha_prestamo': timezone.now() - timedelta(days=2),
        'fecha_limite': timezone.now() + timedelta(days=3),
        'condicion_entrega': 'Excelente',
        'estado': 'ACTIVO'
    },
    {
        'pk': 102,
        'usuario': {'first_name': 'Ana', 'last_name': 'Rivas'},
        'equipo': {'codigo': 'PROY-05', 'marca': 'Epson'},
        'fecha_prestamo': timezone.now() - timedelta(days=5),
        'fecha_limite': timezone.now() - timedelta(days=1),
        'condicion_entrega': 'Bueno',
        'estado': 'DEVUELTO'
    }
]

def prestamo_list(request):
    return render(request, 'prestamo/prestamo_list.html', {
        'prestamos': PRESTAMOS_MOCK
    })

def prestamo_create(request):
    if request.method == 'POST':
        # Aquí puedes simular la validación de "Usuario ya tiene préstamo"
        # messages.error(request, "Este usuario ya tiene un préstamo activo.")
        return redirect('prestamo_list')
    
    return render(request, 'prestamo/prestamo_form.html', {
        'titulo': 'Nuevo Préstamo'
    })

def prestamo_update(request, pk):
    # Simulamos que cargamos el préstamo 101
    prestamo_edit = PRESTAMOS_MOCK[0]
    return render(request, 'prestamo/prestamo_form.html', {
        'prestamo': prestamo_edit,
        'titulo': f'Editar Préstamo #{pk}'
    })

def prestamo_detail(request, pk):
    prestamo_ver = PRESTAMOS_MOCK[1] # Simulamos ver uno devuelto
    return render(request, 'prestamo/prestamo_detail.html', {
        'prestamo': prestamo_ver
    })

def prestamo_delete(request, pk):
    return redirect('prestamo_list')
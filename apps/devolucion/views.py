from django.shortcuts import render, redirect
from django.utils import timezone

# DATOS DE PRUEBA (MOCK DATA)
PRESTAMOS_FICTICIOS = [
    {
        'pk': 1,
        'equipo': {'codigo': 'LAP-001', 'marca': 'Dell Latitude'},
        'usuario': {'first_name': 'Juan', 'last_name': 'Pérez'},
        'fecha_prestamo': timezone.now(),
        'fecha_limite': timezone.now(),
        'estado': 'ACTIVO'
    },
    {
        'pk': 2,
        'equipo': {'codigo': 'PROY-05', 'marca': 'Epson PowerLite'},
        'usuario': {'first_name': 'Maria', 'last_name': 'García'},
        'fecha_prestamo': timezone.now(),
        'fecha_limite': timezone.now(),
        'estado': 'ACTIVO'
    }
]

def devolucion_list(request):
    # Pasamos la lista ficticia directamente
    return render(request, 'devolucion/devolucion_list.html', {
        'prestamos': PRESTAMOS_FICTICIOS,
        'today': timezone.now().date()
    })

def devolver_prestamo(request, pk):
    # Simulamos obtener el objeto (usamos el primero de la lista por defecto)
    prestamo_ejemplo = PRESTAMOS_FICTICIOS[0]
    
    if request.method == 'POST':
        # En el prototipo, no guardamos nada, solo simulamos éxito
        from django.contrib import messages
        messages.success(request, "Devolución registrada correctamente (Simulación).")
        return redirect('devolucion_list')

    return render(request, 'devolucion/devolucion_form.html', {
        'prestamo': prestamo_ejemplo
    })
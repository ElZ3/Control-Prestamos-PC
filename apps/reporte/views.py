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
from django.contrib import messages
from django.shortcuts import render

def dashboard(request):
    return render(request, "dashboard.html")

# --- DATOS MOCK PARA QUE LA TABLA NO ESTÉ VACÍA ---
MOCK_PRESTAMOS = [
    {'usuario': 'Juan Pérez', 'equipo': 'LAP-001', 'fecha_prestamo': '2026-04-20', 'fecha_limite': '2026-04-25', 'estado': 'PENDIENTE', 'condicion_entrega': 'BUENO'},
    {'usuario': 'Maria Lopez', 'equipo': 'PROY-02', 'fecha_prestamo': '2026-04-21', 'fecha_limite': '2026-04-24', 'estado': 'DEVUELTO', 'condicion_entrega': 'EXCELENTE'},
]

def dashboard_view(request):
    context = {
        "equipos_disponibles": 12,
        "equipos_prestados": 8,
        "equipos_mantenimiento": 2,
        "prestamos_hoy": 5,
    }
    return render(request, "reporte/dashboard.html", context)

def reporte_view(request):
    context = {
        'prestamos': MOCK_PRESTAMOS,
        'usuarios': [{'id':1, 'username': 'Maria Lopez'}],
        'equipos': [{'id':1, 'codigo': 'LAP-001', 'marca': 'Dell'}],
    }
    return render(request, 'reporte/reporte.html', context)

# ESTA ES LA FUNCIÓN QUE TE ESTÁ DANDO ERROR
def exportar_excel(request):
    # Por ahora, solo redirecciona para que no rompa el programa
    messages.info(request, "Función de exportación disponible en la versión final.")
    return redirect('reporte:reporte')

# Agregamos esta por si tus URLs también la llaman
def importar_excel(request):
    messages.info(request, "Función de importación disponible en la versión final.")
    return redirect('reporte:reporte')


def integrantes(request):
    raw_list = [
        {'first_name': 'Daniel', 'last_name': 'Pozo', 'role': 'Gerente del Proyecto', 'email': 'daniel.pozo@unicaes.edu.sv', 'image': 'img/integrantes/daniel_pozo.jpg'},
        {'first_name': 'Karla', 'last_name': 'Pineda', 'role': 'Análisis de Requerimientos', 'email': 'karla.pineda@unicaes.edu.sv', 'image': 'img/integrantes/karla_pineda.jpg'},
        {'first_name': 'Ana', 'last_name': 'Villeda', 'role': 'Diseño UI/UX', 'email': 'ana.villeda@unicaes.edu.sv', 'image': 'img/integrantes/ana_villeda.jpg'},
        {'first_name': 'Fabio', 'last_name': 'DelaCruz', 'role': 'Diseño / Tester y QA', 'email': 'fabio.delacruz@unicaes.edu.sv', 'image': 'img/integrantes/fabio_de.jpg'},
        {'first_name': 'Samuel', 'last_name': 'Ventura', 'role': 'Desarrollador Backend/Frontend', 'email': 'samuel.ventura@unicaes.edu.sv', 'image': 'img/integrantes/samuel_ventura.jpg'},
        {'first_name': 'Diego', 'last_name': 'Escobar', 'role': 'Desarrollador Backend/Frontend', 'email': 'diego.escobar@unicaes.edu.sv', 'image': 'img/integrantes/diego_escobar.jpg'},
        {'first_name': 'Ervin', 'last_name': 'Durán', 'role': 'Soporte y Mantenimiento', 'email': 'ervin.duran@unicaes.edu.sv', 'image': 'img/integrantes/ervin_duran.jpg'},
        {'first_name': 'William', 'last_name': 'Deras', 'role': 'Soporte y Mantenimiento', 'email': 'william.deras@unicaes.edu.sv', 'image': 'img/integrantes/william_deras.jpg'},
    ]

    integrantes_list = []
    for r in raw_list:
        # Primer apellido (token antes del primer espacio)
        first_surname = r['last_name'].split()[0]
        item = r.copy()
        item['first_surname'] = first_surname
        integrantes_list.append(item)

    context = {
        'integrantes': integrantes_list,
    }
    return render(request, 'integrantes.html', context)
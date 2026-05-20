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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from apps.reporte.views import dashboard
from apps.reporte.views import integrantes

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rutas de Autenticación nativas de Django
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Ruta de la aplicación (Inicio/Gráficas)
    path('inicio/', dashboard, name='home'),
    
    # URLs de apps
    path('usuarios/', include('apps.usuario.urls')),
    path('carreras/', include('apps.carrera.urls')),
    path('equipo/', include('apps.equipo.urls')),
    path('prestamo/', include('apps.prestamo.urls')),
    path('devolucion/', include('apps.devolucion.urls')),
    path('reporte/', include('apps.reporte.urls')),
    # Página estática del equipo de desarrollo
    path('integrantes/', integrantes, name='integrantes'),
]
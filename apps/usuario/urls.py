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
from django.urls import path
from . import views

urlpatterns = [
    
##################################    
# +================================+
#
# URLS: ADMINISTRADOR
#
# +================================+
##################################

    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('administradores/', views.UsuarioListView.as_view(), name='usuario_list'),
    path('administradores/crear/', views.UsuarioCreateView.as_view(), name='usuario_create'),
    path('administradores/editar/<int:pk>/', views.UsuarioUpdateView.as_view(), name='usuario_edit'),
    path('administradores/eliminar/<int:pk>/', views.UsuarioDeleteView.as_view(), name='usuario_delete'),
    
##################################    
# +================================+
#
# URLS: PRESTATARIO
#
# +================================+
##################################
    
    path('prestatarios/', views.PrestatarioListView.as_view(), name='prestatario_list'),
    path('prestatarios/crear/', views.PrestatarioCreateView.as_view(), name='prestatario_create'),
    path('prestatarios/editar/<int:pk>/', views.PrestatarioUpdateView.as_view(), name='prestatario_update'),
    path('prestatarios/eliminar/<int:pk>/', views.PrestatarioDeleteView.as_view(), name='prestatario_delete')
]
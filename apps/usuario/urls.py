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
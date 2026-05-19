from django.urls import path
from . import views

urlpatterns = [
    path('equipos/', views.EquipoListView.as_view(), name='equipo_list'),
    path('equipos/nuevo/', views.EquipoCreateView.as_view(), name='equipo_create'),
    path('equipos/editar/<int:pk>/', views.EquipoUpdateView.as_view(), name='equipo_update'),
    path('equipos/eliminar/<int:pk>/', views.EquipoDeleteView.as_view(), name='equipo_delete'),
]
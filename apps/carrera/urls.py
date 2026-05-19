from django.urls import path
from . import views

urlpatterns = [
    path('carreras/', views.CarreraListView.as_view(), name='carrera_list'),
    path('carreras/crear/', views.CarreraCreateView.as_view(), name='carrera_create'),
    path('carreras/editar/<int:pk>/', views.CarreraUpdateView.as_view(), name='carrera_update'),
    path('carreras/desactivar/<int:pk>/', views.CarreraDeleteView.as_view(), name='carrera_delete'),
]
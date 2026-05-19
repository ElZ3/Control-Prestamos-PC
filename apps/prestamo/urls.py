from django.urls import path
from . import views

urlpatterns = [
    path('', views.prestamo_list, name='prestamo_list'),
    path('crear/', views.prestamo_create, name='prestamo_create'),
    path('editar/<int:pk>/', views.prestamo_update, name='prestamo_update'),
    path('eliminar/<int:pk>/', views.prestamo_delete, name='prestamo_delete'),

    path('detalle/<int:pk>/', views.prestamo_detail, name='prestamo_detail'),
]
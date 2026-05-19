from django.urls import path
from . import views

urlpatterns = [
    path('', views.devolucion_list, name='devolucion_list'),
    path('devolver/<int:pk>/', views.devolver_prestamo, name='devolver_prestamo'),
]
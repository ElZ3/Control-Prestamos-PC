from django.urls import path
from .views import reporte_view, exportar_excel, dashboard_view

app_name = "reporte"

urlpatterns = [
    path('', reporte_view, name='reporte'),
    path('excel/', exportar_excel, name='exportar_excel'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
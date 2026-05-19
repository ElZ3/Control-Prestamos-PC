"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
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
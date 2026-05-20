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
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from .models import Carrera
from apps.usuario.models import Prestatario
from .forms import CarreraForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# --- MIXIN DE SEGURIDAD ---
class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Permite acceso solo a usuarios autenticados con rol:
    - administrador
    - superadministrador
    """

    def test_func(self):
        user = self.request.user

        if not user.is_authenticated:
            return False

        # Validación por rol (principal)
        if user.rol in ['administrador', 'superadministrador']:
            return True

        # Fallback por flags de Django (por seguridad)
        if user.is_staff or user.is_superuser:
            return True

        return False

    def handle_no_permission(self):
        return redirect('login')  

class CarreraListView(AdminRequiredMixin, ListView):
    model = Carrera
    template_name = 'carrera/carrera_list.html'
    context_object_name = 'carreras'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Carrera.objects.filter(
                Q(codigo__icontains=query) | Q(nombre__icontains=query)
            ).order_by('codigo')
        return Carrera.objects.all().order_by('codigo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


class CarreraCreateView(AdminRequiredMixin, CreateView):
    model = Carrera
    form_class = CarreraForm
    template_name = 'carrera/carrera_form.html'
    success_url = reverse_lazy('carrera_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Carrera'
        return context

    def form_valid(self, form):

        # GUARDAR USUARIO QUE CREÓ
        form.instance.creado_por = self.request.user

        messages.success(
            self.request,
            'Carrera registrada con éxito.'
        )

        return super().form_valid(form)

class CarreraUpdateView(AdminRequiredMixin, UpdateView):
    model = Carrera
    form_class = CarreraForm
    template_name = 'carrera/carrera_form.html'
    success_url = reverse_lazy('carrera_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Carrera'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Carrera actualizada correctamente.')
        return super().form_valid(form)


class CarreraDeleteView(AdminRequiredMixin, DeleteView):

    model = Carrera

    success_url = reverse_lazy('carrera_list')

    def post(self, request, *args, **kwargs):

        carrera = self.get_object()

        # Verificar si existe algún prestatario usando esta carrera
        en_uso = Prestatario.objects.filter(
            carrera=carrera
        ).exists()

        if en_uso:

            messages.error(
                request,
                'No se puede eliminar la carrera porque ya está asignada a prestatarios.'
            )

            return redirect('carrera_list')

        messages.success(
            request,
            'Carrera eliminada correctamente.'
        )

        return super().post(request, *args, **kwargs)
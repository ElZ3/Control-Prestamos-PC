from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from .models import Equipo
from .forms import EquipoForm

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
    
# --- VISTAS DE EQUIPOS ---

class EquipoListView(AdminRequiredMixin, ListView):
    model = Equipo
    template_name = 'equipo/equipo_list.html'
    context_object_name = 'equipos'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            # Búsqueda por Código, Marca o Modelo usando Q objects (OR lógico)
            queryset = queryset.filter(
                Q(codigo__icontains=q) | 
                Q(marca__icontains=q) | 
                Q(modelo__icontains=q)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

class EquipoCreateView(AdminRequiredMixin, CreateView):
    model = Equipo
    form_class = EquipoForm
    template_name = 'equipo/equipo_form.html'
    success_url = reverse_lazy('equipo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nuevo Equipo'
        return context

    def form_valid(self, form):

        form.instance.creado_por = self.request.user

        messages.success(
            self.request,
            "Equipo registrado exitosamente."
        )

        return super().form_valid(form)

class EquipoUpdateView(AdminRequiredMixin, UpdateView):
    model = Equipo
    form_class = EquipoForm
    template_name = 'equipo/equipo_form.html'
    success_url = reverse_lazy('equipo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Equipo'
        return context

    def form_valid(self, form):
        messages.success(self.request, "Equipo actualizado correctamente.")
        return super().form_valid(form)

class EquipoDeleteView(AdminRequiredMixin, DeleteView):
    model = Equipo
    success_url = reverse_lazy('equipo_list')

    def post(self, request, *args, **kwargs):
        messages.success(request, "Equipo eliminado correctamente.")
        return super().post(request, *args, **kwargs)
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Usuario, Prestatario
from .forms import UsuarioForm, PrestatarioForm

class AdminOrSuperAdminRequiredMixin(UserPassesTestMixin):

    allowed_roles = []

    def test_func(self):

        if not self.request.user.is_authenticated:
            return False

        return self.request.user.rol in self.allowed_roles

    def handle_no_permission(self):

        if not self.request.user.is_authenticated:
            return redirect('login')

        messages.error(
            self.request,
            "No tienes permisos para acceder a esta sección."
        )

        return redirect('prestatario_list')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    
    def form_valid(self, form):
        user = form.get_user()
        if not user.is_active:
            messages.error(self.request, "Esta cuenta está inactiva.")
            return self.form_invalid(form)
        return super().form_valid(form)
    
##################################    
# +================================+
#
# VIEWS: ADMINISTRADOR
#
# +================================+
##################################

class UsuarioListView(LoginRequiredMixin, AdminOrSuperAdminRequiredMixin, ListView):
    allowed_roles = ['superadministrador']
    model = Usuario
    template_name = 'usuario/administrador_list.html'
    context_object_name = 'usuarios'

class UsuarioCreateView(LoginRequiredMixin, AdminOrSuperAdminRequiredMixin, CreateView):
    allowed_roles = ['superadministrador']
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/administrador_form.html'
    success_url = reverse_lazy('usuario_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Usuario'
        return context

    def form_valid(self, form):

        form.instance.creado_por = self.request.user

        messages.success(
            self.request,
            "Usuario creado exitosamente."
        )

        return super().form_valid(form)

class UsuarioUpdateView(LoginRequiredMixin, AdminOrSuperAdminRequiredMixin, UpdateView):
    allowed_roles = ['superadministrador']
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/administrador_form.html'
    success_url = reverse_lazy('usuario_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Usuario'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Usuario editado exitosamente.")
        return super().form_valid(form)

class UsuarioDeleteView(LoginRequiredMixin, AdminOrSuperAdminRequiredMixin, DeleteView):

    allowed_roles = ['superadministrador']

    model = Usuario
    success_url = reverse_lazy('usuario_list')

    def post(self, request, *args, **kwargs):

        usuario = self.get_object()

        # NO puede eliminarse a sí mismo
        if usuario == request.user:

            messages.error(
                request,
                "No puedes eliminar tu propio usuario."
            )

            return redirect('usuario_list')

        # NO puede eliminar usuarios con acciones
        if usuario.tiene_registros():

            messages.warning(
                request,
                "No se puede eliminar el usuario porque "
                "ha realizado acciones en el sistema."
            )

            return redirect('usuario_list')

        messages.success(
            request,
            "Usuario eliminado correctamente."
        )

        return super().post(request, *args, **kwargs)
    
##################################    
# +================================+
#
# VIEWS: PRESTATARIO
#
# +================================+
################################## 

class PrestatarioListView(LoginRequiredMixin, AdminOrSuperAdminRequiredMixin, ListView):
    allowed_roles = ['administrador', 'superadministrador']
    model = Prestatario
    template_name = 'usuario/prestatario_list.html'
    context_object_name = 'usuarios'

class PrestatarioCreateView(LoginRequiredMixin, AdminOrSuperAdminRequiredMixin, CreateView):
    allowed_roles = ['administrador', 'superadministrador']
    model = Prestatario
    form_class = PrestatarioForm
    template_name = 'usuario/prestatario_form.html'
    success_url = reverse_lazy('prestatario_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Prestatario'
        return context

    def form_valid(self, form):

        form.instance.creado_por = self.request.user

        messages.success(
            self.request,
            "Prestatario registrado exitosamente."
        )

        return super().form_valid(form)

class PrestatarioUpdateView(LoginRequiredMixin, AdminOrSuperAdminRequiredMixin, UpdateView):
    allowed_roles = ['administrador', 'superadministrador']
    model = Prestatario
    form_class = PrestatarioForm
    template_name = 'usuario/prestatario_form.html'
    success_url = reverse_lazy('prestatario_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Prestatario'
        return context

    def form_valid(self, form):
        messages.success(self.request, "Prestatario actualizado correctamente.")
        return super().form_valid(form)

class PrestatarioDeleteView(LoginRequiredMixin, AdminOrSuperAdminRequiredMixin, DeleteView):
    allowed_roles = ['administrador', 'superadministrador']

    model = Prestatario
    success_url = reverse_lazy('prestatario_list')

    def post(self, request, *args, **kwargs):
        messages.success(
            request,
            "Prestatario eliminado correctamente."
        )

        return super().post(request, *args, **kwargs)
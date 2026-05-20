"""
====================================================================
SISTEMA DE GESTIÓN DE PRÉSTAMO DE LAPTOPS (RESO-LAP)
====================================================================
Descripción: Aplicación backend en Django para el control, asignación y devolución de laptops.
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

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import Group
# from django.contrib import messages
# from .models import Usuario

# admin.site.unregister(Group)

# @admin.register(Usuario)
# class CustomUserAdmin(UserAdmin):
#     model = Usuario
    
#     # 1. FORMULARIO DE EDICIÓN: Agregamos el campo 'estado'
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Información Personal', {'fields': ('first_name', 'last_name', 'email')}),
#         ('Roles y Estado', {'fields': ('rol', 'estado')}), 
#         ('Fechas Importantes', {'fields': ('last_login', 'date_joined')}),
#     )
    
#     # 2. SOLUCIÓN A LA CONTRASEÑA EN CREACIÓN:
#     # Usamos UserAdmin.add_fieldsets (que ya trae las contraseñas) y le SUMAMOS nuestros campos
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         ('Información Adicional Obligatoria', {
#             'classes': ('wide',),
#             'fields': ('first_name', 'last_name', 'email', 'rol', 'estado'),
#         }),
#     )

#     list_display = ['username', 'first_name', 'last_name', 'email', 'rol', 'estado']
#     list_filter = ['rol', 'estado']
#     search_fields = ['username', 'first_name', 'last_name', 'email']

#     # --- Permisos de Visualización y Edición ---
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if not request.user.is_superuser:
#             return qs.exclude(rol=Usuario.Roles.SUPERADMIN)
#         return qs

#     def has_add_permission(self, request):
#         return request.user.is_superuser

#     def has_change_permission(self, request, obj=None):
#         if not request.user.is_superuser:
#             if obj:
#                 if obj.rol == Usuario.Roles.SUPERADMIN:
#                     return False
#                 if obj.rol == Usuario.Roles.ADMIN and obj != request.user:
#                     return False
#         return super().has_change_permission(request, obj)

#     # ==========================================
#     # LÓGICA DE ELIMINACIÓN (SOFT DELETE)
#     # ==========================================

#     def has_delete_permission(self, request, obj=None):
#         if not request.user.is_superuser:
#             return False
#         # El Superadmin no puede eliminarse a sí mismo
#         if obj and obj == request.user:
#             return False
#         return True

#     def delete_model(self, request, obj):
#         """
#         Intercepta cuando el Superadmin hace clic en "Eliminar" en el perfil.
#         En lugar de borrar de la base de datos, lo marca como INACTIVO.
#         """
#         obj.estado = Usuario.Estados.INACTIVO
#         obj.save()
#         self.message_user(request, f"El usuario {obj.username} no se borró por seguridad de la base de datos, pero fue marcado como INACTIVO.", level=messages.WARNING)

#     def delete_queryset(self, request, queryset):
#         """
#         Intercepta cuando el Superadmin selecciona varios usuarios y elige "Eliminar seleccionados".
#         """
#         for obj in queryset:
#             obj.estado = Usuario.Estados.INACTIVO
#             obj.save()
#         self.message_user(request, "Los usuarios seleccionados han sido marcados como INACTIVOS en lugar de eliminarse por completo.", level=messages.WARNING)
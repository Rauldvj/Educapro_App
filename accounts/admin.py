from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile

# Define una clase inline para el perfil del usuario
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'perfiles'
    fields = ('image', 'rut', 'direccion', 'region', 'comuna', 'telefono', 
              'apellido_paterno', 'apellido_materno', 'creado_por_coordinador')

# Define una clase personalizada para el modelo de administración del usuario
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'email')
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('first_name', 'email')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Define una clase personalizada para el modelo de administración del perfil
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'apellido_paterno', 'apellido_materno', 'rut', 
                    'direccion', 'region', 'comuna', 'telefono', 'creado_por_coordinador')
    search_fields = ('rut', 'user__username', 'apellido_paterno', 'apellido_materno')
    list_filter = ('region', 'comuna', 'creado_por_coordinador')

admin.site.register(Profile, ProfileAdmin)

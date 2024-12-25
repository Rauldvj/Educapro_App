from django.contrib import admin
from .models import RegistroPie

class RegistroPieAdmin(admin.ModelAdmin):
    list_display = ('año_registro', 'curso', 'estudiante', 'apoderado_titular')	
    
    fieldsets = (
        ('Datos del Estudiante', {
            'fields': ('estudiante', 'apoderado_titular')
        }),
        ('Datos de la Matricula', {
            'fields': ('año_registro', 'curso', 'enable')
        }),
    )

admin.site.register(RegistroPie, RegistroPieAdmin)
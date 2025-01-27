# estudiantes/apps.py

from django.apps import AppConfig

class EstudiantesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'estudiantes'

    def ready(self):
        import estudiantes.signals  # Importamos las señales cuando la aplicación esté lista

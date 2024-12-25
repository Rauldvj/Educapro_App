import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from estudiantes.models import Estudiante, ApoderadoTitular, BitacoraEstudiante, ObjetivoSemanal
from pie.models import RegistroPie
from app.models import Anamnesis

@receiver(post_save, sender=Estudiante)
def crear_o_actualizar_registro_pie(sender, instance, created, **kwargs):
    if created:
        # Crear un nuevo RegistroPie cuando se crea un nuevo estudiante
        RegistroPie.objects.create(
            estudiante=instance,
            curso=instance.cursos,
            enable=instance.enable,
            año_matricula=datetime.now().year  # Registrar el año de creación
        )
    else:
        # Actualizar los campos en RegistroPie si el estudiante ya existe
        registro_pie = RegistroPie.objects.filter(estudiante=instance).first()
        if registro_pie:
            registro_pie.curso = instance.cursos
            registro_pie.enable = instance.enable
            registro_pie.save()

# -------------------------------------------------------------------------------------------------
# Actualizar registros en simultaneo con el registro PIE del Apoderado Titular

@receiver(post_save, sender=ApoderadoTitular)
def actualizar_apoderado_titular_registro_pie(sender, instance, **kwargs):
    try:
        registro_pie = RegistroPie.objects.get(estudiante=instance.estudiante)
        registro_pie.apoderado_titular = instance  # Actualiza el apoderado titular
        registro_pie.save()  # Guarda los cambios en el registro PIE
    except RegistroPie.DoesNotExist:
        pass  # Si no existe un registro PIE, no hace nada

# -------------------------------------------------------------------------------------------------

@receiver(post_save, sender=BitacoraEstudiante)
def actualizar_avance(sender, instance, **kwargs):
    objetivos = ObjetivoSemanal.objects.filter(bitacora=instance)
    for objetivo in objetivos:
        objetivo.save()
from django.db import models
from estudiantes.models import Estudiante, ApoderadoTitular, Curso
from datetime import datetime


# Modelo de RegistroPie
class RegistroPie(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE, verbose_name='Estudiante')
    apoderado_titular = models.ForeignKey(ApoderadoTitular, on_delete=models.CASCADE, verbose_name='Apoderado', null=True, blank=True)
    año_registro = models.PositiveIntegerField(verbose_name='Año de Registro en PIE')

    def save(self, *args, **kwargs):
        if self._state.adding and not self.año_registro:
            self.año_registro = datetime.now().year
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.estudiante}'
    
    class Meta:
        verbose_name = 'Pie'
        verbose_name_plural = 'Pies'
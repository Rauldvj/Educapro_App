# Generated by Django 5.1.4 on 2024-12-12 15:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroPie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año_registro', models.PositiveIntegerField(verbose_name='Año de Registro en PIE')),
                ('apoderado_titular', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estudiantes.apoderadotitular', verbose_name='Apoderado')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.curso', verbose_name='Curso')),
                ('estudiante', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.estudiante', verbose_name='Estudiante')),
            ],
            options={
                'verbose_name': 'Pie',
                'verbose_name_plural': 'Pies',
            },
        ),
    ]

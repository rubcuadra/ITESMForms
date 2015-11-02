# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import students.models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20150912_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno_Profesional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('complete_name', models.CharField(max_length=120, verbose_name='Nombre y Apellidos')),
                ('birth_date', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('phone_number', models.CharField(max_length=10, verbose_name='TelCasa')),
                ('cellphone_number', models.CharField(max_length=10, verbose_name='Celular')),
                ('email', models.EmailField(max_length=254, verbose_name='Mail')),
                ('facebook', models.CharField(max_length=120, verbose_name='Facebook: ')),
                ('twitter', models.CharField(max_length=120, verbose_name='Twitter')),
                ('high_school', models.CharField(max_length=120, verbose_name='Nombre de Preparatoria')),
                ('average', models.DecimalField(default=75.0, verbose_name='Promedio de Preparatoria', max_digits=4, decimal_places=2)),
                ('interests', models.CharField(max_length=9, verbose_name='Carreras de Interes', validators=[students.models.validate_length])),
                ('starting_date', models.CharField(max_length=2, verbose_name='Periodo de Ingreso', choices=[(b'AD', b'Agosto-Diciembre'), (b'EM', b'Enero-Mayo')])),
                ('starting_year', models.IntegerField(verbose_name='Year de Ingreso', validators=[students.models.validate_year])),
            ],
        ),
        migrations.RemoveField(
            model_name='alumno_preparatoria',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Nombre y Apellidos'),
        ),
    ]

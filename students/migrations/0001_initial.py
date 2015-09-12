# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno_Preparatoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('average', models.DecimalField(verbose_name='Promedio de Secundaria', max_digits=4, decimal_places=2)),
                ('name', models.CharField(max_length=120, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=120, null=True, verbose_name='Apellidos', blank=True)),
                ('birth_date', models.DateTimeField(verbose_name='Fecha de Nacimiento')),
                ('nationality', models.CharField(max_length=120, null=True, verbose_name='Nacionalidad', blank=True)),
                ('high_school', models.CharField(max_length=120, null=True, verbose_name='Secundaria', blank=True)),
                ('phone_number', models.CharField(max_length=10, verbose_name='TelCasa', blank=True)),
                ('cellphone_number', models.CharField(max_length=10, verbose_name='Celular', blank=True)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Mail', blank=True)),
                ('street_and_number', models.CharField(max_length=200, null=True, verbose_name='Calle y Numero', blank=True)),
                ('district_and_zipcode', models.CharField(max_length=200, null=True, verbose_name='Colonia y C.P', blank=True)),
                ('city_and_county', models.CharField(max_length=200, null=True, verbose_name='Ciudad y Estado', blank=True)),
                ('father_name', models.CharField(max_length=120, verbose_name='Nombre de Padre')),
                ('mother_name', models.CharField(max_length=120, verbose_name='Nombre de Madre')),
                ('program', models.CharField(default=b'PTB', max_length=3, choices=[(b'PTB', b'Preparatoria Bilingue'), (b'PTM', b'Preparatoria Bicultural'), (b'IB', b'Preparatoria Internacional')])),
                ('exam_done', models.CharField(default=b'No', max_length=2, choices=[(b'Si', b'Si'), (b'No', b'No')])),
            ],
        ),
    ]

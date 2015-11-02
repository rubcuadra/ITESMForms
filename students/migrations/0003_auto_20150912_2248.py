# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20150911_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno_preparatoria',
            name='graduation_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 12, 22, 46, 48, 866362, tzinfo=utc), verbose_name='Fecha de Graduacion '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='average',
            field=models.DecimalField(default=75.0, verbose_name='Promedio de Secundaria', max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 12, 22, 46, 55, 71032, tzinfo=utc), verbose_name='Fecha de Nacimiento'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='cellphone_number',
            field=models.CharField(max_length=10, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='city_and_county',
            field=models.CharField(default='Mexico DF', max_length=200, verbose_name='Ciudad y Estado'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='district_and_zipcode',
            field=models.CharField(default='DF 0', max_length=200, verbose_name='Colonia y C.P'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='email',
            field=models.EmailField(default='a@a.com', max_length=254, verbose_name='Mail'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='exam_done',
            field=models.CharField(default=b'No', max_length=2, verbose_name='Ya presentaste examen?', choices=[(b'Si', b'Si'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='high_school',
            field=models.CharField(default='Tec', max_length=120, verbose_name='Nombre de Secundaria'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='last_name',
            field=models.CharField(default='Tec', max_length=120, verbose_name='Apellidos'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='nationality',
            field=models.CharField(default='Mexicana', max_length=120, verbose_name='Nacionalidad'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='phone_number',
            field=models.CharField(max_length=10, verbose_name='TelCasa'),
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='program',
            field=models.CharField(max_length=3, verbose_name='Programa Academico: ', choices=[(b'PTB', b'Preparatoria Bilingue'), (b'PTM', b'Preparatoria Bicultural'), (b'IB', b'Preparatoria Internacional')]),
        ),
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='street_and_number',
            field=models.CharField(default='Street and number', max_length=200, verbose_name='Calle y Numero'),
            preserve_default=False,
        ),
    ]

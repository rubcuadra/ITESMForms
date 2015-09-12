# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno_preparatoria',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='Fecha de Nacimiento', blank=True),
        ),
    ]

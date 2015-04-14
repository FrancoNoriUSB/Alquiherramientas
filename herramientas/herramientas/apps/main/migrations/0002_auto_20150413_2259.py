# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='fecha_expiracion',
        ),
        migrations.AddField(
            model_name='producto',
            name='preguntas',
            field=models.CharField(default='Preguntas frecuentes de los articulos', max_length=500),
            preserve_default=False,
        ),
    ]

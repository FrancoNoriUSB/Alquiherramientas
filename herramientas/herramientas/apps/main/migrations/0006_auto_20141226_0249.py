# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20141226_0224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alquiler',
            old_name='feche_actualizacion',
            new_name='fecha_actualizacion',
        ),
        migrations.RenameField(
            model_name='compra',
            old_name='feche_actualizacion',
            new_name='fecha_actualizacion',
        ),
    ]

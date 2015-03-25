# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0006_notificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificacion',
            name='tipo',
            field=models.CharField(max_length=20, choices=[(b'venta', b'venta'), (b'alquiler', b'alquiler'), (b'usuario', b'usuario')]),
            preserve_default=True,
        ),
    ]

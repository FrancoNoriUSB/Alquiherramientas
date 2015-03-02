# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_afiliacion_contactos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='aceptado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

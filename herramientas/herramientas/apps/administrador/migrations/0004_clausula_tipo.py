# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0003_auto_20150319_0337'),
    ]

    operations = [
        migrations.AddField(
            model_name='clausula',
            name='tipo',
            field=models.CharField(default='alquiler', max_length=30, choices=[(b'alquiler', b'alquiler'), (b'venta', b'venta')]),
            preserve_default=False,
        ),
    ]

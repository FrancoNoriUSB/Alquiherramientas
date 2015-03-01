# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_producto_disponible'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='cantidad',
            field=models.DecimalField(default=1, max_digits=10, decimal_places=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(default=1, max_length=10),
            preserve_default=True,
        ),
    ]

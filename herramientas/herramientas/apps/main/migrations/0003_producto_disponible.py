# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_pago_verificado'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='disponible',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]

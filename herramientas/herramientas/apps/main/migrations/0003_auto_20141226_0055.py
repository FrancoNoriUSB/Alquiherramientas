# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20141210_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='alquiler',
            name='oferta',
            field=models.BooleanField(default=False, help_text=b'Marcado si desea que se muestre como una oferta'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compra',
            name='oferta',
            field=models.BooleanField(default=False, help_text=b'Marcado si desea que se muestre como una oferta'),
            preserve_default=True,
        ),
    ]

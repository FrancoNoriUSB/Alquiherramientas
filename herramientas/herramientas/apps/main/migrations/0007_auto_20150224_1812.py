# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150224_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_expiracion',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]

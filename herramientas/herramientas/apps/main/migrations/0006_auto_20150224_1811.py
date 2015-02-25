# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_expiracion',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0004_clausula_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='clausula',
            name='texto',
            field=models.CharField(default=' ', max_length=10000),
            preserve_default=False,
        ),
    ]

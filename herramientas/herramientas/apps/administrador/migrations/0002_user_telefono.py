# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telefono',
            field=models.IntegerField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]

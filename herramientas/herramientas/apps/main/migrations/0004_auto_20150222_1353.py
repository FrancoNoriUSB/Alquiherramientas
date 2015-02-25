# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='info',
            field=models.CharField(max_length=1200),
            preserve_default=True,
        ),
    ]

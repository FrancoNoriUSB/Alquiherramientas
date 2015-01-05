# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20141227_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='imagen',
            field=models.ImageField(default='0', upload_to=b''),
            preserve_default=False,
        ),
    ]

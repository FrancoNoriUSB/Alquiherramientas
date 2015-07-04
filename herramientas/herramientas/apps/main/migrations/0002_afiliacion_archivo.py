# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='afiliacion',
            name='archivo',
            field=models.FileField(default='none', upload_to=b'uploads/archivos/'),
            preserve_default=False,
        ),
    ]

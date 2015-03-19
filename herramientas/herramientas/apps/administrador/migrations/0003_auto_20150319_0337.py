# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_clausula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clausula',
            name='archivo',
            field=models.FileField(upload_to=b'uploads/archivos/'),
            preserve_default=True,
        ),
    ]

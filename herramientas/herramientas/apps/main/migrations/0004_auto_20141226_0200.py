# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20141226_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='alquiler',
            name='fecha_expiracion',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 26, 6, 29, 42, 832000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alquiler',
            name='fecha_publicacion',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 26, 6, 29, 42, 832000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alquiler',
            name='feche_actualizacion',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 26, 6, 29, 50, 544000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='fecha_expiracion',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 26, 6, 30, 0, 80000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='fecha_publicacion',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 26, 6, 30, 11, 176000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='feche_actualizacion',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 26, 6, 30, 18, 992000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]

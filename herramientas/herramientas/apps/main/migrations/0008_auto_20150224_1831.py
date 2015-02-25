# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20150224_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='direccion',
            field=models.ForeignKey(to='main.Direccion', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='producto',
            name='herramienta',
            field=models.OneToOneField(null=True, to='main.Herramienta'),
            preserve_default=True,
        ),
    ]

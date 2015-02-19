# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_producto_cantidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info', models.CharField(max_length=800)),
                ('mision', models.CharField(max_length=800)),
                ('vision', models.CharField(max_length=800)),
                ('servicios', models.CharField(max_length=800)),
            ],
            options={
                'ordering': ('info',),
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
            bases=(models.Model,),
        ),
    ]

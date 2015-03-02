# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150301_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Afiliacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info', models.CharField(max_length=1200)),
                ('beneficios', models.CharField(max_length=800)),
            ],
            options={
                'ordering': ('info',),
                'verbose_name': 'Afiliacion',
                'verbose_name_plural': 'Afiliaciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telefonos', models.CharField(max_length=500)),
                ('correo', models.CharField(max_length=500)),
            ],
            options={
                'ordering': ('correo',),
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
            },
            bases=(models.Model,),
        ),
    ]

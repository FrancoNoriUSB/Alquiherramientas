# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('ciudad', models.CharField(max_length=40)),
                ('nacionalidad', models.CharField(default=b'V', max_length=1, choices=[(b'V', b'V'), (b'E', b'E')])),
                ('cedula', models.IntegerField(max_length=10)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
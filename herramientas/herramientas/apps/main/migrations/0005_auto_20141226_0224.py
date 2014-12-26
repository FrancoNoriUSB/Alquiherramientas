# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20141226_0200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='herramienta',
            name='categoria',
            field=models.ForeignKey(default=1, to='main.Categoria'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alquiler',
            name='fecha_expiracion',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]

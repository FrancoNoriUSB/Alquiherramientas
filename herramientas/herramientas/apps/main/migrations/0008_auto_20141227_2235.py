# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20141227_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('publicacion_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='main.Publicacion')),
                ('precio', models.DecimalField(max_digits=20, decimal_places=2)),
            ],
            options={
                'ordering': ('precio',),
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
            bases=('main.publicacion',),
        ),
        migrations.RemoveField(
            model_name='compra',
            name='publicacion_ptr',
        ),
        migrations.DeleteModel(
            name='Compra',
        ),
        migrations.AlterModelOptions(
            name='alquiler',
            options={'ordering': ('dias',), 'verbose_name': 'Alquiler', 'verbose_name_plural': 'Alquileres'},
        ),
        migrations.RenameField(
            model_name='alquiler',
            old_name='diasAlquiler',
            new_name='dias',
        ),
        migrations.RenameField(
            model_name='alquiler',
            old_name='precioDia',
            new_name='precio',
        ),
    ]

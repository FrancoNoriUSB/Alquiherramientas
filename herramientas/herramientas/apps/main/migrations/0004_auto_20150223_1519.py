# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('concepto', models.CharField(max_length=200)),
                ('monto', models.DecimalField(max_digits=20, decimal_places=2)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.EmailField(max_length=75)),
            ],
            options={
                'verbose_name': 'Pago',
                'verbose_name_plural': 'Pagos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PagoAlquiler',
            fields=[
                ('pago_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='main.Pago')),
                ('dias', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Pago Alquiler',
                'verbose_name_plural': 'Pago Alquilers',
            },
            bases=('main.pago',),
        ),
        migrations.CreateModel(
            name='PagoVenta',
            fields=[
                ('pago_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='main.Pago')),
            ],
            options={
                'verbose_name': 'Pago Venta',
                'verbose_name_plural': 'Pago Ventas',
            },
            bases=('main.pago',),
        ),
        migrations.AlterModelOptions(
            name='imagenproducto',
            options={'verbose_name': 'Imagen Producto', 'verbose_name_plural': 'Imagenes Producto'},
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alquiler',
            options={'ordering': ('diasAlquiler',), 'verbose_name': 'Alquiler', 'verbose_name_plural': 'Alquileres'},
        ),
        migrations.AlterModelOptions(
            name='ciudad',
            options={'ordering': ('nombre',), 'verbose_name': 'Ciudad', 'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='compra',
            options={'ordering': ('precio',), 'verbose_name': 'Compra', 'verbose_name_plural': 'Compras'},
        ),
        migrations.AlterModelOptions(
            name='direccion',
            options={'ordering': ('domicilio',), 'verbose_name': 'Direccion', 'verbose_name_plural': 'Direcciones'},
        ),
        migrations.AlterModelOptions(
            name='estado',
            options={'ordering': ('nombre',), 'verbose_name': 'Estado', 'verbose_name_plural': 'Estados'},
        ),
        migrations.AlterModelOptions(
            name='herramienta',
            options={'ordering': ('nombre',), 'verbose_name': 'Herramienta', 'verbose_name_plural': 'Herramientas'},
        ),
        migrations.AlterModelOptions(
            name='marca',
            options={'ordering': ('nombre',), 'verbose_name': 'Marca', 'verbose_name_plural': 'Marcas'},
        ),
        migrations.AlterModelOptions(
            name='modelo',
            options={'ordering': ('nombre',), 'verbose_name': 'Modelo', 'verbose_name_plural': 'Modelos'},
        ),
        migrations.AlterModelOptions(
            name='zona',
            options={'ordering': ('nombre',), 'verbose_name': 'Zona', 'verbose_name_plural': 'Zonas'},
        ),
        migrations.RenameField(
            model_name='ciudad',
            old_name='ciudad',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='estado',
            old_name='estado',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='marca',
            old_name='marca',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='modelo',
            old_name='modelo',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='zona',
            old_name='zona',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='herramienta',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='marca',
            name='modelo',
        ),
        migrations.AddField(
            model_name='alquiler',
            name='direccion',
            field=models.ForeignKey(default='0', to='main.Direccion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alquiler',
            name='herramienta',
            field=models.OneToOneField(default='0', to='main.Herramienta'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ciudad',
            name='estado',
            field=models.ForeignKey(default='0', to='main.Estado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='direccion',
            field=models.ForeignKey(default='0', to='main.Direccion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='herramienta',
            field=models.OneToOneField(default='0', to='main.Herramienta'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='direccion',
            name='domicilio',
            field=models.CharField(default='0', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='herramienta',
            name='modelo',
            field=models.ForeignKey(default='0', to='main.Modelo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modelo',
            name='marca',
            field=models.ForeignKey(default='0', to='main.Marca'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zona',
            name='ciudad',
            field=models.ForeignKey(default='0', to='main.Ciudad'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='direccion',
            name='ciudad',
            field=models.ForeignKey(to='main.Ciudad'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='direccion',
            name='estado',
            field=models.ForeignKey(to='main.Estado'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='direccion',
            name='zona',
            field=models.ForeignKey(to='main.Zona'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='herramienta',
            name='marca',
            field=models.ForeignKey(to='main.Marca'),
            preserve_default=True,
        ),
    ]

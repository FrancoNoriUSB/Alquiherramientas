# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20141226_0249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('contenido', models.CharField(max_length=10000)),
                ('oferta', models.BooleanField(default=False, help_text=b'Marcado si desea que se muestre como una oferta')),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('fecha_expiracion', models.DateTimeField()),
                ('direccion', models.ForeignKey(to='main.Direccion')),
                ('herramienta', models.OneToOneField(to='main.Herramienta')),
            ],
            options={
                'ordering': ('titulo',),
                'verbose_name': 'Publicacion',
                'verbose_name_plural': 'Publicaciones',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='alquiler',
            name='contenido',
        ),
        migrations.RemoveField(
            model_name='alquiler',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='alquiler',
            name='fecha_actualizacion',
        ),
        migrations.RemoveField(
            model_name='alquiler',
            name='fecha_expiracion',
        ),
        migrations.RemoveField(
            model_name='alquiler',
            name='fecha_publicacion',
        ),
        migrations.RemoveField(
            model_name='alquiler',
            name='herramienta',
        ),
        migrations.RemoveField(
            model_name='alquiler',
            name='id',
        ),
        migrations.RemoveField(
            model_name='alquiler',
            name='oferta',
        ),
        migrations.RemoveField(
            model_name='alquiler',
            name='titulo',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='contenido',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='fecha_actualizacion',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='fecha_expiracion',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='fecha_publicacion',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='herramienta',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='id',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='oferta',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='titulo',
        ),
        migrations.AddField(
            model_name='alquiler',
            name='publicacion_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='main.Publicacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='publicacion_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='main.Publicacion'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_herramienta_ano'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenPublicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(null=True, upload_to=b'uploads/img/')),
                ('thumbnail', models.ImageField(upload_to=b'uploads/img/thumbnails/', null=True, editable=False, blank=True)),
                ('descripcion', models.CharField(max_length=140, null=True)),
                ('publicacion', models.ForeignKey(related_name='imagenes', to='main.Publicacion')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'ImagenPublicacion',
                'verbose_name_plural': 'ImagenesPublicaciones',
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20141227_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenPublicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(null=True, upload_to=b'uploads/img/')),
                ('thumbnail', models.ImageField(upload_to=b'uploads/img/thumbnails/', null=True, editable=False, blank=True)),
                ('descripcion', models.CharField(max_length=140, null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'ImagenPublicacion',
                'verbose_name_plural': 'ImagenesPublicaciones',
            },
            bases=(models.Model,),
        ),
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
        migrations.AddField(
            model_name='imagenpublicacion',
            name='publicacion',
            field=models.ForeignKey(related_name='imagenes', to='main.Publicacion'),
            preserve_default=True,
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
        migrations.AddField(
            model_name='herramienta',
            name='ano',
            field=models.IntegerField(default=2015, max_length=4, choices=[(1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publicacion',
            name='imagen',
            field=models.ImageField(default=0, upload_to=b'uploads/publicaciones'),
            preserve_default=False,
        ),
    ]

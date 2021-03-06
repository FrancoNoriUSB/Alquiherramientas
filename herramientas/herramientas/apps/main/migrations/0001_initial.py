# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('nombre',),
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
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
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domicilio', models.CharField(max_length=100)),
                ('ciudad', models.ForeignKey(to='main.Ciudad')),
            ],
            options={
                'ordering': ('domicilio',),
                'verbose_name': 'Direccion',
                'verbose_name_plural': 'Direcciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info', models.CharField(max_length=1200)),
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
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('nombre',),
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Herramienta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('ano', models.IntegerField(default=2015, max_length=4, choices=[(1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015)])),
                ('categoria', models.ForeignKey(to='main.Categoria')),
            ],
            options={
                'ordering': ('nombre',),
                'verbose_name': 'Herramienta',
                'verbose_name_plural': 'Herramientas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImagenInicial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(upload_to=b'uploads/img/')),
                ('thumbnail', models.ImageField(upload_to=b'uploads/img/thumbnails/', null=True, editable=False, blank=True)),
                ('descripcion', models.CharField(max_length=140, null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Imagen Inicial',
                'verbose_name_plural': 'Imagenes Iniciales',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImagenProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(upload_to=b'uploads/img/')),
                ('thumbnail', models.ImageField(upload_to=b'uploads/img/thumbnails/', null=True, editable=False, blank=True)),
                ('descripcion', models.CharField(max_length=140, null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Imagen Producto',
                'verbose_name_plural': 'Imagenes Producto',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('nombre',),
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('marca', models.ForeignKey(to='main.Marca')),
            ],
            options={
                'ordering': ('nombre',),
                'verbose_name': 'Modelo',
                'verbose_name_plural': 'Modelos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto', models.DecimalField(max_digits=20, decimal_places=2)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('verificado', models.BooleanField(default=False)),
                ('cantidad', models.DecimalField(max_digits=10, decimal_places=0)),
                ('aceptado', models.BooleanField(default=False)),
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
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('contenido', models.CharField(max_length=10000)),
                ('cantidad', models.IntegerField(default=1, max_length=10)),
                ('oferta', models.BooleanField(default=False, help_text=b'Marcado si desea que se muestre como una oferta')),
                ('disponible', models.BooleanField(default=True)),
                ('preguntas', models.CharField(max_length=500)),
                ('fecha_producto', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('titulo',),
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('producto_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='main.Producto')),
                ('dias', models.IntegerField()),
                ('precio', models.DecimalField(max_digits=20, decimal_places=2)),
                ('visible', models.BooleanField(default=None)),
            ],
            options={
                'ordering': ('dias',),
                'verbose_name': 'Alquiler',
                'verbose_name_plural': 'Alquileres',
            },
            bases=('main.producto',),
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('producto_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='main.Producto')),
                ('precio', models.DecimalField(max_digits=20, decimal_places=2)),
                ('visible', models.BooleanField(default=None)),
            ],
            options={
                'ordering': ('precio',),
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
            bases=('main.producto',),
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('ciudad', models.ForeignKey(to='main.Ciudad')),
            ],
            options={
                'ordering': ('nombre',),
                'verbose_name': 'Zona',
                'verbose_name_plural': 'Zonas',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='producto',
            name='direccion',
            field=models.ForeignKey(to='main.Direccion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='producto',
            name='herramienta',
            field=models.OneToOneField(to='main.Herramienta'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ForeignKey(to='main.ImagenInicial'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pago',
            name='producto',
            field=models.ForeignKey(to='main.Producto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pago',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='imagenproducto',
            name='Producto',
            field=models.ForeignKey(related_name=b'imagenes', to='main.Producto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='herramienta',
            name='marca',
            field=models.ForeignKey(to='main.Marca'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='herramienta',
            name='modelo',
            field=models.ForeignKey(to='main.Modelo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='direccion',
            name='estado',
            field=models.ForeignKey(to='main.Estado'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='direccion',
            name='zona',
            field=models.ForeignKey(to='main.Zona'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ciudad',
            name='estado',
            field=models.ForeignKey(to='main.Estado'),
            preserve_default=True,
        ),
    ]

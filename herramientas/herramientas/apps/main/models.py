# -*- coding: utf-8 -*-
from django.utils.translation import gettext as _
import datetime
from django.db import models

#Rango de anos a utilizar en las herramientas
anos = []
for n in range(1960, (datetime.datetime.now().year+1)):
    anos.append((n,n))

#Modelos de la base de datos de Alquiherramientas 2112

#Estados del pais
class Estado(models.Model):
	nombre = models.CharField(max_length=30)

	class Meta:
		ordering = ('nombre',)
		verbose_name = "Estado"
		verbose_name_plural = "Estados"

	def __unicode__(self):
		return u"%s" %(self.nombre)


#Ciudaddes de las maquinarias
class Ciudad(models.Model):
	nombre = models.CharField(max_length=30)

	#Claves foraneas
	estado = models.ForeignKey(Estado)

	class Meta:
		ordering = ('nombre',)
		verbose_name = "Ciudad"
		verbose_name_plural = "Ciudades"

	def __unicode__(self):
		return u"%s" %(self.nombre)


#Zonas de las ciudades
class Zona(models.Model):
	nombre = models.CharField(max_length=30)

	#Claves foraneas
	ciudad = models.ForeignKey(Ciudad)

	class Meta:
		ordering = ('nombre',)
		verbose_name = "Zona"
		verbose_name_plural = "Zonas"

	def __unicode__(self):
		return u"%s" %(self.nombre)


#Direcciones de las herramientas publicadas
class Direccion(models.Model):
	domicilio = models.CharField(max_length=100)

	#Claves foraneas
	estado = models.ForeignKey(Estado)
	ciudad = models.ForeignKey(Ciudad)
	zona = models.ForeignKey(Zona)

	class Meta:
		ordering = ('domicilio',)
		verbose_name = "Direccion"
		verbose_name_plural = "Direcciones"

	def __unicode__(self):
		return u"%s" %(self.domicilio)


#Imagen de los anuncios que se publican
class Imagen(models.Model):
    imagen = models.ImageField(upload_to='uploads/img/', null=True)
    thumbnail = models.ImageField(upload_to='uploads/img/thumbnails/', blank=True, null=True, editable=False)
    descripcion = models.CharField(max_length=140, null=True)

    #Metodo para crear el thumbnail al momento de cear la imagen
    def create_thumbnail(self):
        # If there is no image associated with this.
        # do not create thumbnail
        if not self.imagen:
            return

        from PIL import Image
        from cStringIO import StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile
        import os

        # Set our max thumbnail size in a tuple (max width, max height)
        THUMBNAIL_SIZE = (200, 200)

        # Open original photo which we want to thumbnail using PIL's Image
        imagen = Image.open(StringIO(self.imagen.read()))
        image_type = imagen.format.lower()

        imagen.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        # Save the thumbnail
        temp_handle = StringIO()
        imagen.save(temp_handle, image_type)
        temp_handle.seek(0)

        # Save image to a SimpleUploadedFile which can be saved into
        # ImageField
        suf = SimpleUploadedFile(os.path.split(self.imagen.name)[-1], temp_handle.read(),
                                 content_type='imagen/%s' % (image_type))
        # Save SimpleUploadedFile into image field
        self.thumbnail.save('%s_thumbnail.%s' %
                            (os.path.splitext(suf.name)[0], image_type), suf, save=False)

    def save(self):
        # create a thumbnail
        self.create_thumbnail()

        super(Imagen, self).save()

    class Meta:
        abstract = True
        ordering = ('imagen',)
        verbose_name = _('Imagen')
        verbose_name_plural = _('Imagenes')

    def __unicode__(self):
        return self.descripcion


#Categoria de cada herramienta
class Categoria(models.Model):
	nombre = models.CharField(max_length=50)

	class Meta:
		verbose_name = "Categoria"
		verbose_name_plural = "Categorias"

	def __unicode__(self):
		return u"%s" %(self.nombre)


#Marca de la herramienta
class Marca(models.Model):
	nombre = models.CharField(max_length=30)

	class Meta:
		ordering = ('nombre',)
		verbose_name = "Marca"
		verbose_name_plural = "Marcas"

	def __unicode__(self):
		return u"%s" %(self.nombre)


#Modelo de cada herramienta
class Modelo(models.Model):
	nombre = models.CharField(max_length=30)

	#Claves foraneas
	marca = models.ForeignKey(Marca)

	class Meta:
		ordering = ('nombre',)
		verbose_name = "Modelo"
		verbose_name_plural = "Modelos"

	def __unicode__(self):
		return u"%s" %(self.nombre)


#Herramienta que se vende o alquila
class Herramienta(models.Model):

	nombre = models.CharField(max_length=30)
	ano = models.IntegerField(default=datetime.datetime.now().year, choices=anos, max_length=4)

	#Claves foraneas
	categoria = models.ForeignKey(Categoria)
	marca = models.ForeignKey(Marca)
	modelo = models.ForeignKey(Modelo)

	class Meta:
		ordering = ('nombre',)
		verbose_name = "Herramienta"
		verbose_name_plural = "Herramientas"

	def __unicode__(self):
		return u"%s" %(self.nombre)


# Publicacion de las herramientas.
class Publicacion(models.Model):
	titulo = models.CharField(max_length=100)
	contenido = models.CharField(max_length=10000)
	imagen = models.ImageField(upload_to='uploads/publicaciones')
	oferta = models.BooleanField(default=False, help_text='Marcado si desea que se muestre como una oferta')
	fecha_publicacion = models.DateTimeField(auto_now_add=True)
	fecha_actualizacion = models.DateTimeField(auto_now=True)
	fecha_expiracion = models.DateTimeField()

	#Claves foraneas
	direccion = models.ForeignKey(Direccion)
	herramienta = models.OneToOneField(Herramienta)


	class Meta:
		ordering = ('titulo',)
		verbose_name = "Publicacion"
		verbose_name_plural = "Publicaciones"

	def __unicode__(self):
		return u"%s" %(self.titulo)


#Imagenes de las publicaciones
class ImagenPublicacion(Imagen):
    publicacion = models.ForeignKey(Publicacion, related_name='imagenes')

    class Meta:
    	abstract = False
        verbose_name = "ImagenPublicacion"
        verbose_name_plural = "ImagenesPublicaciones"

    def __unicode__(self):
        return u"%s" %(self.descripcion)


#Clase de alquiler de herramienta que hereda de la publicacion
class Alquiler(Publicacion):
	dias = models.IntegerField()
	# Dos numeros decimales.
	precio = models.DecimalField(max_digits=20,decimal_places=2)

	class Meta:
		ordering = ('dias',)
		verbose_name = "Alquiler"
		verbose_name_plural = "Alquileres"


#Clase de venta de herramienta que hereda de la publicacion
class Venta(Publicacion):
	# Dos numeros decimales.
	precio = models.DecimalField(max_digits=20, decimal_places=2)

	class Meta:
		ordering = ('precio',)
		verbose_name = "Venta"
		verbose_name_plural = "Ventas"
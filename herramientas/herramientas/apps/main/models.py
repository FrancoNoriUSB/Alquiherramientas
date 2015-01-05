# -*- coding: utf-8 -*-
from django.utils.translation import gettext as _
from django.db import models

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
	imagen = models.ImageField()
	contenido = models.CharField(max_length=10000)
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


#Clase de alquiler de herramienta que hereda de la publicacion
class Alquiler(Publicacion):
	diasAlquiler = models.IntegerField()
	# Dos numeros decimales.
	precioDia = models.DecimalField(max_digits=20,decimal_places=2)

	class Meta:
		ordering = ('diasAlquiler',)
		verbose_name = "Alquiler"
		verbose_name_plural = "Alquileres"


#Clase de compra de herramienta que hereda de la publicacion
class Compra(Publicacion):
	# Dos numeros decimales.
	precio = models.DecimalField(max_digits=20, decimal_places=2)

	class Meta:
		ordering = ('precio',)
		verbose_name = "Compra"
		verbose_name_plural = "Compras"
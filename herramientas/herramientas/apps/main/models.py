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


#Marca de la herramienta
class Marca(models.Model):
	nombre = models.CharField(max_length=30)

	class Meta:
		ordering = ('nombre',)
		verbose_name = "Marca"
		verbose_name_plural = "Marcas"

	def __unicode__(self):
		return u"%s" %(self.marca)


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

	#Claves foraneas
	direccion = models.ForeignKey(Direccion)
	herramienta = models.OneToOneField(Herramienta)

	class Meta:
		abstract = True
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

	class Meta(Publicacion.Meta):
		abstract = False
		ordering = ('diasAlquiler',)
		verbose_name = "Alquiler"
		verbose_name_plural = "Alquileres"


#Clase de compra de herramienta que hereda de la publicacion
class Compra(Publicacion):
	# Dos numeros decimales.
	precio = models.DecimalField(max_digits=20, decimal_places=2)

	class Meta(Publicacion.Meta):
		abstract = False
		ordering = ('precio',)
		verbose_name = "Compra"
		verbose_name_plural = "Compras"
from django.db import models


# Herramienta.
class Herramienta(models.Model):
	nombre = models.CharField()
	marca = models.OneToOneField(Marca)
	direccion = models.OneToOneField(Direccion)


# Datos de las herramientas: marca, modelo y direccion.
class Marca(models.Model):
	marca = models.CharField()
	modelo = mdoels.OneToOneField(Modelo)


class Modelo(models.Model):
	modelo = models.CharField()


class Direccion(models.Model):
	estado = models.OneToOneField(Estado)
	ciudad = models.OneToOneField(Ciudad)
	zona = models.OneToOneField(Zona)


class Estado(models.Model):
	estado = models.CharField()


class Ciudad(models.Model):
	ciudad = models.CharField()


class Zona(models.Model):
	zona = models.CharField()


# Publicacion y sus hijos.
class Publicacion(models.Model):
	titulo = models.CharField()
	contenido = models.CharField()

	class Meta:
		abstract = True


class Alquiler(Publicacion):
	diasAlquiler = models.IntegerField()
	# Dos numeros decimales.
	precioDia = models.DecimalField(decimal_places=2)


class Compra(Publicacion):
	# Dos numeros decimales.
	precio = models.DecimalField(decimal_places=2)
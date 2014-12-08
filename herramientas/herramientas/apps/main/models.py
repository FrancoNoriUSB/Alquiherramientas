from django.db import models


# Datos de las herramientas: marca, modelo y direccion.
class Estado(models.Model):
	estado = models.CharField(max_length=30)


class Ciudad(models.Model):
	ciudad = models.CharField(max_length=30)


class Zona(models.Model):
	zona = models.CharField(max_length=30)


class Direccion(models.Model):
	estado = models.OneToOneField(Estado)
	ciudad = models.OneToOneField(Ciudad)
	zona = models.OneToOneField(Zona)


class Modelo(models.Model):
	modelo = models.CharField(max_length=30)


class Marca(models.Model):
	marca = models.CharField(max_length=30)
	modelo = models.OneToOneField(Modelo)


# Herramienta.
class Herramienta(models.Model):
	nombre = models.CharField(max_length=30)
	marca = models.OneToOneField(Marca)
	direccion = models.OneToOneField(Direccion)


# Publicacion y sus hijos.
class Publicacion(models.Model):
	titulo = models.CharField(max_length=100)
	contenido = models.CharField(max_length=10000)

	class Meta:
		abstract = True


class Alquiler(Publicacion):
	diasAlquiler = models.IntegerField()
	# Dos numeros decimales.
	precioDia = models.DecimalField(max_digits=20,decimal_places=2)


class Compra(Publicacion):
	# Dos numeros decimales.
	precio = models.DecimalField(max_digits=20, decimal_places=2)
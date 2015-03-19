# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


#Manager del modelo de usuario
class UserManager(BaseUserManager):
	def create_user(self, nombre, apellido, correo, telefono, password, ciudad, nacionalidad, cedula, afiliado):
		if not email:
			raise ValueError("Por favor ingrese un correo válido.")

		user = self.model(
			email = self.normalize_email(correo),
			nombre = nombre,
			apellido = apellido,
			telefono = telefono,
			ciudad = ciudad,
			nacionalidad = nacionalidad,
			cedula = cedula,
			is_afiliado = afiliado,
			)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, nombre, apellido, email, telefono, password, ciudad, nacionalidad, cedula):
		user = self.model(
			email = self.normalize_email(email),
			nombre = nombre,
			apellido = apellido,
			telefono = telefono,
			ciudad = ciudad,
			nacionalidad = nacionalidad,
			cedula = cedula,
			is_afiliado = True,
		)
		user.set_password(password)
		user.is_staff = True
		user.save()
		return user


# Definicion del usuario
class User(AbstractBaseUser):
	NAC = (
		('V', 'V'),
		('E', 'E'),
		)

	nombre = models.CharField(max_length=40)
	apellido = models.CharField(max_length=40)
	email = models.EmailField(unique=True)
	ciudad = models.CharField(max_length=40)
	telefono = models.IntegerField(max_length=20)
	nacionalidad = models.CharField(max_length=1, choices=NAC, default='V')
	cedula = models.IntegerField(max_length=10)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_afiliado = models.BooleanField(default=False, blank=True)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ['nombre', 'apellido', 'password', 'telefono',
						'ciudad', 'nacionalidad', 'cedula']

	objects = UserManager()

	def get_full_name(self):
		return self.email


	def get_short_name(self):
		return self.email


	def __str__(self):
		return self.email

	def has_perm(self, obj=None):
		return self.is_staff

	def has_module_perms(self, package):
		return self.is_staff


#Modelo para los banners de la aplicacion
class Banner(models.Model):

	nombre = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to='slide-home/')
	url = models.CharField(max_length=200)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Banner"
		verbose_name_plural = "Banners"

	def __unicode__(self):
		return u"%s" %(self.nombre)


#Modelo para las clausulas
class Clausula(models.Model):

	nombre = models.CharField(max_length=100)
	archivo = models.FileField(upload_to='uploads/archivos/')
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name='Clausula'
		verbose_name_plural = 'Clausulas'

	def __unicode__(self):
		return u"%s" %(self.nombre)

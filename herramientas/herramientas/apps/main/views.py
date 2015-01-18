# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from datetime import datetime, date
from django.db.models import Count
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_countries import countries
from random import randint
from funciones import *
from models import *
from forms import *
from herramientas.apps.administrador.forms import *

#Vista del inicio
def inicio(request):

	#Formulario de busqueda
	busquedaF = BusquedaForm()
	# formulario de nuevo usuario
	usuarioF = UserCreationForm()

	# Ofertas de los productos
	ofertas = []
	ofertas = Producto.objects.filter(oferta=True).order_by('?')
	
	if len(ofertas) > 0:
		ofertas = ofertas[randint(0, len(ofertas)-1)]

	#productos que se ofertan
	productos = Producto.objects.all().order_by('fecha_producto')

	#Caso que se realizo una busqueda
	if request.GET:
		busquedaF = BusquedaForm(request.GET)
        
        #Caso para el buscador de herramientas
        if busquedaF.is_valid():
			tipo = busquedaF.cleaned_data['tipo']
			categoria = busquedaF.cleaned_data['categoria']
			marca = busquedaF.cleaned_data['marca']
			estado = busquedaF.cleaned_data['estado']
			ciudad = busquedaF.cleaned_data['ciudad']
			zona = busquedaF.cleaned_data['zona']

			#Verificacion de campos
			if tipo != '' or categoria != None or marca != None or estado != None or ciudad != None or zona != None:

				#Verificacion de string vacio
				if tipo == '':
				    tipo = None

				#Campos a buscar
				fields_list = []
				fields_list.append('herramienta')
				fields_list.append('herramienta')
				fields_list.append('direccion')
				fields_list.append('direccion')
				fields_list.append('direccion')

				#Comparadores para buscar
				types_list=[]
				types_list.append('categoria__nombre__exact')
				types_list.append('marca__nombre__exact')
				types_list.append('estado__nombre__exact')
				types_list.append('ciudad__nombre__exact')
				types_list.append('zona__nombre__exact')

				#Valores a buscar
				values_list=[]
				values_list.append(categoria)
				values_list.append(marca)
				values_list.append(estado)
				values_list.append(ciudad)
				values_list.append(zona)

				operator = 'and'

				productos = dynamic_query(Producto, fields_list, types_list, values_list, operator)
				
				if tipo == 'alquiler':
					fields_list.append('alquiler')
				else:
					fields_list.append('venta')

				#Caso no encontro nada
				if productos == []:
					productos = Producto.objects.all().order_by('fecha_producto')

	#Busqueda de propiedades en el pais actual
	paginator = Paginator(productos, 6)
	page = request.GET.get('page')

	try:
		productos = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		productos = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		productos = paginator.page(paginator.num_pages)

	# Creando un nuevo usuario
	if request.method=='POST':
		usuarioF = UserCreationForm(request.POST)
		if usuarioF.is_valid():
			usuarioF.save()
			return HttpResponseRedirect('/')

	ctx = {
		'BusquedaForm':busquedaF,
		'ofertas':ofertas,
		'productos':productos,
		'UsuarioForm':usuarioF,
	}

	return render_to_response('main/inicio/inicio.html', ctx, context_instance=RequestContext(request))


# Vista de la informacion de la empresa
def empresa(request):

	#Formulario de busqueda
	busquedaF = BusquedaForm()
	# Formulario de nuevo usuario
	usuarioF = UserCreationForm()	

	# Ofertas de los productos
	ofertas = []
	ofertas = Producto.objects.filter(oferta=True).order_by('?')
	
	if len(ofertas) > 0:
		ofertas = ofertas[randint(0, len(ofertas)-1)]

	# Creando un nuevo usuario
	if request.method=='POST':
		usuarioF = UserCreationForm(request.POST)
		if usuarioF.is_valid():
			usuarioF.save()
			return HttpResponseRedirect('/')

	ctx = {
		'BusquedaForm':busquedaF,
		'ofertas':ofertas,
		'UsuarioForm':usuarioF,
	}

	return render_to_response('main/empresa/empresa.html', ctx, context_instance=RequestContext(request))


# Vista de los productos
def productos(request):

	#Formulario de busqueda
	busquedaF = BusquedaForm()
	# Formulario de nuevo usuario
	usuarioF = UserCreationForm()

	# Ofertas de los productos
	ofertas = []
	ofertas = Producto.objects.filter(oferta=True).order_by('?')
	
	if len(ofertas) > 0:
		ofertas = ofertas[randint(0, len(ofertas)-1)]

	#productos que se ofertan
	productos = Producto.objects.all().order_by('fecha_producto')

	# Creando un nuevo usuario
	if request.method=='POST':
		usuarioF = UserCreationForm(request.POST)
		if usuarioF.is_valid():
			usuarioF.save()
			return HttpResponseRedirect('/')

	ctx = {
		'BusquedaForm':busquedaF,
		'ofertas':ofertas,
		'productos':productos,
		'UsuarioForm':usuarioF,
	}

	return render_to_response('main/productos/productos.html', ctx, context_instance=RequestContext(request))


# Vista de un producto especifico
def producto(request, id_producto):

	#Formulario de busqueda
	busquedaF = BusquedaForm()
	# Formulario de nuevo usuario
	usuarioF = UserCreationForm()

	# Ofertas de los productos
	ofertas = []
	ofertas = Producto.objects.filter(oferta=True).order_by('?')
	
	if len(ofertas) > 0:
		ofertas = ofertas[randint(0, len(ofertas)-1)]

	producto = Producto.objects.get(id=id_producto)

	# Creando un nuevo usuario
	if request.method=='POST':
		usuarioF = UserCreationForm(request.POST)
		if usuarioF.is_valid():
			usuarioF.save()
			return HttpResponseRedirect('/')

	ctx = {
		'BusquedaForm':busquedaF,
		'ofertas':ofertas,
		'producto': producto,
		'UsuarioForm':usuarioF,
	}

	return render_to_response('main/productos/producto.html', ctx, context_instance=RequestContext(request))


# Vista para la afiliacion
def afiliacion(request):

	#Formulario de busqueda
	busquedaF = BusquedaForm()
	# Formulario de nuevo usuario
	usuarioF = UserCreationForm()

	# Ofertas de los productos
	ofertas = []
	ofertas = Producto.objects.filter(oferta=True).order_by('?')
	
	if len(ofertas) > 0:
		ofertas = ofertas[randint(0, len(ofertas)-1)]

	# Creando un nuevo usuario
	if request.method=='POST':
		usuarioF = UserCreationForm(request.POST)
		if usuarioF.is_valid():
			usuarioF.save()
			return HttpResponseRedirect('/')

	ctx = {
		'BusquedaForm':busquedaF,
		'ofertas':ofertas,
		'UsuarioForm':usuarioF,
	}

	return render_to_response('main/afiliacion/afiliacion.html', ctx, context_instance=RequestContext(request))


# Vista de contactos
def contactos(request):

	#Formulario de busqueda
	busquedaF = BusquedaForm()
	# Formulario de nuevo usuario
	usuarioF = UserCreationForm()

	#Formulario de contacto
	if request.method == 'POST':
		contactoF = ContactoForm(request.POST)
		if contactoF.is_valid():
			titulo = "Mensaje de: "+contactoF.cleaned_data['remitente']
			mensaje = contactoF.cleaned_data['mensaje']
			correo = EmailMessage(titulo, mensaje, to=['valderrama_862@hotmail.com'])
			correo.send()
			return HttpResponseRedirect('/contactos/')
	else:
		contactoF = ContactoForm()

	# Ofertas de los productos
	ofertas = []
	ofertas = Producto.objects.filter(oferta=True).order_by('?')
	
	if len(ofertas) > 0:
		ofertas = ofertas[randint(0, len(ofertas)-1)]

	# Creando un nuevo usuario
	if request.method=='POST':
		usuarioF = UserCreationForm(request.POST)
		if usuarioF.is_valid():
			usuarioF.save()
			return HttpResponseRedirect('/')

	ctx = {
		'BusquedaForm':busquedaF,
		'ofertas':ofertas,
		'ContactoForm': contactoF,
		'UsuarioForm':usuarioF,
	}

	return render_to_response('main/contactos/contactos.html', ctx, context_instance=RequestContext(request))
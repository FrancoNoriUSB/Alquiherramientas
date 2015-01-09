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
from models import *
from forms import *
from django.core.mail.message import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_countries import countries
from random import randint

#Vista del inicio
def inicio(request):

	#Formulario de busqueda
	busquedaF = BusquedaForm()

	# Ofertas de los publicaciones
	ofertas = []
	ofertas = Publicacion.objects.filter(oferta=True).order_by('?')
	
	if len(ofertas) > 0:
		ofertas = ofertas[randint(0, len(ofertas)-1)]

	ctx = {
		'BusquedaForm':busquedaF,
		'ofertas':ofertas,
	}

	return render_to_response('main/inicio/inicio.html', ctx, context_instance=RequestContext(request))


# Vista de la informacion de la empresa
def empresa(request):

	#Formulario de busqueda
	busquedaF = BusquedaForm()

	# Ofertas de los publicaciones
	ofertas = []
	ofertas = Publicacion.objects.filter(oferta=True).order_by('?')
	
	if len(ofertas) > 0:
		ofertas = ofertas[randint(0, len(ofertas)-1)]

	ctx = {
		'BusquedaForm':busquedaF,
		'ofertas':ofertas,
	}

	return render_to_response('main/empresa/empresa.html', ctx, context_instance=RequestContext(request))


# Vista de los publicaciones
def publicaciones(request):

	#Formulario de busqueda
	busquedaF = BusquedaForm()

	# Ofertas de los publicaciones
	ofertas = []
	ofertas = Publicacion.objects.filter(oferta=True).order_by('?')
	
	if len(ofertas) > 0:
		ofertas = ofertas[randint(0, len(ofertas)-1)]

	#publicaciones que se ofertan
	publicaciones = Publicacion.objects.all().order_by('fecha_publicacion')

	ctx = {
		'BusquedaForm':busquedaF,
		'ofertas':ofertas,
		'publicaciones':publicaciones,
	}

	return render_to_response('main/publicaciones/publicaciones.html', ctx, context_instance=RequestContext(request))


# Vista de un producto especifico
def producto(request, id_producto):

	#Formulario de busqueda
	busquedaF = BusquedaForm()

	# Ofertas de los publicaciones
	ofertas = []
	ofertas = Publicacion.objects.filter(oferta=True).order_by('?')
	
	if len(ofertas) > 0:
		ofertas = ofertas[randint(0, len(ofertas)-1)]

	producto = Publicacion.objects.get(id=id_producto)

	ctx = {
		'BusquedaForm':busquedaF,
		'ofertas':ofertas,
		'producto': producto
	}

	return render_to_response('main/publicaciones/publicacion.html', ctx, context_instance=RequestContext(request))


# Vista para la afiliacion
def afiliacion(request):

	#Formulario de busqueda
	busquedaF = BusquedaForm()

	# Ofertas de los publicaciones
	ofertas = []
	ofertas = Publicacion.objects.filter(oferta=True).order_by('?')
	
	if len(ofertas) > 0:
		ofertas = ofertas[randint(0, len(ofertas)-1)]

	ctx = {
		'BusquedaForm':busquedaF,
		'ofertas':ofertas,
	}

	return render_to_response('main/afiliacion/afiliacion.html', ctx, context_instance=RequestContext(request))


# Vista de contactos
def contactos(request):

	#Formulario de busqueda
	busquedaF = BusquedaForm()

	#Formulario de contacto
	if request.method == 'POST':
		contactoF = ContactoForm(request.POST)
		if contactoF.is_valid:
			titulo = "Mensaje de: "+contactoF.cleaned_data['remitente']
			mensaje = contactoF.cleaned_data['mensaje']
			correo = EmailMessage(titulo, mensaje, to=['evalderrama862@gmail.com'])
			print("Envio")
			correo.send
			return HttpResponseRedirect('/contactos/')
	else:
		contactoF = ContactoForm()

	# Ofertas de los publicaciones
	ofertas = []
	ofertas = Publicacion.objects.filter(oferta=True).order_by('?')
	
	if len(ofertas) > 0:
		ofertas = ofertas[randint(0, len(ofertas)-1)]

	ctx = {
		'BusquedaForm':busquedaF,
		'ofertas':ofertas,
		'ContactoForm': contactoF,
	}

	return render_to_response('main/contactos/contactos.html', ctx, context_instance=RequestContext(request))
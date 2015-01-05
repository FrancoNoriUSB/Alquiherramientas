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
from itertools import chain


#Vista del inicio
def inicio(request):

	# Ofertas de los productos
	oferta = []
	oferta_alquiler = Alquiler.objects.filter(oferta=True).order_by('?')
	oferta_venta = Compra.objects.filter(oferta=True).order_by('?')
	oferta = list(chain(oferta_alquiler, oferta_venta))
	
	if len(oferta) > 0:
		oferta = oferta[randint(0, len(oferta)-1)]

	ctx = {
		'oferta':oferta,
	}

	return render_to_response('main/inicio/inicio.html', ctx, context_instance=RequestContext(request))


# Vista de la informacion de la empresa
def empresa(request):

	# Ofertas de los productos
	oferta = []
	oferta_alquiler = Alquiler.objects.filter(oferta=True).order_by('?')
	oferta_venta = Compra.objects.filter(oferta=True).order_by('?')
	oferta = list(chain(oferta_alquiler, oferta_venta))
	
	if len(oferta) > 0:
		oferta = oferta[randint(0, len(oferta)-1)]

	ctx = {
		'oferta':oferta,
	}

	return render_to_response('main/empresa/empresa.html', ctx, context_instance=RequestContext(request))


# Vista de los productos
def productos(request):

	# Ofertas de los productos
	oferta = []
	oferta_alquiler = Alquiler.objects.filter(oferta=True).order_by('?')
	oferta_venta = Compra.objects.filter(oferta=True).order_by('?')
	oferta = list(chain(oferta_alquiler, oferta_venta))
	
	if len(oferta) > 0:
		oferta = oferta[randint(0, len(oferta)-1)]

	compra = Compra.objects.all().order_by('fecha_publicacion')
	alquileres = Alquiler.objects.all().order_by('fecha_publicacion')

	ctx = {
		'oferta': oferta,
		'productos':productos,
	}

	return render_to_response('main/productos/productos.html', ctx, context_instance=RequestContext(request))


# Vista de un producto especifico
def producto(request, id_producto):
	producto = Publicacion.objects.get(id=id_producto)

	ctx = {
		'producto': producto
	}

	return render_to_response('main/productos/producto.html', ctx, context_instance=RequestContext(request))


# Vista para la afiliacion
def afiliacion(request):

	# Ofertas de los productos
	oferta = []
	oferta_alquiler = Alquiler.objects.filter(oferta=True).order_by('?')
	oferta_venta = Compra.objects.filter(oferta=True).order_by('?')
	oferta = list(chain(oferta_alquiler, oferta_venta))
	
	if len(oferta) > 0:
		oferta = oferta[randint(0, len(oferta)-1)]

	ctx = {
		'oferta':oferta,
	}

	return render_to_response('main/afiliacion/afiliacion.html', ctx, context_instance=RequestContext(request))


# Vista de contactos
def contactos(request):

	# Ofertas de los productos
	oferta = []
	oferta_alquiler = Alquiler.objects.filter(oferta=True).order_by('?')
	oferta_venta = Compra.objects.filter(oferta=True).order_by('?')
	oferta = list(chain(oferta_alquiler, oferta_venta))
	
	if len(oferta) > 0:
		oferta = oferta[randint(0, len(oferta)-1)]

	ctx = {
		'oferta':oferta,
	}

	return render_to_response('main/contactos/contactos.html', ctx, context_instance=RequestContext(request))


def ultimasPublicaciones(request):
	publicaciones = Publicacion.objects.all().order_by("-fecha_publicacion")

	ctx = {
		'publicaciones':publicaciones,
	}

	return render_to_response('main/inicio/inicio.html', ctx, context_instance=RequestContext(request))
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
from models import *
from herramientas.apps.administrador.forms import *
from herramientas.apps.main.models import *
import json


#Vista de login de user administrador
def login_admin(request):

	loginF = LoginForm()
	email = ''
	password = ''

	if request.POST:
		loginF = LoginForm(request.POST)
		if request.user.is_authenticated() and request.user and request.user.is_staff:
			return HttpResponseRedirect('/administrador/')
		else:
			email = request.POST['email']
			password = request.POST['password']
			usuario = authenticate(email=email, password=password, is_staff=True)
			if usuario:
					# Caso del usuario activo
					if usuario.is_active:
						login(request, usuario)
						return HttpResponseRedirect('/administrador/')
					else:
						return "Tu cuenta esta bloqueada"
			else:
				# Usuario invalido o no existe!
				print "Invalid login details: {0}, {1}".format(email, password)

		return HttpResponseRedirect('/administrador/')

	ctx={
		'LoginForm':loginF,
	}

	return render_to_response('administrador/login/login.html', ctx, context_instance=RequestContext(request))


#Vista del inicio
@login_required(login_url='/administrador/login/')
def inicio(request):

	ctx={

	}

	return render_to_response('administrador/inicio/inicio.html', ctx, context_instance=RequestContext(request))


#Vista de la empresa en el admin
@login_required(login_url='/administrador/login/')
def empresa_admin(request):

	editado = ''
	empresa = get_object_or_404(Empresa, id=1)
	empresaF = EmpresaForm(instance=empresa)

	if request.POST:
		empresaF = EmpresaForm(request.POST, instance=empresa)
		if empresaF.is_valid():
			empresaF.save()
			editado = True

	empresaF = EmpresaForm(instance=empresa)

	ctx={
		'EmpresaForm':empresaF,
		'editado':editado,
	}

	return render_to_response('administrador/empresa/empresa.html', ctx, context_instance=RequestContext(request))


#Vista de agregar producto de venta en el admin
@login_required(login_url='/administrador/login/')
def venta_agregar(request):

	editado = ''
	ventaF = VentaForm()
	herramientaF = HerramientaForm()
	direccionF = DireccionForm()

	if request.POST:
		ventaF = VentaForm(request.POST, request.FILES)
		herramientaF = HerramientaForm(request.POST)
		direccionF = DireccionForm(request.POST)
		if ventaF.is_valid() and herramientaF.is_valid() and direccionF.is_valid():
			print "SI SI SI"
			venta = ventaF.save(commit=False)
			herramienta = herramientaF.save()
			direccion = direccionF.save()
			venta.herramienta = herramienta
			venta.direccion = direccion
			venta.save()
			editado = True


	ctx={
		'VentaForm':ventaF,
		'HerramientaForm':herramientaF,
		'DireccionForm':direccionF,
		'editado':editado,
	}

	return render_to_response('administrador/venta/agregar.html', ctx, context_instance=RequestContext(request))


#Vista de editar producto de venta en el admin
@login_required(login_url='/administrador/login/')
def venta_editar(request, id_producto):

	ctx={

	}

	return render_to_response('administrador/venta/editar.html', ctx, context_instance=RequestContext(request))



#Vista de listar productos de venta en el admin
@login_required(login_url='/administrador/login/')
def venta_listar(request):

	ctx={

	}

	return render_to_response('administrador/venta/ventas.html', ctx, context_instance=RequestContext(request))


#Vista de agregar producto de alquiler en el admin
@login_required(login_url='/administrador/login/')
def alquiler_agregar(request):

	ctx={

	}

	return render_to_response('administrador/alquiler/agregar.html', ctx, context_instance=RequestContext(request))


#Vista de editar producto de alquiler en el admin
@login_required(login_url='/administrador/login/')
def alquiler_editar(request, id_producto):

	ctx={

	}

	return render_to_response('administrador/alquiler/editar.html', ctx, context_instance=RequestContext(request))


#Vista de listar productos de alquiler en el admin
@login_required(login_url='/administrador/login/')
def alquiler_listar(request):

	ctx={

	}

	return render_to_response('administrador/alquiler/alquileres.html', ctx, context_instance=RequestContext(request))


#Vista de afiliaciones en el admin
@login_required(login_url='/administrador/login/')
def afiliacion_admin(request):

	ctx={

	}

	return render_to_response('administrador/afiliacion/afiliacion.html', ctx, context_instance=RequestContext(request))


#Vista de contactos en el admin
@login_required(login_url='/administrador/login/')
def contactos_admin(request):

	ctx={

	}

	return render_to_response('administrador/contactos/contactos.html', ctx, context_instance=RequestContext(request))


#Vista de la empresa en el admin
@login_required(login_url='/administrador/login/')
def banners_admin(request):

	ctx={

	}

	return render_to_response('administrador/banners/banners.html', ctx, context_instance=RequestContext(request))


#Vista de la empresa en el admin
@login_required(login_url='/administrador/login/')
def usuarios_admin(request):

	ctx={

	}

	return render_to_response('administrador/usuarios/usuarios.html', ctx, context_instance=RequestContext(request))


#Vista de la empresa en el admin
@login_required(login_url='/administrador/login/')
def configuracion_admin(request):

	ctx={

	}

	return render_to_response('administrador/configuracion/configuracion.html', ctx, context_instance=RequestContext(request))



#Vista para cerrar la sesion
@login_required
def logout_admin(request):

    logout(request)
    return HttpResponseRedirect('/administrador/')
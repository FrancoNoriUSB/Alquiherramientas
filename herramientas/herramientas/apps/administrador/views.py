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
from forms import *
from herramientas.apps.main.models import *
from herramientas.apps.administrador.forms import *
import json


#Vista de login de user administrador
def login_admin(request):

	loginF = LoginForm()

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

	return ''


#Vista de agregar producto de venta en el admin
@login_required(login_url='/administrador/login/')
def venta_agregar(request):

	return ''

#Vista de editar producto de venta en el admin
@login_required(login_url='/administrador/login/')
def venta_editar(request, id_producto):

	return ''


#Vista de listar productos de venta en el admin
@login_required(login_url='/administrador/login/')
def venta_listar(request):

	return ''


#Vista de agregar producto de alquiler en el admin
@login_required(login_url='/administrador/login/')
def alquiler_agregar(request):

	return ''

#Vista de editar producto de alquiler en el admin
@login_required(login_url='/administrador/login/')
def alquiler_editar(request, id_producto):

	return ''


#Vista de listar productos de alquiler en el admin
@login_required(login_url='/administrador/login/')
def alquiler_listar(request):

	return ''


#Vista de afiliaciones en el admin
@login_required(login_url='/administrador/login/')
def afiliacion_admin(request):

	return ''


#Vista de contactos en el admin
@login_required(login_url='/administrador/login/')
def contactos_admin(request):

	return ''


#Vista de la empresa en el admin
@login_required(login_url='/administrador/login/')
def banners_admin(request):

	return ''


#Vista de la empresa en el admin
@login_required(login_url='/administrador/login/')
def usuarios_admin(request):

	return ''


#Vista de la empresa en el admin
@login_required(login_url='/administrador/login/')
def configuracion_admin(request):

	return ''
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
from django.forms.models import inlineformset_factory
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

		if herramientaF.is_valid() and direccionF.is_valid():
			herramienta = herramientaF.save(commit=False)
			direccion = direccionF.save(commit=False)
			if ventaF.is_valid():
				herramienta.save()
				direccion.save()
				venta = ventaF.save(commit=False)
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

	editado = ''
	venta = Venta.objects.get(id=id_producto)
	ventaF = VentaForm(instance=venta)
	herramientaF = HerramientaForm(instance=venta.herramienta)
	direccionF = DireccionForm(instance=venta.direccion)

	if request.POST:
		ventaF = VentaForm(request.POST, request.FILES, instance=venta)
		herramientaF = HerramientaForm(request.POST, instance=venta.herramienta)
		direccionF = DireccionForm(request.POST, instance=venta.direccion)

		if herramientaF.is_valid() and direccionF.is_valid():
			herramienta = herramientaF.save(commit=False)
			direccion = direccionF.save(commit=False)
			if ventaF.is_valid():
				herramienta.save()
				direccion.save()
				venta = ventaF.save(commit=False)
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

	return render_to_response('administrador/venta/editar.html', ctx, context_instance=RequestContext(request))


#Vista de editar imagenes de producto de venta
@login_required(login_url='/administrador/login/')
def venta_imagen(request, id_producto):

	editado = ''
	venta = Venta.objects.get(id=id_producto)

	imagenes = ImagenProducto.objects.filter(Producto=venta)

	#Formset de imagen
	ImagenFormset = inlineformset_factory(Producto, ImagenProducto, form = ImagenProductoForm, can_delete=True, extra=1, max_num=len(imagenes)+2, fields=['imagen', 'descripcion'])
	ventaF = ImagenFormset(instance=venta, queryset=ImagenProducto.objects.filter(Producto=venta))

	if request.POST:
		ventaF = ImagenFormset(request.POST, request.FILES, instance=venta)
		if ventaF.is_valid():
			ventaF.save()

	ventaF = ImagenFormset(instance=venta, queryset=ImagenProducto.objects.filter(Producto=venta))
	
	ctx = {
		'Venta':venta,
		'VentaForm':ventaF,
		'editado':editado,
	}

	return render_to_response('administrador/venta/imagen.html', ctx, context_instance=RequestContext(request))


#Vista de listar productos de venta en el admin
@login_required(login_url='/administrador/login/')
def venta_listar(request):

	ventas = Venta.objects.all().order_by('id')

	paginator = Paginator(ventas, 10)
	page = request.GET.get('page')

	try:
		ventas = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		ventas = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		ventas = paginator.page(paginator.num_pages)

	ctx={
		'ventas':ventas,
	}

	return render_to_response('administrador/venta/listar.html', ctx, context_instance=RequestContext(request))


#Vista de agregar producto de alquiler en el admin
@login_required(login_url='/administrador/login/')
def alquiler_agregar(request):

	editado = ''
	alquilerF = AlquilerForm()
	herramientaF = HerramientaForm()
	direccionF = DireccionForm()

	if request.POST:
		alquilerF = AlquilerForm(request.POST, request.FILES)
		herramientaF = HerramientaForm(request.POST)
		direccionF = DireccionForm(request.POST)

		if herramientaF.is_valid() and direccionF.is_valid():
			herramienta = herramientaF.save(commit=False)
			direccion = direccionF.save(commit=False)
			if alquilerF.is_valid():
				herramienta.save()
				direccion.save()
				venta = alquilerF.save(commit=False)
				venta.herramienta = herramienta
				venta.direccion = direccion
				venta.save()
				editado = True

	ctx={
		'AlquilerForm':alquilerF,
		'HerramientaForm':herramientaF,
		'DireccionForm':direccionF,
		'editado':editado,
	}

	return render_to_response('administrador/alquiler/agregar.html', ctx, context_instance=RequestContext(request))


#Vista de editar producto de alquiler en el admin
@login_required(login_url='/administrador/login/')
def alquiler_editar(request, id_producto):

	editado = ''
	alquiler = Alquiler.objects.get(id=id_producto)
	alquilerF = AlquilerForm(instance=alquiler)
	herramientaF = HerramientaForm(instance=alquiler.herramienta)
	direccionF = DireccionForm(instance=alquiler.direccion)

	if request.POST:
		alquilerF = AlquilerForm(request.POST, request.FILES, instance=alquiler)
		herramientaF = HerramientaForm(request.POST, instance=alquiler.herramienta)
		direccionF = DireccionForm(request.POST, instance=alquiler.direccion)

		if herramientaF.is_valid() and direccionF.is_valid():
			herramienta = herramientaF.save(commit=False)
			direccion = direccionF.save(commit=False)
			if alquilerF.is_valid():
				herramienta.save()
				direccion.save()
				venta = alquilerF.save(commit=False)
				venta.herramienta = herramienta
				venta.direccion = direccion
				venta.save()
				editado = True

	ctx={
		'AlquilerForm':alquilerF,
		'HerramientaForm':herramientaF,
		'DireccionForm':direccionF,
		'editado':editado,
	}
	
	return render_to_response('administrador/alquiler/editar.html', ctx, context_instance=RequestContext(request))


#Vista de editar imagenes de producto de alquiler
@login_required(login_url='/administrador/login/')
def alquiler_imagen(request, id_producto):

	editado = ''
	alquiler = Alquiler.objects.get(id=id_producto)

	imagenes = ImagenProducto.objects.filter(Producto=alquiler)

	#Formset de imagen
	ImagenFormset = inlineformset_factory(Producto, ImagenProducto, form = ImagenProductoForm, can_delete=True, extra=1, max_num=len(imagenes)+2, fields=['imagen', 'descripcion'])
	alquilerF = ImagenFormset(instance=alquiler, queryset=ImagenProducto.objects.filter(Producto=alquiler))

	if request.POST:
		alquilerF = ImagenFormset(request.POST, request.FILES, instance=alquiler)
		if alquilerF.is_valid():
			alquilerF.save()

	alquilerF = ImagenFormset(instance=alquiler, queryset=ImagenProducto.objects.filter(Producto=alquiler))
	
	ctx = {
		'Alquiler':alquiler,
		'AlquilerForm':alquilerF,
		'editado':editado,
	}

	return render_to_response('administrador/alquiler/imagen.html', ctx, context_instance=RequestContext(request))


#Vista de listar productos de alquiler en el admin
@login_required(login_url='/administrador/login/')
def alquiler_listar(request):

	alquileres = Alquiler.objects.all().order_by('id')

	paginator = Paginator(alquileres, 10)
	page = request.GET.get('page')

	try:
		alquileres = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		alquileres = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		alquileres = paginator.page(paginator.num_pages)

	ctx={
		'alquileres':alquileres,
	}


	return render_to_response('administrador/alquiler/listar.html', ctx, context_instance=RequestContext(request))


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


#Vista de la empresa en el admin
@login_required(login_url='/administrador/login/')
def configuracion_admin(request):

	ctx={

	}

	return render_to_response('administrador/configuracion/configuracion.html', ctx, context_instance=RequestContext(request))


#Vista para agregar categorias
@login_required(login_url='/administrador/login/')
def categoria_agregar(request):

	editado = ''
	categoriaF = CategoriaForm()

	if request.POST:
		categoriaF = CategoriaForm(request.POST)
		if categoriaF.is_valid():
			categoriaF.save()
			editado = True

	ctx={
		'CategoriaForm':categoriaF,
		'editado':editado,
	}

	return render_to_response('administrador/categoria/agregar.html', ctx, context_instance=RequestContext(request))


#Vista para editar categorias
@login_required(login_url='/administrador/login/')
def categoria_editar(request, id_categoria):

	editado = ''
	categoria = get_object_or_404(Categoria, id=id_categoria)
	categoriaF = CategoriaForm(instance=categoria)

	if request.POST:
		categoriaF = CategoriaForm(request.POST, instance=categoria)
		if categoriaF.is_valid():
			categoriaF.save()
			editado = True

	ctx={
		'CategoriaForm':categoriaF,
		'editado':editado,
	}

	return render_to_response('administrador/categoria/editar.html', ctx, context_instance=RequestContext(request))


#Vista para listar categorias
@login_required(login_url='/administrador/login/')
def categoria_listar(request):

	categorias = Categoria.objects.all().order_by('id')

	ctx={
		"categorias":categorias,
	}

	return render_to_response('administrador/categoria/listar.html', ctx, context_instance=RequestContext(request))


#Vista para agregar marcas
@login_required(login_url='/administrador/login/')
def marca_agregar(request):

	editado = ''
	marcaF = MarcaForm()

	if request.POST:
		marcaF = MarcaForm(request.POST)
		if marcaF.is_valid():
			marcaF.save()
			editado = True


	ctx={
		'MarcaForm':marcaF,
		'editado':editado,
	}

	return render_to_response('administrador/marca/agregar.html', ctx, context_instance=RequestContext(request))


#Vista para editar marcas
@login_required(login_url='/administrador/login/')
def marca_editar(request, id_marca):

	editado = ''
	marca = get_object_or_404(marca, id=id_marca)
	marcaF = MarcaForm(instance=marca)

	if request.POST:
		marcaF = MarcaForm(request.POST,instance=marca)
		if marcaF.is_valid():
			marcaF.save()
			editado = True


	ctx={
		'MarcaForm':marcaF,
		'editado':editado,
	}

	return render_to_response('administrador/marca/editar.html', ctx, context_instance=RequestContext(request))


#Vista para listar marcas
@login_required(login_url='/administrador/login/')
def marca_listar(request):

	marcas = Marca.objects.all().order_by('id')

	ctx={
		"marcas":marcas,
	}

	return render_to_response('administrador/marca/listar.html', ctx, context_instance=RequestContext(request))


#Vista para agregar modelos
@login_required(login_url='/administrador/login/')
def modelo_agregar(request):

	editado = ''
	modeloF = ModeloForm()

	if request.POST:
		modeloF = ModeloForm(request.POST)
		if modeloF.is_valid():
			modeloF.save()
			editado = True

	ctx={
		'ModeloForm':modeloF,
		'editado':editado,
	}

	return render_to_response('administrador/modelo/agregar.html', ctx, context_instance=RequestContext(request))


#Vista para editar modelos
@login_required(login_url='/administrador/login/')
def modelo_editar(request, id_modelo):

	editado = ''
	modelo = get_object_or_404(Modelo, id=id_modelo)
	modeloF = ModeloForm(instance=modelo)

	if request.POST:
		modeloF = ModeloForm(request.POST,instance=modelo)
		if modeloF.is_valid():
			modeloF.save()
			editado = True

	ctx={
		'ModeloForm':modeloF,
		'editado':editado,
	}

	return render_to_response('administrador/modelo/editar.html', ctx, context_instance=RequestContext(request))


#Vista para listar modelos
@login_required(login_url='/administrador/login/')
def modelo_listar(request):

	modelos = Modelo.objects.all().order_by('id')

	ctx={
		"modelos":modelos,
	}

	return render_to_response('administrador/modelo/listar.html', ctx, context_instance=RequestContext(request))


#Vista para agregar estados
@login_required(login_url='/administrador/login/')
def estado_agregar(request):

	editado = ''
	estadoF = EstadoForm()

	if request.POST:
		estadoF = EstadoForm(request.POST)
		if estadoF.is_valid():
			estadoF.save()
			editado = True

	ctx={
		'EstadoForm':estadoF,
		'editado':editado,
	}

	return render_to_response('administrador/estado/agregar.html', ctx, context_instance=RequestContext(request))


#Vista para editar estados
@login_required(login_url='/administrador/login/')
def estado_editar(request, id_estado):

	editado = ''
	estado = get_object_or_404(Estado,id=id_estado)
	estadoF = EstadoForm(instance=estado)

	if request.POST:
		estadoF = EstadoForm(request.POST,instance=estado)
		if estadoF.is_valid():
			estadoF.save()
			editado = True

	ctx={
		'EstadoForm':estadoF,
		'editado':editado,
	}

	return render_to_response('administrador/estado/editar.html', ctx, context_instance=RequestContext(request))


#Vista para listar estados
@login_required(login_url='/administrador/login/')
def estado_listar(request):

	estados = Estado.objects.all().order_by('id')

	ctx={
		"estados":estados,
	}

	return render_to_response('administrador/estado/listar.html', ctx, context_instance=RequestContext(request))


#Vista para agregar ciudades
@login_required(login_url='/administrador/login/')
def ciudad_agregar(request):

	editado = ''
	ciudadF = CiudadForm()

	if request.POST:
		ciudadF = CiudadForm(request.POST)
		if ciudadF.is_valid():
			ciudadF.save()
			editado = True

	ctx={
		'CiudadForm':ciudadF,
		'editado':editado,
	}

	return render_to_response('administrador/ciudad/agregar.html', ctx, context_instance=RequestContext(request))


#Vista para editar ciudades
@login_required(login_url='/administrador/login/')
def ciudad_editar(request, id_ciudad):

	editado = ''
	ciudad = get_object_or_404(Ciudad,id=id_ciudad)
	ciudadF = CiudadForm(instance=ciudad)

	if request.POST:
		ciudadF = CiudadForm(request.POST,instance=ciudad)
		if ciudadF.is_valid():
			ciudadF.save()
			editado = True

	ctx={
		'CiudadForm':ciudadF,
		'editado':editado,
	}

	return render_to_response('administrador/ciudad/editar.html', ctx, context_instance=RequestContext(request))


#Vista para listar ciudades
@login_required(login_url='/administrador/login/')
def ciudad_listar(request):

	ciudades = Ciudad.objects.all().order_by('id')

	ctx={
		"ciudades":ciudades,
	}

	return render_to_response('administrador/ciudad/listar.html', ctx, context_instance=RequestContext(request))


#Vista para agregar zonas
@login_required(login_url='/administrador/login/')
def zona_agregar(request):

	editado = ''
	zonaF = ZonaForm()

	if request.POST:
		zonaF = ZonaForm(request.POST)
		if zonaF.is_valid():
			zonaF.save()
			editado = True

	ctx={
		'ZonaForm':zonaF,
		'editado':editado,
	}

	return render_to_response('administrador/zona/agregar.html', ctx, context_instance=RequestContext(request))


#Vista para editar zonas
@login_required(login_url='/administrador/login/')
def zona_editar(request, id_zona):

	editado = ''
	zona = get_object_or_404(Zona,id=id_zona)
	zonaF = ZonaForm(instance=zona)

	if request.POST:
		zonaF = ZonaForm(request.POST,instance=zona)
		if zonaF.is_valid():
			zonaF.save()
			editado = True

	ctx={
		'ZonaForm':zonaF,
		'editado':editado,
	}

	return render_to_response('administrador/zona/editar.html', ctx, context_instance=RequestContext(request))


#Vista para listar zonas
@login_required(login_url='/administrador/login/')
def zona_listar(request):

	zonas = Zona.objects.all().order_by('id')

	ctx={
		"zonas":zonas,
	}

	return render_to_response('administrador/zona/listar.html', ctx, context_instance=RequestContext(request))


#Vista para cerrar la sesion
@login_required
def logout_admin(request):

    logout(request)
    return HttpResponseRedirect('/administrador/')
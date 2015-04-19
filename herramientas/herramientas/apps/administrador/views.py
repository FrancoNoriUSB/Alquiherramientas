# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from datetime import datetime, date
from django.db.models import Count
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.models import inlineformset_factory, modelformset_factory, formset_factory
from models import *
from herramientas.apps.administrador.forms import *
from herramientas.apps.main.models import *
from herramientas.apps.administrador.models import *
from funciones import *
import json


#Vista de login de user administrador
def login_admin(request):

	loginF = LoginForm()
	email = ''
	password = ''
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	if request.POST:
		loginF = LoginForm(request.POST)
		if request.user.is_authenticated() and request.user and request.user.is_staff:
			return HttpResponseRedirect('/administrador/')
		else:
			email = request.POST['email']
			password = request.POST['password']
			usuario = authenticate(email=email, password=password)
			if usuario:
				#Caso del usuario activo
				if usuario.is_active and usuario.is_staff:
					login(request, usuario)
					return HttpResponseRedirect('/administrador/')
			else:
				#Usuario invalido o no existe!
				print "Invalid login details: {0}, {1}".format(email, password)

	ctx={
		'LoginForm':loginF,
	}

	return render_to_response('administrador/login/login.html', ctx, context_instance=RequestContext(request))


#Vista para confirmar el reseteo de la contrasena
def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='administrador/resetpass/password_reset_confirm.html',
        uidb64=uidb64, token=token, post_reset_redirect='/administrador/')


#Vista para resetear la contrasena
def reset(request):
    return password_reset(request, template_name='administrador/resetpass/password_reset_form.html',
        email_template_name='administrador/resetpass/password_reset_email.html',
        subject_template_name='administrador/resetpass/password_reset_subject.txt',
        post_reset_redirect='/administrador/')


#Vista del inicio
@login_required(login_url='/administrador/login/')
def inicio(request):

	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()
	ctx={
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/inicio/inicio.html', ctx, context_instance=RequestContext(request))


#Vista de la empresa en el admin
@login_required(login_url='/administrador/login/')
def empresa_admin(request):

	editado = ''
	empresa = get_object_or_404(Empresa, id=1)
	empresaF = EmpresaForm(instance=empresa)
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	if request.POST:
		empresaF = EmpresaForm(request.POST, instance=empresa)
		if empresaF.is_valid():
			empresaF.save()
			editado = True

	empresaF = EmpresaForm(instance=empresa)

	ctx={
		'EmpresaForm':empresaF,
		'editado':editado,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/empresa/empresa.html', ctx, context_instance=RequestContext(request))


#Vista de agregar producto de venta en el admin
@login_required(login_url='/administrador/login/')
def venta_agregar(request):

	editado = ''
	ventaF = VentaForm()
	imagenF = ImagenForm()
	herramientaF = HerramientaForm()
	estados = Estado.objects.all()
	direccionF = DireccionForm(initial={'estado':estados, 'ciudad':'', 'zona':''})
	ciudades = {'':'- Ciudad -'}
	zonas = {}
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	if request.POST:
		ventaF = VentaForm(request.POST)
		imagenF = ImagenForm(request.POST, request.FILES)
		herramientaF = HerramientaForm(request.POST)
		direccionF = DireccionForm(request.POST)
		if herramientaF.is_valid() and direccionF.is_valid() and imagenF.is_valid():
			herramienta = herramientaF.save(commit=False)
			direccion = direccionF.save(commit=False)
			imagen = imagenF.save(commit=False)
			if ventaF.is_valid():
				herramienta.save()
				direccion.save()
				imagen.save()
				venta = ventaF.save(commit=False)
				venta.herramienta = herramienta
				venta.direccion = direccion
				venta.imagen = imagen
				venta.disponible = True
				venta.save()
				editado = True

	#Ciudades a agregar
	for estado in Estado.objects.all().order_by('id'):
		ciudades_estado = Ciudad.objects.filter(estado=estado)
		for ciudad in ciudades_estado:
			ciudades[estado.id] = dict(Ciudad.objects.filter(estado=estado).values_list('id','nombre'))
	ciudades = json.dumps(ciudades)

	#Zonas a agregar
	for ciudad in Ciudad.objects.all():
		zonas[ciudad.id] = dict(Zona.objects.filter(ciudad=ciudad).values_list('id', 'nombre'))
	zonas = json.dumps(zonas)

	ctx={
		'VentaForm':ventaF,
		'HerramientaForm':herramientaF,
		'DireccionForm':direccionF,
		'ImagenForm':imagenF,
		'ciudades':ciudades,
		'zonas':zonas,
		'editado':editado,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/venta/agregar.html', ctx, context_instance=RequestContext(request))


#Vista de editar producto de venta en el admin
@login_required(login_url='/administrador/login/')
def venta_editar(request, id_producto):

	editado = ''
	venta = Venta.objects.get(id=id_producto)
	ventaF = VentaForm(instance=venta)
	imagenF = ImagenForm(instance=venta.imagen)
	herramientaF = HerramientaForm(instance=venta.herramienta)
	direccionF = DireccionForm(instance=venta.direccion)
	ciudades = {'':'- Ciudad -'}
	zonas = {'':'- Zona -'}
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()


	if request.POST:
		ventaF = VentaForm(request.POST, instance=venta)
		herramientaF = HerramientaForm(request.POST, instance=venta.herramienta)
		direccionF = DireccionForm(request.POST, instance=venta.direccion)
		imagenF = ImagenForm(request.POST, request.FILES, instance=venta.imagen)
		if herramientaF.is_valid() and direccionF.is_valid() and imagenF.is_valid():
			herramienta = herramientaF.save(commit=False)
			direccion = direccionF.save(commit=False)
			imagen = imagenF.save(commit=False)
			if ventaF.is_valid():
				herramienta.save()
				direccion.save()
				imagen.save()
				venta = ventaF.save(commit=False)
				venta.herramienta = herramienta
				venta.direccion = direccion
				venta.imagen = imagen
				venta.disponible = True
				venta.save()
				editado = True

	#Ciudades a agregar
	for estado in Estado.objects.all().order_by('id'):
		ciudades_estado = Ciudad.objects.filter(estado=estado)
		for ciudad in ciudades_estado:
			ciudades[estado.id] = dict(Ciudad.objects.filter(estado=estado).values_list('id','nombre'))
	ciudades = json.dumps(ciudades)

	#Zonas a agregar
	for ciudad in Ciudad.objects.all():
		zonas[ciudad.id] = dict(Zona.objects.filter(ciudad=ciudad).values_list('id', 'nombre'))
	zonas = json.dumps(zonas)

	ctx={
		'VentaForm':ventaF,
		'HerramientaForm':herramientaF,
		'DireccionForm':direccionF,
		'ImagenForm':imagenF,
		'ciudades':ciudades,
		'zonas':zonas,
		'editado':editado,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/venta/editar.html', ctx, context_instance=RequestContext(request))


#Vista de disponibilidad de venta
@login_required(login_url='/administrador/login/')
def venta_disponible(request, id_producto):

	venta = get_object_or_404(Venta, id=id_producto)
	venta.disponible = not (venta.disponible)
	venta.save()
	return HttpResponseRedirect('/administrador/venta/listar/')


#Vista de editar imagenes de producto de venta
@login_required(login_url='/administrador/login/')
def venta_imagen(request, id_producto):

	editado = ''
	venta = Venta.objects.get(id=id_producto)
	imagenes = ImagenProducto.objects.filter(Producto=venta)
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

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
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/venta/imagen.html', ctx, context_instance=RequestContext(request))


#Vista de listar productos de venta en el admin
@login_required(login_url='/administrador/login/')
def venta_listar(request):

	ventas = Venta.objects.all().order_by('-id')

	paginator = Paginator(ventas, 10)
	page = request.GET.get('page')
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

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
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/venta/listar.html', ctx, context_instance=RequestContext(request))


#Vista de listar productos que se han vendido
@login_required(login_url='/administrador/login/')
def venta_ventas(request):

	ventas = PagoVenta.objects.all().order_by('-id')

	paginator = Paginator(ventas, 10)
	page = request.GET.get('page')
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

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
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/venta/ventas.html', ctx, context_instance=RequestContext(request))


#Vista de verificacion de ventas realizados
@login_required(login_url='/administrador/login/')
def venta_ventas_verificar(request, id_producto):

	venta = get_object_or_404(PagoVenta, id=id_producto)
	venta.verificado = not (venta.verificado)
	venta.save()
	return HttpResponseRedirect('/administrador/venta/ventas/')


#Vista de eliminar venta
@login_required(login_url='/administrador/login/')
def venta_eliminar(request, id_producto):

	venta = get_object_or_404(Venta, id=id_producto)
	venta.delete()
	return HttpResponseRedirect('/administrador/venta/listar/')


#Vista de agregar producto de alquiler en el admin
@login_required(login_url='/administrador/login/')
def alquiler_agregar(request):

	editado = ''
	alquilerF = AlquilerForm()
	imagenF = ImagenForm()
	herramientaF = HerramientaForm()
	estados = Estado.objects.all()
	direccionF = DireccionForm(initial={'estado':estados, 'ciudad':'', 'zona':''})
	ciudades = {'':'- Ciudad -'}
	zonas = {'':'- Zona -'}
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	if request.POST:
		alquilerF = AlquilerForm(request.POST)
		imagenF = ImagenForm(request.POST, request.FILES)
		herramientaF = HerramientaForm(request.POST)
		direccionF = DireccionForm(request.POST)
		if herramientaF.is_valid() and direccionF.is_valid() and imagenF.is_valid():
			herramienta = herramientaF.save(commit=False)
			direccion = direccionF.save(commit=False)
			imagen = imagenF.save(commit=False)
			if alquilerF.is_valid():
				herramienta.save()
				direccion.save()
				imagen.save()
				alquiler = alquilerF.save(commit=False)
				alquiler.herramienta = herramienta
				alquiler.direccion = direccion
				alquiler.imagen = imagen
				alquiler.disponible = True
				alquiler.save()
				editado = True

	#Ciudades a agregar
	for estado in Estado.objects.all().order_by('id'):
		ciudades_estado = Ciudad.objects.filter(estado=estado)
		for ciudad in ciudades_estado:
			ciudades[estado.id] = dict(Ciudad.objects.filter(estado=estado).values_list('id','nombre'))
	ciudades = json.dumps(ciudades)

	#Zonas a agregar
	for ciudad in Ciudad.objects.all():
		zonas[ciudad.id] = dict(Zona.objects.filter(ciudad=ciudad).values_list('id', 'nombre'))
	zonas = json.dumps(zonas)

	ctx={
		'AlquilerForm':alquilerF,
		'HerramientaForm':herramientaF,
		'DireccionForm':direccionF,
		'ImagenForm': imagenF,
		'ciudades':ciudades,
		'zonas':zonas,
		'editado':editado,
		'notificaciones':notificaciones,
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
	imagenF = ImagenForm(instance=alquiler.imagen)
	ciudades = {'':'- Ciudad -'}
	zonas = {'':'- Zona -'}
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	if request.POST:
		alquilerF = AlquilerForm(request.POST, instance=alquiler)
		herramientaF = HerramientaForm(request.POST, instance=alquiler.herramienta)
		direccionF = DireccionForm(request.POST, instance=alquiler.direccion)
		imagenF = ImagenForm(request.POST, request.FILES, instance=alquiler.imagen)
		if herramientaF.is_valid() and direccionF.is_valid():
			herramienta = herramientaF.save(commit=False)
			direccion = direccionF.save(commit=False)
			imagen = imagenF.save(commit=False)
			if alquilerF.is_valid():
				herramienta.save()
				direccion.save()
				imagen.save()
				alquiler = alquilerF.save(commit=False)
				alquiler.herramienta = herramienta
				alquiler.direccion = direccion
				alquiler.imagen = imagen
				alquiler.disponible = True
				alquiler.save()
				editado = True

	#Ciudades a agregar
	for estado in Estado.objects.all().order_by('id'):
		ciudades_estado = Ciudad.objects.filter(estado=estado)
		for ciudad in ciudades_estado:
			ciudades[estado.id] = dict(Ciudad.objects.filter(estado=estado).values_list('id','nombre'))
	ciudades = json.dumps(ciudades)

	#Zonas a agregar
	for ciudad in Ciudad.objects.all():
		zonas[ciudad.id] = dict(Zona.objects.filter(ciudad=ciudad).values_list('id', 'nombre'))
	zonas = json.dumps(zonas)

	ctx={
		'AlquilerForm':alquilerF,
		'HerramientaForm':herramientaF,
		'ImagenForm': imagenF,
		'DireccionForm':direccionF,
		'ciudades':ciudades,
		'zonas':zonas,
		'editado':editado,
		'notificaciones':notificaciones,
	}
	
	return render_to_response('administrador/alquiler/editar.html', ctx, context_instance=RequestContext(request))


#Vista de disponibilidad de alquiler
@login_required(login_url='/administrador/login/')
def alquiler_disponible(request, id_producto):

	alquiler = get_object_or_404(Alquiler, id=id_producto)
	alquiler.disponible = not (alquiler.disponible)
	alquiler.save()
	return HttpResponseRedirect('/administrador/alquiler/listar/')


#Vista de editar imagenes de producto de alquiler
@login_required(login_url='/administrador/login/')
def alquiler_imagen(request, id_producto):

	editado = ''
	alquiler = Alquiler.objects.get(id=id_producto)
	imagenes = ImagenProducto.objects.filter(Producto=alquiler)
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

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
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/alquiler/imagen.html', ctx, context_instance=RequestContext(request))


#Vista de listar productos de alquiler en el admin
@login_required(login_url='/administrador/login/')
def alquiler_listar(request):

	alquileres = Alquiler.objects.all().order_by('-id')

	paginator = Paginator(alquileres, 10)
	page = request.GET.get('page')
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

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
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/alquiler/listar.html', ctx, context_instance=RequestContext(request))


#Vista de listar productos alquilados
@login_required(login_url='/administrador/login/')
def alquiler_alquileres(request):

	alquileres = PagoAlquiler.objects.all().order_by('-id')

	paginator = Paginator(alquileres, 10)
	page = request.GET.get('page')
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

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
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/alquiler/alquileres.html', ctx, context_instance=RequestContext(request))


#Vista de verificacion de alquileres realizados
@login_required(login_url='/administrador/login/')
def alquiler_alquileres_verificar(request, id_producto):

	alquiler = get_object_or_404(PagoAlquiler, id=id_producto)
	alquiler.verificado = not (alquiler.verificado)
	alquiler.save()
	return HttpResponseRedirect('/administrador/alquiler/alquileres/')


#Vista de eliminar alquiler
@login_required(login_url='/administrador/login/')
def alquiler_eliminar(request, id_producto):

	alquiler = get_object_or_404(Alquiler, id=id_producto)
	alquiler.delete()
	return HttpResponseRedirect('/administrador/alquiler/listar/')


#Vista de afiliaciones en el admin
@login_required(login_url='/administrador/login/')
def afiliacion_admin(request):

	editado = ''
	afiliacion = get_object_or_404(Afiliacion, id=1)
	afiliacionF = AfiliacionForm(instance=afiliacion)
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	if request.POST:
		afiliacionF = AfiliacionForm(request.POST, instance=afiliacion)
		if afiliacionF.is_valid():
			afiliacionF.save()
			editado = True

	afiliacionF = AfiliacionForm(instance=afiliacion)

	ctx={
		'AfiliacionForm':afiliacionF,
		'editado':editado,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/afiliacion/afiliacion.html', ctx, context_instance=RequestContext(request))


#Vista de contactos en el admin
@login_required(login_url='/administrador/login/')
def contactos_admin(request):

	editado = ''
	contactos = get_object_or_404(Contactos, id=1)
	contactosF = ContactosForm(instance=contactos)
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	if request.POST:
		contactosF = ContactosForm(request.POST, instance=contactos)
		if contactosF.is_valid():
			contactosF.save()
			editado = True

	contactosF = ContactosForm(instance=contactos)

	ctx={
		'ContactosForm':contactosF,
		'editado':editado,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/contactos/contactos.html', ctx, context_instance=RequestContext(request))


#Vista de los banners
@login_required(login_url='/administrador/login/')
def banners_admin(request):

	editado = ''
	banners = Banner.objects.all()
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	#Formset de imagen
	BannerFormset = modelformset_factory(Banner,  form=BannerForm, can_delete=True, extra=1, max_num=len(banners)+2, fields=['nombre', 'imagen', 'url'])
	bannerF = BannerFormset(queryset=Banner.objects.all())
	errores = []

	if request.POST:
		bannerF = BannerFormset(request.POST, request.FILES)
		errores = bannerF.errors
		if bannerF.is_valid():
			bannerF.save()

	bannerF = BannerFormset(queryset=Banner.objects.all())
	
	ctx = {
		'BannerForm':bannerF,
		'errores':errores,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/banners/banners.html', ctx, context_instance=RequestContext(request))


#Vista de la empresa en el admin
@login_required(login_url='/administrador/login/')
def usuario_listar(request):

	usuarios = User.objects.all().order_by('-id')

	paginator = Paginator(usuarios, 10)
	page = request.GET.get('page')
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()
	
	try:
		usuarios = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		usuarios = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		usuarios = paginator.page(paginator.num_pages)

	ctx={
		'usuarios':usuarios,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/usuarios/listar.html', ctx, context_instance=RequestContext(request))


#Vista de la empresa en el admin
@login_required(login_url='/administrador/login/')
def usuario_view(request, id_usuario):

	usuario = User.objects.get(id=id_usuario)
	usuario.is_active = False
	usuario.save()

	return HttpResponseRedirect('/administrador/usuario/listar/')


#Vista de bloqueo y desbloqueo de usuario de usuario
@login_required(login_url='/administrador/login/')
def usuario_bloquear(request, id_usuario):

	usuario = User.objects.get(id=id_usuario)
	usuario.is_active = not (usuario.is_active)
	usuario.save()

	return HttpResponseRedirect('/administrador/usuario/listar/')


#Vista de eliminar usuario
@login_required(login_url='/administrador/login/')
def usuario_eliminar(request, id_usuario):

	usuario = get_object_or_404(User, id=id_usuario)
	usuario.delete()
	return HttpResponseRedirect('/administrador/usuario/listar/')


#Vista de la empresa en el admin
@login_required(login_url='/administrador/login/')
def configuracion_admin(request):

	editado = ''
	modificado = ''
	user = User.objects.get(email=request.user.email)
	userF = UserChangeForm(instance=user)
	modificarF = modificarContrasenaForm(user=user)
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()
	
	if request.POST:
		userF = UserChangeForm(request.POST, instance=user)
		modificarF = modificarContrasenaForm(user=request.user,data=request.POST)
		if userF.is_valid():
			userF.save()
			editado = True
		elif modificarF.is_valid():
			modificarF.save()
			update_session_auth_hash(request, modificadoF.user)
			modificado = True

	userF = UserChangeForm(instance=user)
	modificarF = modificarContrasenaForm(user=user)

	ctx={
		'UserChangeForm':userF,
		'modificarContrasenaForm': modificarF,
		'editado':editado,
		'modificado':modificado,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/configuracion/configuracion.html', ctx, context_instance=RequestContext(request))


#Vista para agregar categorias
@login_required(login_url='/administrador/login/')
def categoria_agregar(request):

	editado = ''
	categoriaF = CategoriaForm()
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	if request.POST:
		categoriaF = CategoriaForm(request.POST)
		if categoriaF.is_valid():
			categoriaF.save()
			editado = True

	ctx={
		'CategoriaForm':categoriaF,
		'editado':editado,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/categoria/agregar.html', ctx, context_instance=RequestContext(request))


#Vista para editar categorias
@login_required(login_url='/administrador/login/')
def categoria_editar(request, id_categoria):

	editado = ''
	categoria = get_object_or_404(Categoria, id=id_categoria)
	categoriaF = CategoriaForm(instance=categoria)
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	if request.POST:
		categoriaF = CategoriaForm(request.POST, instance=categoria)
		if categoriaF.is_valid():
			categoriaF.save()
			editado = True

	ctx={
		'CategoriaForm':categoriaF,
		'editado':editado,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/categoria/editar.html', ctx, context_instance=RequestContext(request))


#Vista para listar categorias
@login_required(login_url='/administrador/login/')
def categoria_listar(request):

	categorias = Categoria.objects.all().order_by('-id')

	paginator = Paginator(categorias, 10)
	page = request.GET.get('page')
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	try:
		categorias = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		categorias = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		categorias = paginator.page(paginator.num_pages)

	ctx={
		"categorias":categorias,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/categoria/listar.html', ctx, context_instance=RequestContext(request))


#Vista de eliminar categoria
@login_required(login_url='/administrador/login/')
def categoria_eliminar(request, id_categoria):

	categoria = get_object_or_404(Categoria, id=id_categoria)
	categoria.delete()
	return HttpResponseRedirect('/administrador/categoria/listar/')


#Vista para agregar marcas
@login_required(login_url='/administrador/login/')
def marca_agregar(request):

	editado = ''
	marcaF = MarcaForm()
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	if request.POST:
		marcaF = MarcaForm(request.POST)
		if marcaF.is_valid():
			marcaF.save()
			editado = True

	ctx={
		'MarcaForm':marcaF,
		'editado':editado,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/marca/agregar.html', ctx, context_instance=RequestContext(request))


#Vista para editar marcas
@login_required(login_url='/administrador/login/')
def marca_editar(request, id_marca):

	editado = ''
	marca = get_object_or_404(Marca, id=id_marca)
	marcaF = MarcaForm(instance=marca)
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	if request.POST:
		marcaF = MarcaForm(request.POST,instance=marca)
		if marcaF.is_valid():
			marcaF.save()
			editado = True

	ctx={
		'MarcaForm':marcaF,
		'editado':editado,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/marca/editar.html', ctx, context_instance=RequestContext(request))


#Vista para listar marcas
@login_required(login_url='/administrador/login/')
def marca_listar(request):

	marcas = Marca.objects.all().order_by('-id')

	paginator = Paginator(marcas, 10)
	page = request.GET.get('page')
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	try:
		marcas = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		marcas = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		marcas = paginator.page(paginator.num_pages)

	ctx={
		"marcas":marcas,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/marca/listar.html', ctx, context_instance=RequestContext(request))


#Vista de eliminar marca
@login_required(login_url='/administrador/login/')
def marca_eliminar(request, id_marca):

	marca = get_object_or_404(Marca, id=id_marca)
	marca.delete()
	return HttpResponseRedirect('/administrador/marca/listar/')


#Vista para agregar modelos
@login_required(login_url='/administrador/login/')
def modelo_agregar(request):

	editado = ''
	modeloF = ModeloForm()
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	if request.POST:
		modeloF = ModeloForm(request.POST)
		if modeloF.is_valid():
			modeloF.save()
			editado = True

	ctx={
		'ModeloForm':modeloF,
		'editado':editado,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/modelo/agregar.html', ctx, context_instance=RequestContext(request))


#Vista para editar modelos
@login_required(login_url='/administrador/login/')
def modelo_editar(request, id_modelo):

	editado = ''
	modelo = get_object_or_404(Modelo, id=id_modelo)
	modeloF = ModeloForm(instance=modelo)
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	if request.POST:
		modeloF = ModeloForm(request.POST,instance=modelo)
		if modeloF.is_valid():
			modeloF.save()
			editado = True

	ctx={
		'ModeloForm':modeloF,
		'editado':editado,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/modelo/editar.html', ctx, context_instance=RequestContext(request))


#Vista para listar modelos
@login_required(login_url='/administrador/login/')
def modelo_listar(request):

	modelos = Modelo.objects.all().order_by('-id')

	paginator = Paginator(modelos, 10)
	page = request.GET.get('page')
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()
	
	try:
		modelos = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		modelos = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		modelos = paginator.page(paginator.num_pages)

	ctx={
		"modelos":modelos,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/modelo/listar.html', ctx, context_instance=RequestContext(request))


#Vista de eliminar modelo
@login_required(login_url='/administrador/login/')
def modelo_eliminar(request, id_modelo):

	modelo = get_object_or_404(Modelo, id=id_modelo)
	modelo.delete()
	return HttpResponseRedirect('/administrador/modelo/listar/')


#Vista para agregar estados
@login_required(login_url='/administrador/login/')
def estado_agregar(request):

	editado = ''
	estadoF = EstadoForm()
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	if request.POST:
		estadoF = EstadoForm(request.POST)
		if estadoF.is_valid():
			estadoF.save()
			editado = True

	ctx={
		'EstadoForm':estadoF,
		'editado':editado,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/estado/agregar.html', ctx, context_instance=RequestContext(request))


#Vista para editar estados
@login_required(login_url='/administrador/login/')
def estado_editar(request, id_estado):

	editado = ''
	estado = get_object_or_404(Estado,id=id_estado)
	estadoF = EstadoForm(instance=estado)
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	if request.POST:
		estadoF = EstadoForm(request.POST,instance=estado)
		if estadoF.is_valid():
			estadoF.save()
			editado = True

	ctx={
		'EstadoForm':estadoF,
		'editado':editado,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/estado/editar.html', ctx, context_instance=RequestContext(request))


#Vista para listar estados
@login_required(login_url='/administrador/login/')
def estado_listar(request):

	estados = Estado.objects.all().order_by('-id')

	paginator = Paginator(estados, 10)
	page = request.GET.get('page')
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	try:
		estados = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		estados = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		estados = paginator.page(paginator.num_pages)

	ctx={
		"estados":estados,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/estado/listar.html', ctx, context_instance=RequestContext(request))


#Vista de eliminar estado
@login_required(login_url='/administrador/login/')
def estado_eliminar(request, id_estado):

	estado = get_object_or_404(Estado, id=id_estado)
	estado.delete()
	return HttpResponseRedirect('/administrador/estado/listar/')


#Vista para agregar ciudades
@login_required(login_url='/administrador/login/')
def ciudad_agregar(request):

	editado = ''
	ciudadF = CiudadForm()
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	if request.POST:
		ciudadF = CiudadForm(request.POST)
		if ciudadF.is_valid():
			ciudadF.save()
			editado = True

	ctx={
		'CiudadForm':ciudadF,
		'editado':editado,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/ciudad/agregar.html', ctx, context_instance=RequestContext(request))


#Vista para editar ciudades
@login_required(login_url='/administrador/login/')
def ciudad_editar(request, id_ciudad):

	editado = ''
	ciudad = get_object_or_404(Ciudad,id=id_ciudad)
	ciudadF = CiudadForm(instance=ciudad)
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	if request.POST:
		ciudadF = CiudadForm(request.POST,instance=ciudad)
		if ciudadF.is_valid():
			ciudadF.save()
			editado = True

	ctx={
		'CiudadForm':ciudadF,
		'editado':editado,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/ciudad/editar.html', ctx, context_instance=RequestContext(request))


#Vista para listar ciudades
@login_required(login_url='/administrador/login/')
def ciudad_listar(request):

	ciudades = Ciudad.objects.all().order_by('-id')

	paginator = Paginator(ciudades, 10)
	page = request.GET.get('page')
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	try:
		ciudades = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		ciudades = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		ciudades = paginator.page(paginator.num_pages)

	ctx={
		"ciudades":ciudades,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/ciudad/listar.html', ctx, context_instance=RequestContext(request))


#Vista de eliminar ciudad
@login_required(login_url='/administrador/login/')
def ciudad_eliminar(request, id_ciudad):

	ciudad = get_object_or_404(Ciudad, id=id_ciudad)
	ciudad.delete()
	return HttpResponseRedirect('/administrador/ciudad/listar/')


#Vista para agregar zonas
@login_required(login_url='/administrador/login/')
def zona_agregar(request):

	editado = ''
	zonaF = ZonaForm()
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	if request.POST:
		zonaF = ZonaForm(request.POST)
		if zonaF.is_valid():
			zonaF.save()
			editado = True

	ctx={
		'ZonaForm':zonaF,
		'editado':editado,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/zona/agregar.html', ctx, context_instance=RequestContext(request))


#Vista para editar zonas
@login_required(login_url='/administrador/login/')
def zona_editar(request, id_zona):

	editado = ''
	zona = get_object_or_404(Zona,id=id_zona)
	zonaF = ZonaForm(instance=zona)
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	if request.POST:
		zonaF = ZonaForm(request.POST,instance=zona)
		if zonaF.is_valid():
			zonaF.save()
			editado = True

	ctx={
		'ZonaForm':zonaF,
		'editado':editado,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/zona/editar.html', ctx, context_instance=RequestContext(request))


#Vista para listar zonas
@login_required(login_url='/administrador/login/')
def zona_listar(request):

	zonas = Zona.objects.all().order_by('-id')

	paginator = Paginator(zonas, 10)
	page = request.GET.get('page')
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()
	
	try:
		zonas = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		zonas = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		zonas = paginator.page(paginator.num_pages)

	ctx={
		"zonas":zonas,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/zona/listar.html', ctx, context_instance=RequestContext(request))


#Vista de eliminar zona
@login_required(login_url='/administrador/login/')
def zona_eliminar(request, id_zona):

	zona = get_object_or_404(Zona, id=id_zona)
	zona.delete()
	return HttpResponseRedirect('/administrador/zona/listar/')


#Vista para cargar las clausulas
def clausulas(request):

	editado = ''
	clausulas = Clausula.objects.filter(id__range=(1,10))
	clausulasFormset = modelformset_factory(Clausula, form=ClausulasForm, extra=1, max_num=2, can_delete=True)
	clausulasF = clausulasFormset(queryset=clausulas)
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()

	if request.method == 'POST':
		clausulasFormset = modelformset_factory(Clausula, form=ClausulasForm, extra=1, max_num=2, can_delete=True)
		clausulasF = clausulasFormset(request.POST, request.FILES, queryset=clausulas)

		if clausulasF.is_valid():
			clausulasSet = clausulasF.save(commit=False)
			for clausula in clausulasSet:
				clausula.save()
				editado = True

	ctx = {
		'ClausulasForm':clausulasF,
		'editado':editado,
		'notificaciones':notificaciones,
	}

	return render_to_response('administrador/clausulas/clausulas.html',ctx, context_instance=RequestContext(request))


#Vista para eliminar las notificaciones
def notificacion_eliminar(request,id_notif):

	notificacion = get_object_or_404(Notificacion, id=id_notif)
	notificacion.delete()
	notificaciones = Notificacion.objects.all().order_by('created_at')[:10].reverse()
	return HttpResponseRedirect('/')


#Vista para cerrar la sesion
@login_required
def logout_admin(request):

	logout(request)
	return HttpResponseRedirect('/administrador/')

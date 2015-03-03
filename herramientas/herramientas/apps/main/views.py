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
from random import randint
from funciones import *
from models import *
from forms import *
from herramientas.apps.administrador.forms import LoginForm, UserCreationForm
from herramientas.apps.administrador.models import Banner
import json

# Mercadopago
# Funcion que se encuentra en mercadopago.py
import mercadopago
import os, sys

#Variable global que tiene datos especificos del cliente. No tocar por ahora
mp = mercadopago.MP("1735954876648483", "hsJ0KIzKHXSYVudbHcCG3yBdmEUF0abn")

#Vista del inicio
def inicio(request):

    #Formulario de busqueda
    busquedaF = BusquedaForm()

    # formulario de nuevo usuario
    usuarioF = UserCreationForm()

    #Formulario de ingreso
    loginF = LoginForm()

    #Banners superiores
    banners = Banner.objects.all().order_by('id')

    # Ofertas de los productos
    ofertas = []
    ofertas = Producto.objects.filter(oferta=True).filter(disponible=True).order_by('?')

    #Ciudades
    ciudades = {}
    
    #Zonas
    zonas = {}

    #Productos que se ofertan
    productos = Producto.objects.filter(disponible=True).order_by('fecha_producto')

    productos_list = productos

    #Caso que se realizo una busqueda
    if request.GET:
        busquedaF = BusquedaForm(request.GET)
        
        #Caso para el buscador de herramientas
        print busquedaF
        if busquedaF.is_valid():
            tipo = busquedaF.cleaned_data['tipo']
            categoria = busquedaF.cleaned_data['categoria']
            marca = busquedaF.cleaned_data['marca']
            estado = busquedaF.cleaned_data['estado']
            ano = busquedaF.cleaned_data['ano']
            precio = busquedaF.cleaned_data['precio']
            precio = precio.split('-', 2)

            #Precios en el rango que se pide
            if len(precio) > 1:
                precio_menor = precio[0]
                precio_mayor = precio[1]
            else:
                precio_menor = 0
                precio_mayor = 10000000000000000

            #Verificacion de campos
            if tipo != '' or categoria != None or marca != None or estado != None or ano != None or len(precio) > 1:

                #Verificacion de string vacio
                if tipo == '':
                    tipo = None

                #Campos a buscar
                fields_list = []
                fields_list.append('herramienta')
                fields_list.append('herramienta')
                fields_list.append('herramienta')
                fields_list.append('direccion')
                if tipo == 'venta':
                    fields_list.append('precio')
                elif tipo == 'alquiler':
                    fields_list.append('precio')

                #Comparadores para buscar
                types_list=[]
                types_list.append('categoria__nombre__exact')
                types_list.append('marca__nombre__exact')
                types_list.append('ano__exact')
                types_list.append('estado__nombre__exact')
                types_list.append('range')

                #Valores a buscar
                values_list=[]
                values_list.append(categoria)
                values_list.append(marca)
                values_list.append(ano)
                values_list.append(estado)
                values_list.append((precio_menor, precio_mayor))

                operator = 'and'

                if tipo != None:
                    if tipo == 'alquiler':
                        productos_list = dynamic_query(Alquiler, fields_list, types_list, values_list, operator)
                        if productos_list == {}:
                            productos_list = Alquiler.objects.all().order_by('fecha_producto')
                    else:
                        productos_list = dynamic_query(Venta, fields_list, types_list, values_list, operator)
                        if productos_list == {}:
                            productos_list = Venta.objects.all().order_by('fecha_producto')
                else:
                    productos_list = dynamic_query(Producto, fields_list, types_list, values_list, operator)

    productos_list = tuple(productos_list)
    paginator = Paginator(productos_list, 6)
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
        elif loginF.is_valid():
            return HttpResponseRedirect('/login/')

    #Preparar el objeto Json de las ciudades
    for estado in Estado.objects.all():
        ciudades[estado.id] = dict(Ciudad.objects.filter(estado=estado).values_list('id', 'nombre'))
    ciudades = json.dumps(ciudades)

    #Preparar el objeto Json de las zonas
    for ciudad in Ciudad.objects.all():
        zona = dict(Zona.objects.filter(ciudad__id=ciudad.id).values_list('id', 'nombre'))
        if zona != {}:
            zonas[ciudad.id] = zona
    zonas = json.dumps(zonas)

    ctx = {
        'BusquedaForm':busquedaF,
        'ofertas':ofertas,
        'productos':productos,
        'UsuarioForm':usuarioF,
        'LoginForm':loginF,
        'banners':banners,
        'ciudades':ciudades,
        'zonas':zonas,
    }

    return render_to_response('main/inicio/inicio.html', ctx, context_instance=RequestContext(request))


# Vista de la informacion de la empresa
def empresa(request):

    #Formulario de busqueda
    busquedaF = BusquedaForm()

    # Formulario de nuevo usuario
    usuarioF = UserCreationForm()   

    #Formulario de ingreso
    loginF = LoginForm()

    #Banners superiores
    banners = Banner.objects.all().order_by('id')

    #Ciudades
    ciudades = Ciudad.objects.all()
    
    #Zonas
    zonas = Zona.objects.all()

    #Datos de la empresa
    empresa = Empresa.objects.get(id=1)

    # Ofertas de los productos
    ofertas = []
    ofertas =  Producto.objects.filter(oferta=True).filter(disponible=True).order_by('?')

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
        'LoginForm':loginF,
        'banners':banners,
        'ciudades':ciudades,
        'zonas':zonas,
        'empresa':empresa,
    }

    return render_to_response('main/empresa/empresa.html', ctx, context_instance=RequestContext(request))


# Vista de los productos
def productos(request, palabra):

    #Formulario de busqueda
    busquedaF = BusquedaForm()

    #Formulario de nuevo usuario
    usuarioF = UserCreationForm()

    #Formulario de ingreso
    loginF = LoginForm()

    #Banners superiores
    banners = Banner.objects.all().order_by('id')

    #Ciudades
    ciudades = {}
    
    #Zonas
    zonas = {}
    
    ofertas = []
    ofertas =  Producto.objects.filter(oferta=True).filter(disponible=True).order_by('?')
    

    #productos que se ofertan
    if palabra == 'alquiler':
        productos = Alquiler.objects.filter(disponible=True).order_by('fecha_producto')
    else:
        productos = Venta.objects.filter(disponible=True).order_by('fecha_producto')

    # Creando un nuevo usuario
    if request.method=='POST':
        usuarioF = UserCreationForm(request.POST)
        if usuarioF.is_valid():
            usuarioF.save()
            return HttpResponseRedirect('/')

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

    #Preparar el objeto Json de las ciudades
    for estado in Estado.objects.all():
        ciudades[estado.id] = dict(Ciudad.objects.filter(estado=estado).values_list('id', 'nombre'))
    ciudades = json.dumps(ciudades)

    #Preparar el objeto Json de las zonas
    for ciudad in Ciudad.objects.all():
        zona = dict(Zona.objects.filter(ciudad__id=ciudad.id).values_list('id', 'nombre'))
        if zona != {}:
            zonas[ciudad.id] = zona
    zonas = json.dumps(zonas)

    ctx = {
        'BusquedaForm':busquedaF,
        'ofertas':ofertas,
        'productos':productos,
        'UsuarioForm':usuarioF,
        'LoginForm':loginF,
        'banners':banners,
        'ciudades':ciudades,
        'zonas':zonas,
    }

    return render_to_response('main/productos/productos.html', ctx, context_instance=RequestContext(request))


# Vista de un producto especifico
def producto(request, id_producto):

    #Formulario de busqueda
    busquedaF = BusquedaForm()
    
    # Formulario de nuevo usuario
    usuarioF = UserCreationForm()

    #Formulario de ingreso
    loginF = LoginForm()

    #Banners superiores
    banners = Banner.objects.all().order_by('id')

    # Formulario de contacto
    contactoF = ContactoForm()

    #Ciudades
    ciudades = Ciudad.objects.all()
    
    #Zonas
    zonas = Zona.objects.all()
    
    # Ofertas de los productos
    ofertas = []
    ofertas =  Producto.objects.filter(oferta=True).filter(disponible=True).order_by('?')
    
    #Datos iniciales de formularios de venta y alquiler
    dataA = {}
    dataV = {}
    ventaF = VentaForm()
    alquilerF = AlquilerForm()

    producto = Producto.objects.get(id=id_producto)

    # Formularios de compra o alquiler con data inicial.
    try:
        dataA = {
            'precio': producto.alquiler.precio,
            'dias':1,
            'cantidad':1,
            'garantia': producto.alquiler.precio,
            'total':producto.alquiler.precio,
            'clausulas':False
        }
    except:
        dataV = {
            'precio': producto.venta.precio,
            'cantidad':1,
            'total': producto.venta.precio
        }

    if dataA != {}:
        alquilerF = AlquilerForm(initial=dataA)
    elif dataV != {}:
        ventaF = VentaForm(initial=dataV)

    # Creando un nuevo usuario
    if request.method=='POST':
        nombre = producto.titulo
        usuarioF = UserCreationForm(request.POST)
        contactoF = ContactoForm(request.POST)

        if usuarioF.is_valid():
            usuarioF.save()
            return HttpResponseRedirect('/')

        if contactoF.is_valid():
            contact_email_producto(request, contactoF, nombre)
            retorno = '/productos/'+str(id_producto)+'/'
            return HttpResponseRedirect(retorno)


    # Crear el slider con las imagenes del producto
    imagenes = producto.imagenes.all()
    x = 1
    indicador = """ <li data-target="#carousel-example-generic" data-slide-to="%s" class="active"></li> """ %x
    wrap = """ <div class="item active">
                    <img src="/media/%s" />
                </div> """ % producto.imagen
    for i in imagenes:
        indicador += """ <li data-target="#carousel-example-generic" data-slide-to="%s"></li> """ %x
        wrap += """ <div class="item">
                          <img src="/media/%s"/>
                        </div> """ % i.imagen
        x += 1

    indicator = """ <ol class="carousel-indicators"> """ + indicador + """ </ol> """
    wrapper = """ <div class="carousel-inner" role="listbox"> """ + wrap + """ </div> """

    ctx = {
        'BusquedaForm':busquedaF,
        'LoginForm':loginF,
        'banners':banners,
        'UsuarioForm':usuarioF,
        'ofertas':ofertas,
        'producto':producto,
        'alquilerF':alquilerF,
        'ventaF':ventaF,
        'ciudades':ciudades,
        'zonas':zonas,
        'contactoF':contactoF,
        'indicator':indicator,
        'wrapper':wrapper,

    }

    return render_to_response('main/productos/producto.html', ctx, context_instance=RequestContext(request))

# View que contiene el boton de pago. Falta trabajar.
def pagar(request, id_producto):

    #Formulario de busqueda
    busquedaF = BusquedaForm()
    
    # Formulario de nuevo usuario
    usuarioF = UserCreationForm()

    #Formulario de ingreso
    loginF = LoginForm()

    #Banners superiores
    banners = Banner.objects.all().order_by('id')
    
    # Formulario de contacto
    contactoF = ContactoForm()

    #Ciudades
    ciudades = Ciudad.objects.all()
    
    #Zonas
    zonas = Zona.objects.all()
    
    # Ofertas de los productos
    ofertas = []
    ofertas =  Producto.objects.filter(oferta=True).filter(disponible=True).order_by('?')

    producto = Producto.objects.get(id=id_producto)

    boton = ''

    # Creando un nuevo usuario
    if request.method=='POST':
        usuarioF = UserCreationForm(request.POST)

        if usuarioF.is_valid():
            usuarioF.save()
            return HttpResponseRedirect('/')

        # Registro del pago.
        nombre = producto.titulo
        razon = producto
        fecha = datetime.datetime.now()
        usuario = request.user
        alquilerF = AlquilerForm(request.POST)
        ventaF = VentaForm(request.POST)
        
        if alquilerF.is_valid():
            precio = alquilerF.cleaned_data['total']
            dias = alquilerF.cleaned_data['dias']
            total = alquilerF.cleaned_data['total']
            cantidad = alquilerF.cleaned_data['cantidad']
            acepto = alquilerF.cleaned_data['clausulas']
            pagoAlquiler = PagoAlquiler.objects.create(producto=razon,monto=precio,dias=dias,
                                                       fecha=fecha,usuario=usuario,verificado=False,
                                                       cantidad=cantidad,aceptado=acepto)
            email_alquiler(request, usuario.nombre, usuario.apellido, usuario.telefono, usuario.email, nombre, dias, cantidad)
            if total > 100000.00:
                return HttpResponseRedirect('/datos/')
        elif ventaF.is_valid():
            precio = ventaF.cleaned_data['total']
            cantidad = ventaF.cleaned_data['cantidad']
            acepto = ventaF.cleaned_data['clausulas']
            pagoVenta = PagoVenta.objects.create(producto=razon,monto=precio,fecha=fecha,
                                                 usuario=usuario,verificado=False,cantidad=cantidad,aceptado=acepto)
            email_venta(request, usuario.nombre, usuario.apellido, usuario.telefono, usuario.email, nombre, cantidad)
            if precio > 100000.00:
                return HttpResponseRedirect('/datos/')

        boton = mercadopago(request, nombre, float(precio))

    ctx = {
        'BusquedaForm':busquedaF,
        'ofertas':ofertas,
        'producto': producto,
        'UsuarioForm':usuarioF,
        'LoginForm':loginF,
        'banners':banners,
        'ciudades':ciudades,
        'zonas':zonas,
        'contactoF': contactoF,
        'boton_mp': boton,
    }

    return render_to_response('main/productos/pago.html', ctx, context_instance=RequestContext(request))

# View de los datos bancarios.
def datos(request):

    #Formulario de busqueda
    busquedaF = BusquedaForm()
    
    # Formulario de nuevo usuario
    usuarioF = UserCreationForm()

    # Formulario de contacto
    contactoF = ContactoForm()

    #Formulario de ingreso
    loginF = LoginForm()

    #Banners superiores
    banners = Banner.objects.all().order_by('id')
    
    #Ciudades
    ciudades = Ciudad.objects.all()
    
    #Zonas
    zonas = Zona.objects.all()

    # Ofertas de los productos
    ofertas = []
    ofertas =  Producto.objects.filter(oferta=True).filter(disponible=True).order_by('?')
    
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
        'LoginForm':loginF,
        'banners':banners,
        'ciudades':ciudades,
        'zonas':zonas,
    }

    return render_to_response('main/productos/datos.html', ctx, context_instance=RequestContext(request))


#View para setear el boton de mercadopago
def mercadopago(request, pago, monto, **kwargs):
    preference = {
      "items": [
        {
          "title": pago,
          "quantity": 1,
          "currency_id": "VEN",
          "unit_price": monto
        }
      ]
    }

    preferenceResult = mp.create_preference(preference)

    url = preferenceResult["response"]["init_point"]

    output = """
        <a href="{url}" name="MP-Checkout" class="blue-l-arall-rn">Pagar</a>
        <script type="text/javascript" src="http://mp-tools.mlstatic.com/buttons/render.js"></script>
    """.format (url=url)
    
    return output


# Vista para la afiliacion
def afiliacion(request):

    #Formulario de busqueda
    busquedaF = BusquedaForm()
    
    # Formulario de nuevo usuario
    usuarioF = UserCreationForm()

    #Formulario de ingreso
    loginF = LoginForm()

    #Banners superiores
    banners = Banner.objects.all().order_by('id')
    
    #Ciudades
    ciudades = Ciudad.objects.all()
    
    #Zonas
    zonas = Zona.objects.all()

    #Afiliacion de alquiherramientas
    afiliacion = Afiliacion.objects.get(id=1)
    
    # Ofertas de los productos
    ofertas = []
    ofertas =  Producto.objects.filter(oferta=True).filter(disponible=True).order_by('?')


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
        'LoginForm':loginF,
        'banners':banners,
        'ciudades':ciudades,
        'zonas':zonas,
        'afiliacion':afiliacion,
    }

    return render_to_response('main/afiliacion/afiliacion.html', ctx, context_instance=RequestContext(request))


# Vista de contactos
def contactos(request):

    #Formulario de busqueda
    busquedaF = BusquedaForm()
    
    # Formulario de nuevo usuario
    usuarioF = UserCreationForm()

    # Formulario de contacto
    contactoF = ContactoForm()

    #Formulario de ingreso
    loginF = LoginForm()

    #Banners superiores
    banners = Banner.objects.all().order_by('id')
    
    #Ciudades
    ciudades = Ciudad.objects.all()
    
    #Zonas
    zonas = Zona.objects.all()

    #Contactos de alquiherramientas
    contactos = Contactos.objects.get(id=1)
    
    #Formulario de contacto
    if request.method == 'POST':
        contactoF = ContactoForm(request.POST)
        if contactoF.is_valid():
            contact_email(request, contactoF)
            return HttpResponseRedirect('/contactos/')

    # Ofertas de los productos
    ofertas = []
    ofertas =  Producto.objects.filter(oferta=True).filter(disponible=True).order_by('?')

    # Creando un nuevo usuario
    if request.method=='POST':
        usuarioF = UserCreationForm(request.POST)
        if usuarioF.is_valid():
            usuarioF.save()
            return HttpResponseRedirect('/')

    ctx = {
        'BusquedaForm':busquedaF,
        'ofertas':ofertas,
        'ContactoForm':contactoF,
        'UsuarioForm':usuarioF,
        'LoginForm':loginF,
        'banners':banners,
        'ciudades':ciudades,
        'zonas':zonas,
        'contactos':contactos,
    }

    return render_to_response('main/contactos/contactos.html', ctx, context_instance=RequestContext(request))



# Vista para login de usuario
def loginUser(request):

    email = ''
    password = ''
    
    if request.user.is_authenticated() and request.user:
        return HttpResponseRedirect('/perfil/')
    else:
        email = request.POST['email']
        password = request.POST['password']
        usuario = authenticate(email=email, password=password)

        if usuario:
                # Caso del usuario activo
                if usuario.is_active:
                    login(request, usuario)
                    return HttpResponseRedirect('/perfil/')
                else:
                    return "Tu cuenta esta bloqueada"
        else:
            # Usuario invalido o no existe!
            print "Invalid login details: {0}, {1}".format(email, password)

    return HttpResponseRedirect('/')


#Vista de perfil de usuario
@login_required
def perfilCompras(request):
    usuario = request.user
    ventas = PagoVenta.objects.filter(usuario=usuario.pk)

    ctx = {
        'ventas': ventas,
    }

    return render_to_response('main/perfil/perfil_compras.html', ctx, context_instance=RequestContext(request))

@login_required
def perfilAlquiler(request):
    usuario = request.user
    alquiler = PagoAlquiler.objects.filter(usuario=usuario.pk)

    ctx = {
        'alquiler': alquiler,
    }

    return render_to_response('main/perfil/perfil_alquileres.html', ctx, context_instance=RequestContext(request))


# Vista para logout de usuario
def logoutUser(request):

    logout(request)
    return HttpResponseRedirect('/')
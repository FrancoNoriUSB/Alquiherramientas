from django.conf.urls import *
from django.conf import settings

#Urls para los views del frontend del usuario visitante
urlpatterns = patterns('herramientas.apps.administrador.views',

	#Url del panel de inicio del admin
    url(r'^administrador/$', 'inicio', name='inicio'),

	#Url de la empresa
    url(r'^administrador/empresa/$', 'empresa', name='empresa'),

	#Url de ventas y alquileres
    url(r'^administrador/venta/agregar$', 'venta_agregar', name='venta_agregar'),
    url(r'^administrador/venta/listar$', 'venta_listar', name='venta_listar'),
    url(r'^administrador/alquiler/agregar$', 'alquiler_agregar', name='alquiler_agregar'),
    url(r'^administrador/alquiler/listar$', 'alquiler_listar', name='alquiler_listar'),

	#Url de afiliacion de usuarios
    url(r'^administrador/afiliacion/$', 'afiliacion', name='afiliacion'),

	#Url de contactos
    url(r'^administrador/contactos/$', 'contactos', name='contactos'),

	#Url de banners
    url(r'^administrador/banners/$', 'banners', name='banners'),

	#Url de usuarios
    url(r'^administrador/usuarios/$', 'usuarios', name='usuarios'),

	#Url de configuracion
    url(r'^administrador/configuracion/$', 'configuracion', name='configuracion'),

)
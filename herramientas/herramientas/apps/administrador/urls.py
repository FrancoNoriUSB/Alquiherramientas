from django.conf.urls import *
from django.conf import settings

#Urls para los views del frontend del usuario visitante
urlpatterns = patterns('herramientas.apps.administrador.views',

    #Url del panel de inicio del admin
    url(r'^administrador/$', 'inicio', name='inicio'),

    #Url del panel de inicio del admin
    url(r'^administrador/login/$', 'login_admin', name='login_admin'),

	#Url de la empresa
    url(r'^administrador/empresa/$', 'empresa_admin', name='empresa_admin'),

	#Urls de ventas
    url(r'^administrador/venta/agregar/$', 'venta_agregar', name='venta_agregar'),
    url(r'^administrador/venta/editar/(?P<id_producto>[0-9A-Za-z]+)/$', 'venta_editar', name='venta_editar'),
    url(r'^administrador/venta/listar/$', 'venta_listar', name='venta_listar'),

    #Urls de alquileres
    url(r'^administrador/alquiler/agregar/$', 'alquiler_agregar', name='alquiler_agregar'),
    url(r'^administrador/alquiler/editar/(?P<id_producto>[0-9A-Za-z]+)/$', 'alquiler_editar', name='alquiler_editar'),
    url(r'^administrador/alquiler/listar/$', 'alquiler_listar', name='alquiler_listar'),

	#Url de afiliacion de usuarios
    url(r'^administrador/afiliacion/$', 'afiliacion_admin', name='afiliacion_admin'),

	#Url de contactos
    url(r'^administrador/contactos/$', 'contactos_admin', name='contactos_admin'),

	#Url de banners
    url(r'^administrador/banners/$', 'banners_admin', name='banners_admin'),

	#Url de usuarios
    url(r'^administrador/usuarios/$', 'usuarios_admin', name='usuarios_admin'),

	#Url de configuracion
    url(r'^administrador/configuracion/$', 'configuracion_admin', name='configuracion_admin'),

    #Url del panel de inicio del admin
    url(r'^administrador/logout/$', 'logout_admin', name='logout_admin'),

)
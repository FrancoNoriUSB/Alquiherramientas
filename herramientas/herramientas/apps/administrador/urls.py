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

    #Urls de categorias
    url(r'^administrador/categoria/agregar/$', 'categoria_agregar', name='categoria_agregar'),
    url(r'^administrador/categoria/editar/(?P<id_categoria>[0-9A-Za-z]+)/$', 'categoria_editar', name='alquiler_editar'),
    url(r'^administrador/categoria/listar/$', 'categoria_listar', name='categoria_listar'),

    #Urls de marcas
    url(r'^administrador/marca/agregar/$', 'marca_agregar', name='marca_agregar'),
    url(r'^administrador/marca/editar/(?P<id_marca>[0-9A-Za-z]+)/$', 'marca_editar', name='marca_editar'),
    url(r'^administrador/marca/listar/$', 'marca_listar', name='marca_listar'),

    #Urls de modelos
    url(r'^administrador/modelo/agregar/$', 'modelo_agregar', name='modelo_agregar'),
    url(r'^administrador/modelo/editar/(?P<id_modelo>[0-9A-Za-z]+)/$', 'modelo_editar', name='modelo_editar'),
    url(r'^administrador/modelo/listar/$', 'modelo_listar', name='modelo_listar'),

    #Urls de estados
    url(r'^administrador/estado/agregar/$', 'estado_agregar', name='estado_agregar'),
    url(r'^administrador/estado/editar/(?P<id_estado>[0-9A-Za-z]+)/$', 'estado_editar', name='estado_editar'),
    url(r'^administrador/estado/listar/$', 'estado_listar', name='estado_listar'),

    #Urls de ciudad
    url(r'^administrador/ciudad/agregar/$', 'ciudad_agregar', name='ciudad_agregar'),
    url(r'^administrador/ciudad/editar/(?P<id_ciudad>[0-9A-Za-z]+)/$', 'ciudad_editar', name='ciudad_editar'),
    url(r'^administrador/ciudad/listar/$', 'ciudad_listar', name='ciudad_listar'),

    #Urls de zonas
    url(r'^administrador/zona/agregar/$', 'zona_agregar', name='zona_agregar'),
    url(r'^administrador/zona/editar/(?P<id_zona>[0-9A-Za-z]+)/$', 'zona_editar', name='zona_editar'),
    url(r'^administrador/zona/listar/$', 'zona_listar', name='zona_listar'),
)
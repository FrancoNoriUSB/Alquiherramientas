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
    url(r'^administrador/venta/disponible/(?P<id_producto>[0-9A-Za-z]+)/$', 'venta_disponible', name='venta_disponible'),
    url(r'^administrador/venta/imagen/(?P<id_producto>[0-9A-Za-z]+)/$', 'venta_imagen', name='venta_imagen'),
    url(r'^administrador/venta/listar/$', 'venta_listar', name='venta_listar'),
    url(r'^administrador/venta/ventas/$', 'venta_ventas', name='venta_ventas'),
    url(r'^administrador/venta/ventas/verificar/(?P<id_producto>[0-9A-Za-z]+)/$', 'venta_ventas_verificar', name='venta_ventas_verificar'),
    url(r'^administrador/venta/eliminar/(?P<id_producto>[0-9A-Za-z]+)/$', 'venta_eliminar', name='venta_eliminar'),

    #Urls de alquileres
    url(r'^administrador/alquiler/agregar/$', 'alquiler_agregar', name='alquiler_agregar'),
    url(r'^administrador/alquiler/editar/(?P<id_producto>[0-9A-Za-z]+)/$', 'alquiler_editar', name='alquiler_editar'),
    url(r'^administrador/alquiler/disponible/(?P<id_producto>[0-9A-Za-z]+)/$', 'alquiler_disponible', name='alquiler_disponible'),
    url(r'^administrador/alquiler/imagen/(?P<id_producto>[0-9A-Za-z]+)/$', 'alquiler_imagen', name='alquiler_imagen'),
    url(r'^administrador/alquiler/listar/$', 'alquiler_listar', name='alquiler_listar'),
    url(r'^administrador/alquiler/alquileres/$', 'alquiler_alquileres', name='alquiler_alquileres'),
    url(r'^administrador/alquiler/alquileres/verificar/(?P<id_producto>[0-9A-Za-z]+)/$', 'alquiler_alquileres_verificar', name='alquiler_alquileres_verificar'),
    url(r'^administrador/alquiler/eliminar/(?P<id_producto>[0-9A-Za-z]+)/$', 'alquiler_eliminar', name='alquiler_eliminar'),

	#Url de afiliacion de usuarios
    url(r'^administrador/afiliacion/$', 'afiliacion_admin', name='afiliacion_admin'),

	#Url de contactos
    url(r'^administrador/contactos/$', 'contactos_admin', name='contactos_admin'),

	#Url de banners
    url(r'^administrador/banners/$', 'banners_admin', name='banners_admin'),

	#Url de usuarios
    url(r'^administrador/usuario/listar/$', 'usuario_listar', name='usuario_listar'),
    url(r'^administrador/usuario/(?P<id_usuario>[0-9A-Za-z]+)/$', 'usuario_view', name='usuario_view'),
    url(r'^administrador/usuario/bloquear/(?P<id_usuario>[0-9A-Za-z]+)/$', 'usuario_bloquear', name='usuario_bloquear'),
    url(r'^administrador/usuario/eliminar/(?P<id_usuario>[0-9A-Za-z]+)/$', 'usuario_eliminar', name='usuario_eliminar'),

	#Url de configuracion
    url(r'^administrador/configuracion/$', 'configuracion_admin', name='configuracion_admin'),

    #Url del panel de inicio del admin
    url(r'^administrador/logout/$', 'logout_admin', name='logout_admin'),

    #Urls de categorias
    url(r'^administrador/categoria/agregar/$', 'categoria_agregar', name='categoria_agregar'),
    url(r'^administrador/categoria/editar/(?P<id_categoria>[0-9A-Za-z]+)/$', 'categoria_editar', name='categoria_editar'),
    url(r'^administrador/categoria/listar/$', 'categoria_listar', name='categoria_listar'),
    url(r'^administrador/categoria/eliminar/(?P<id_categoria>[0-9A-Za-z]+)/$', 'categoria_eliminar', name='categoria_eliminar'),

    #Urls de marcas
    url(r'^administrador/marca/agregar/$', 'marca_agregar', name='marca_agregar'),
    url(r'^administrador/marca/editar/(?P<id_marca>[0-9A-Za-z]+)/$', 'marca_editar', name='marca_editar'),
    url(r'^administrador/marca/listar/$', 'marca_listar', name='marca_listar'),
    url(r'^administrador/marca/eliminar/(?P<id_marca>[0-9A-Za-z]+)/$', 'marca_eliminar', name='marca_eliminar'),

    #Urls de modelos
    url(r'^administrador/modelo/agregar/$', 'modelo_agregar', name='modelo_agregar'),
    url(r'^administrador/modelo/editar/(?P<id_modelo>[0-9A-Za-z]+)/$', 'modelo_editar', name='modelo_editar'),
    url(r'^administrador/modelo/listar/$', 'modelo_listar', name='modelo_listar'),
    url(r'^administrador/modelo/eliminar/(?P<id_modelo>[0-9A-Za-z]+)/$', 'modelo_eliminar', name='modelo_eliminar'),

    #Urls de estados
    url(r'^administrador/estado/agregar/$', 'estado_agregar', name='estado_agregar'),
    url(r'^administrador/estado/editar/(?P<id_estado>[0-9A-Za-z]+)/$', 'estado_editar', name='estado_editar'),
    url(r'^administrador/estado/listar/$', 'estado_listar', name='estado_listar'),
    url(r'^administrador/estado/eliminar/(?P<id_estado>[0-9A-Za-z]+)/$', 'estado_eliminar', name='estado_eliminar'),

    #Urls de ciudad
    url(r'^administrador/ciudad/agregar/$', 'ciudad_agregar', name='ciudad_agregar'),
    url(r'^administrador/ciudad/editar/(?P<id_ciudad>[0-9A-Za-z]+)/$', 'ciudad_editar', name='ciudad_editar'),
    url(r'^administrador/ciudad/listar/$', 'ciudad_listar', name='ciudad_listar'),
    url(r'^administrador/ciudad/eliminar/(?P<id_ciudad>[0-9A-Za-z]+)/$', 'ciudad_eliminar', name='ciudad_eliminar'),

    #Urls de zonas
    url(r'^administrador/zona/agregar/$', 'zona_agregar', name='zona_agregar'),
    url(r'^administrador/zona/editar/(?P<id_zona>[0-9A-Za-z]+)/$', 'zona_editar', name='zona_editar'),
    url(r'^administrador/zona/listar/$', 'zona_listar', name='zona_listar'),
    url(r'^administrador/zona/eliminar/(?P<id_zona>[0-9A-Za-z]+)/$', 'zona_eliminar', name='zona_eliminar'),
)
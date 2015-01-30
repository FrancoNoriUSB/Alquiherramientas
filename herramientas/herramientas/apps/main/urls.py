from django.conf.urls import *
from django.conf import settings

#Urls para los views del frontend del usuario visitante
urlpatterns = patterns('herramientas.apps.main.views',

	#View del home
    url(r'^$', 'inicio', name='inicio'),

    #View de empresa
    url(r'^empresa/$', 'empresa', name='empresa'),

    #Views de los productos
    url(r'^productos/(?P<palabra>[A-Z a-z]+)$', 'productos', name='productos'),
    url(r'^productos/(?P<id_producto>\d+)/$', 'producto', name='producto'),

    #View de afiliacion
    url(r'^afiliacion/$', 'afiliacion', name='afiliacion'),

    #View de contactos
    url(r'^contactos/$', 'contactos', name='contactos'),

    #View de login de usuario
    url(r'^login/$', 'loginUser', name='loginUser'),

    #View de perfil de usuario
    url(r'^perfil/$', 'perfil', name='perfil'),

    #View de login de usuario
    url(r'^logout/$', 'logoutUser', name='logoutUser'),
)
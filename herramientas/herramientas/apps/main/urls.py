from django.conf.urls import *
from django.conf import settings

#Urls para los views del frontend del usuario visitante
urlpatterns = patterns('herramientas.apps.main.views',

	#View del home
    url(r'^$', 'ultimasPublicaciones', name='inicio'),

    #View de empresa
    url(r'^empresa/$', 'empresa', name='empresa'),

    #Views de los productos
    url(r'^productos/$', 'productos', name='productos'),
    url(r'^productos/(?P<id_producto>\d+)/$', 'producto', name='producto'),

    #View de afiliacion
    url(r'^afiliacion/$', 'afiliacion', name='afiliacion'),

    #View de contactos
    url(r'^contactos/$', 'contactos', name='contactos'),
)
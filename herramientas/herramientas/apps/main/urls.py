from django.conf.urls import *
from django.conf import settings

#Urls para los views del frontend del usuario visitante
urlpatterns = patterns('herramientas.apps.main.views',

	#View del home
    url(r'^$', 'inicio', name='inicio'),

    #View de empresa
    url(r'^empresa/$', 'empresa', name='empresa'),

    #Views de los publicaciones
    url(r'^publicaciones/$', 'publicaciones', name='publicaciones'),
    url(r'^publicaciones/(?P<id_publicacion>\d+)/$', 'publicacion', name='publicacion'),

    #View de afiliacion
    url(r'^afiliacion/$', 'afiliacion', name='afiliacion'),

    #View de contactos
    url(r'^contactos/$', 'contactos', name='contactos'),
)
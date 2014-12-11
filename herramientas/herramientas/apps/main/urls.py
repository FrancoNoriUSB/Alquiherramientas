from django.conf.urls import *
from django.conf import settings

#Urls para los views del frontend del usuario visitante
urlpatterns = patterns('herramientas.apps.main.views',
    url(r'^$', 'home', name='home'),
    url(r'^herramientas/$', 'allHerramieta', name='herramientas'),
    url(r'^herramientas/(?P<herramienta>\d+)/$', 'viewHerramienta', name='herramientas'),
)
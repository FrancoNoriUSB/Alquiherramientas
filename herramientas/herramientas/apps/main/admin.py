from django.contrib import admin
from herramientas.apps.main.models import Alquiler, Ciudad, Venta, Direccion, Estado
from herramientas.apps.main.models import Herramienta, Marca, Modelo, Publicacion, Zona


admin.site.register(Alquiler)
admin.site.register(Ciudad)
admin.site.register(Venta)
admin.site.register(Direccion)
admin.site.register(Estado)
admin.site.register(Herramienta)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Publicacion)
admin.site.register(Zona)

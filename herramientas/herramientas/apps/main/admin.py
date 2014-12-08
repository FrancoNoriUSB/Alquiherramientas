from django.contrib import admin
from herramientas.apps.main.models import Alquiler, Ciudad, Compra, Direccion, Estado
from herramientas.apps.main.models import Herramienta, Marca, Modelo, Publicacion, Zona


admin.site.register(Alquiler)
admin.site.register(Ciudad)
admin.site.register(Compra)
admin.site.register(Direccion)
admin.site.register(Estado)
admin.site.register(Herramienta)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Zona)

from django.contrib import admin
from herramientas.apps.main.models import Alquiler, Categoria, Ciudad, Venta, Direccion, Estado
from herramientas.apps.main.models import Herramienta, Marca, Modelo, Producto, Zona, Empresa


admin.site.register(Alquiler)
admin.site.register(Categoria)
admin.site.register(Ciudad)
admin.site.register(Venta)
admin.site.register(Direccion)
admin.site.register(Estado)
admin.site.register(Empresa)
admin.site.register(Herramienta)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Producto)
admin.site.register(Zona)

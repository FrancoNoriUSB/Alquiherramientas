from django.contrib import admin
from herramientas.apps.main.models import *


class ImagenProductoInline(admin.TabularInline):
	model = ImagenProducto
	extra = 2
	max_num = 6

class ProductoAdmin(admin.ModelAdmin):
	inlines = (ImagenProductoInline,)

admin.site.register(Alquiler, ProductoAdmin)
admin.site.register(Afiliacion)
admin.site.register(Categoria)
admin.site.register(Ciudad)
admin.site.register(Contactos)
admin.site.register(Venta, ProductoAdmin)
admin.site.register(Direccion)
admin.site.register(Estado)
admin.site.register(Empresa)
admin.site.register(Herramienta)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Zona)

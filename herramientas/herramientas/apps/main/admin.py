from django.contrib import admin
from herramientas.apps.main.models import Alquiler, Categoria, Ciudad, Venta, Direccion, Estado
<<<<<<< HEAD
from herramientas.apps.main.models import Herramienta, Marca, Modelo, Producto, Zona, Empresa
=======
from herramientas.apps.main.models import Herramienta, Marca, Modelo, Producto, Zona, ImagenProducto


class ImagenProductoInline(admin.TabularInline):
	model = ImagenProducto
	extra = 2
	max_num = 6

class ProductoAdmin(admin.ModelAdmin):
	inlines = (ImagenProductoInline,)
>>>>>>> c5922837ddea2d05098cd48b4f89c4e8273da5d3


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
admin.site.register(Zona)
admin.site.register(Producto, ProductoAdmin)

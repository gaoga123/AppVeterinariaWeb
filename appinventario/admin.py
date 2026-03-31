from django.contrib import admin

from .models import Producto, TipoProducto

# Register your models here.


def marcar_sin_stock(modeladmin, request, queryset):
    queryset.update(stock=0)


marcar_sin_stock.short_description = "Marcar productos seleccionados como SIN STOCK"


def normalizar_tipo_producto(modeladmin, request, queryset):
    for tipo in queryset:
        tipo.nombre = tipo.nombre.upper()
        tipo.save()


normalizar_tipo_producto.short_description = "Normalizar nombre"


class ProductoAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Datos del Producto", {"fields": [
         "nombre", "descripcion", "stock", "precio", "tipo"]}),
    ]
    list_display = ["nombre", "stock", "precio", "tipo"]
    ordering = ["-nombre"]
    list_filter = ["tipo"]
    actions = [marcar_sin_stock]


class TipoProductoAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Datos del Tipo de Producto", {"fields": [
         "nombre"]}),
    ]
    list_display = ["nombre"]
    ordering = ["-nombre"]
    actions = [normalizar_tipo_producto]


admin.site.register(Producto, ProductoAdmin)
admin.site.register(TipoProducto, TipoProductoAdmin)

from django.contrib import admin

from .models import DetallePedido, Pedido

# Register your models here.


class PedidoAdmin(admin.ModelAdmin):
    list_display = ["cliente", "fecha", "total"]
    ordering = ["-fecha"]

    list_filter = ["cliente", "fecha"]
    search_fields = ["cliente__username"]

    date_hierarchy = "fecha"


class DetallePedidoAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Usuario asociado al Dueño", {"fields": [
         "pedido", "producto", "cantidad", "precio"]}),
    ]
    list_display = ["pedido", "producto", "cantidad", "precio"]
    ordering = ["-pedido"]


admin.site.register(Pedido, PedidoAdmin)
admin.site.register(DetallePedido, DetallePedidoAdmin)

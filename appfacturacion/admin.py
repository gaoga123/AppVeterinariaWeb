from decimal import Decimal

from django.contrib import admin
from django.shortcuts import get_object_or_404, render
from django.urls import path
from django.utils.html import format_html

from .models import DetalleFactura, Factura

# Register your models here.


def recalcular_total_factura(modeladmin, request, queryset):
    for factura in queryset:
        total = Decimal("0.00")
        for detalle in factura.detalles.all():
            total += detalle.subtotal
        factura.total = total
        factura.save()


recalcular_total_factura.short_description = "Recalcular total de la factura"


def recalcular_subtotal_detalle(modeladmin, request, queryset):
    for detalle in queryset:
        subtotal = Decimal("0.00")

        if detalle.producto:
            subtotal = detalle.producto.precio * detalle.cantidad

        elif detalle.consulta:
            subtotal = Decimal("5000.00")

        detalle.subtotal = subtotal
        detalle.save()


recalcular_subtotal_detalle.short_description = "Recalcular subtotal del detalle"


class FacturaAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Datos del Detalle de la Factura", {"fields": [
         "cliente", "fecha", "total", "metodo_pago"]}),
    ]
    list_display = ["cliente", "fecha", "total", "metodo_pago"]
    ordering = ["-fecha"]
    actions = [
        recalcular_total_factura,
    ]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "<int:factura_id>/detalle/",
                self.admin_site.admin_view(self.detalle_factura),
                name="factura-detalle",
            ),
        ]
        return custom_urls + urls

    def detalle_factura(self, request, factura_id):
        factura = get_object_or_404(Factura, pk=factura_id)
        detalles = factura.detalles.all()

        return render(
            request,
            "admin/facturacion/factura_detalle.html",
            {
                "factura": factura,
                "detalles": detalles,
            },
        )

    def ver_detalle(self, obj):
        return format_html(
            '<a class="button" href="{}">Ver / Editar</a>',
            f"{obj.id}/detalle/"
        )

    ver_detalle.short_description = "Detalle"


class DetalleFacturaAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Datos del Detalle de la Factura", {"fields": [
         "factura", "producto", "cantidad", "subtotal"]}),
    ]
    list_display = ["factura", "producto", "cantidad", "subtotal"]
    ordering = ["-factura"]
    actions = [
        recalcular_subtotal_detalle,
    ]


admin.site.register(Factura, FacturaAdmin)
admin.site.register(DetalleFactura, DetalleFacturaAdmin)

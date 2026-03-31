from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .forms import DetalleFacturaForm, FacturaForm
from .models import DetalleFactura, Factura

# Create your views here.


def ultima_factura(request):

    factura = Factura.objects.filter(cliente=request.user).last()

    return render(request, "factura.html", {
        "factura": factura
    })


class FacturaCreateView(FormView):
    template_name = "appfacturacion/facturacion.html"
    form_class = FacturaForm
    success_url = reverse_lazy("facturacion:factura_creada")

    def form_valid(self, form):
        factura = form.save(commit=False)
        factura.total = 0  # se calculará al agregar detalles
        factura.save()
        return super().form_valid(form)


class DetalleFacturaCreateView(FormView):
    template_name = "appfacturacion/detalle_factura.html"
    form_class = DetalleFacturaForm
    success_url = reverse_lazy("facturacion:detalle_creado")

    def form_valid(self, form):
        factura_id = self.kwargs.get("factura_id")
        factura = Factura.objects.get(id=factura_id)

        detalle = form.save(commit=False)
        detalle.factura = factura
        detalle.subtotal = 0  # será calculado abajo

        # --- Lógica de precio dinámico ---
        if detalle.producto:
            detalle.subtotal = detalle.producto.precio * detalle.cantidad

        if detalle.consulta:
            # Si facturás consultas, podés agregar un precio fijo:
            detalle.subtotal = 5000  # ejemplo, reemplazar según regla

        detalle.save()

        # actualizar total de factura
        factura.total += detalle.subtotal
        factura.save()

        return super().form_valid(form)

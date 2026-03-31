from django import forms

from .models import DetalleFactura, Factura


class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ["cliente", "metodo_pago"]


class DetalleFacturaForm(forms.ModelForm):
    class Meta:
        model = DetalleFactura
        fields = ["producto", "cantidad"]

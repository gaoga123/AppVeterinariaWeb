from django import forms

from .models import Producto, TipoProducto


class TipoProductoForm(forms.ModelForm):
    class Meta:
        model = TipoProducto
        fields = ["nombre"]


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "descripcion", "stock", "precio", "tipo"]

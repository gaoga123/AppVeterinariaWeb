from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import ProductoForm, TipoProductoForm
from .models import Producto, TipoProducto

# Create your views here.


class TipoProductoCreateView(FormView):
    template_name = "appinventario/tipo_producto.html"
    form_class = TipoProductoForm
    success_url = "tipo_producto_creado"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def tipo_producto_creado(request):
    params = {}
    params['nombre_sitio'] = 'Veterinaria Web'
    tipos_productos = TipoProducto.objects.all()
    params['tipo_productos'] = tipos_productos
    return render(request, 'appinventario/tipo_producto_creado.html', params)


class ProductoCreateView(FormView):
    template_name = "appinventario/inventario.html"
    form_class = ProductoForm
    success_url = "producto_creado"

    def form_valid(self, form):
        # Aquí podrías validar stock inicial o registrar historial
        form.save()
        return super().form_valid(form)


def producto_creado(request):
    params = {}
    params['nombre_sitio'] = 'Veterinaria Web'
    productos = Producto.objects.all()
    params['productos'] = productos
    return render(request, 'appinventario/producto_creado.html', params)

from django.urls import path

from .views import (
    ProductoCreateView,
    TipoProductoCreateView,
    producto_creado,
    tipo_producto_creado,
)

urlpatterns = [
    path("producto/", ProductoCreateView.as_view(), name="producto"),
    path("tipo/", TipoProductoCreateView.as_view(), name="tipo"),
    path("producto/producto_creado/", producto_creado, name="producto_creado"),
    path("tipo/tipo_producto_creado/",
         tipo_producto_creado, name="tipo_producto_creado"),
]

from django.urls import path

from .views import carrito, checkout, pedido_creado

urlpatterns = [
    path("", carrito, name="carrito"),
    path("finalizar-compra/", checkout, name="checkout"),
    path("pedido-creado/", pedido_creado, name="pedido-creado"),
]

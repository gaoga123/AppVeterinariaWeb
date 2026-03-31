from django.urls import path

from .views import DetalleFacturaCreateView, FacturaCreateView

urlpatterns = [
    path("factura/", FacturaCreateView.as_view(), name="factura"),
    path("detalle/", DetalleFacturaCreateView.as_view(), name="detalle"),
]

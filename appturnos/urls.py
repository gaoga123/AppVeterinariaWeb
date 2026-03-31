from django.urls import path

from .views import CitaCreateView, cita_creada

urlpatterns = [
    path("", CitaCreateView.as_view(), name="citas"),
    path("turno-confirmado/", cita_creada, name="cita_creada"),
]

from django.urls import path

from .views import (
    MascotaCreateView,
    buscar_mascotas,
    buscar_mascotas_ajax,
    mascota_creada,
    opciones_mascotas,
)

urlpatterns = [
    path("", MascotaCreateView.as_view(), name="mascotas"),
    path("opciones/", opciones_mascotas, name="opciones_mascotas"),
    path("buscar/", buscar_mascotas, name="buscar_mascotas"),
    path("buscar/ajax/", buscar_mascotas_ajax, name="buscar_mascotas_ajax"),
    path("registro-exitoso/", mascota_creada, name="mascota_creada"),
]

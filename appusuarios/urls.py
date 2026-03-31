from django.urls import path

from .views import ClienteCreateFormView, ProfesionalCreateFormView

urlpatterns = [
    path("cliente/nuevo/",
         ClienteCreateFormView.as_view(),
         name="crear_cliente"),
    path("profesional/nuevo/",
         ProfesionalCreateFormView.as_view(),
         name="crear_profesional"),
]

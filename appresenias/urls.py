from django.urls import path

from .views import ReseniaCreateView, resenia_creada

urlpatterns = [
    path("", ReseniaCreateView.as_view(), name="resenias"),
    path("opinion-enviada/", resenia_creada, name="resenia_creada"),
]

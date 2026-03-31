from django.db import models
from django.utils import timezone

# Create your models here.


class ReseniaRestApi(models.Model):
    cliente = models.TextField(blank=True, null=True)
    puntuacion = models.PositiveIntegerField(
        choices=[(1, "1 / 5 Estrellas"), (2, "2 / 5 Estrellas"),
                 (3, "3 / 5 Estrellas"), (4, "4 / 5 Estrellas"),
                 (5, "5 / 5 Estrellas")], default=5)
    comentarios = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(default=timezone.now)
    aprobada = models.BooleanField(default=False)

    def __str__(self):
        return f"Reseña de {self.cliente} ({self.puntuacion} estrellas)"

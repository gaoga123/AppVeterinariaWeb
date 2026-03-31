from django.db import models
from django.utils import timezone

from appusuarios.models import Cliente


class Resenia(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="resenias",
        db_index=True
    )

    puntuacion = models.PositiveIntegerField(
        choices=[
            (1, "1 / 5 Estrellas"),
            (2, "2 / 5 Estrellas"),
            (3, "3 / 5 Estrellas"),
            (4, "4 / 5 Estrellas"),
            (5, "5 / 5 Estrellas")
        ],
        default=5,
        db_index=True
    )

    comentarios = models.TextField(blank=True, null=True)

    fecha = models.DateTimeField(
        default=timezone.now,
        db_index=True
    )

    aprobada = models.BooleanField(default=False, db_index=True)

    class Meta:
        ordering = ["-fecha"]
        indexes = [
            models.Index(fields=["cliente", "fecha"]),
            models.Index(fields=["aprobada", "fecha"]),
        ]

    def __str__(self):
        return f"Reseña de {self.cliente.user.username} ({self.puntuacion}⭐)"

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from appinventario.models import Producto

# Create your models here.


class Pedido(models.Model):
    cliente = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_index=True
    )

    fecha = models.DateTimeField(default=timezone.now, db_index=True)

    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        ordering = ["-fecha"]
        indexes = [
            models.Index(fields=["cliente"]),
            models.Index(fields=["fecha"]),
        ]

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente}"


class DetallePedido(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name="detalles",
        db_index=True
    )

    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        db_index=True
    )

    cantidad = models.PositiveIntegerField()

    precio = models.DecimalField(max_digits=10, decimal_places=2)

    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        indexes = [
            models.Index(fields=["pedido"]),
            models.Index(fields=["producto"]),
        ]

    def save(self, *args, **kwargs):
        self.subtotal = self.precio * self.cantidad
        super().save(*args, **kwargs)

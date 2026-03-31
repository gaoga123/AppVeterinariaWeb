from django.db import models
from django.utils import timezone

from appinventario.models import Producto
from appusuarios.models import Cliente


class Factura(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = "pendiente", "Pendiente"
        PAGADA = "pagada", "Pagada"
        CANCELADA = "cancelada", "Cancelada"

    class MetodoPago(models.TextChoices):
        EFECTIVO = "efectivo", "Efectivo"
        TARJETA = "tarjeta", "Tarjeta"
        TRANSFERENCIA = "transferencia", "Transferencia"

    numero = models.CharField(max_length=20, unique=True, db_index=True)

    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.PENDIENTE,
        db_index=True
    )

    metodo_pago = models.CharField(
        max_length=20,
        choices=MetodoPago.choices
    )

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="facturas",
        db_index=True
    )

    pedido = models.OneToOneField(
        "appcarrito.Pedido",
        on_delete=models.CASCADE,
        related_name="factura",
        null=True,
        blank=True
    )

    fecha = models.DateTimeField(default=timezone.now, db_index=True)

    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        ordering = ["-fecha"]
        indexes = [
            models.Index(fields=["numero"]),
            models.Index(fields=["estado"]),
            models.Index(fields=["cliente"]),
            models.Index(fields=["fecha"]),
        ]

    def __str__(self):
        return f"Factura #{self.numero} - {self.cliente.user}"


class DetalleFactura(models.Model):
    factura = models.ForeignKey(
        Factura,
        on_delete=models.CASCADE,
        related_name="detalles",
        db_index=True
    )

    producto = models.ForeignKey(
        Producto,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    cantidad = models.PositiveIntegerField(default=1)

    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        indexes = [
            models.Index(fields=["factura"]),
        ]

    def save(self, *args, **kwargs):
        self.subtotal = self.precio_unitario * self.cantidad
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Factura {self.factura.numero} - {self.producto}"

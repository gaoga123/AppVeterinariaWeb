from django.db import models


class TipoProducto(models.Model):
    nombre = models.CharField(max_length=100, unique=True, db_index=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=150, unique=True, db_index=True)
    descripcion = models.TextField(blank=True)
    stock = models.PositiveIntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    tipo = models.ForeignKey(
        TipoProducto,
        on_delete=models.SET_NULL,
        null=True,
        related_name="productos",
        db_index=True
    )

    imagen = models.ImageField(
        upload_to="productos/",
        blank=True,
        null=True
    )

    class Meta:
        ordering = ["nombre"]
        indexes = [
            models.Index(fields=["nombre"]),
            models.Index(fields=["tipo"]),
        ]

    def __str__(self):
        return f"{self.nombre} (${self.precio})"

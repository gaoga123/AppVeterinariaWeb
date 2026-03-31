from django.db import models
from django.utils import timezone

from appusuarios.models import Cliente


class Especie(models.Model):
    nombre = models.CharField(max_length=50, unique=True, db_index=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Raza(models.Model):
    especie = models.ForeignKey(
        Especie,
        on_delete=models.CASCADE,
        related_name="razas"
    )
    nombre = models.CharField(max_length=50)

    class Meta:
        unique_together = ("especie", "nombre")
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} ({self.especie.nombre})"


class Mascota(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="mascotas",
        db_index=True
    )
    especie = models.ForeignKey(
        Especie,
        on_delete=models.SET_NULL,
        null=True
    )
    raza = models.ForeignKey(
        Raza,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    nombre = models.CharField(max_length=100, db_index=True)
    sexo = models.CharField(
        max_length=6,
        choices=[("Macho", "Macho"), ("Hembra", "Hembra")]
    )
    edad = models.PositiveIntegerField(default=0)
    fecha_alta = models.DateTimeField(default=timezone.now, db_index=True)
    notas = models.TextField(blank=True, null=True)
    imagen = models.ImageField(
        upload_to="imgmascota",
        blank=True,
        null=True
    )

    class Meta:
        ordering = ["nombre"]
        indexes = [
            models.Index(fields=["cliente", "nombre"]),
        ]

    def __str__(self):
        return f"{self.nombre} ({self.especie})"

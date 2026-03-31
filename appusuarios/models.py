from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="cliente",
        db_index=True
    )
    fecha_registro = models.DateTimeField(
        default=timezone.now,
        db_index=True
    )

    class Meta:
        ordering = ["-fecha_registro"]

    def __str__(self):
        return self.user.username


class Rol(models.Model):
    nombre = models.CharField(
        max_length=50,
        unique=True,
        db_index=True
    )

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Profesional(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)
    apellido = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(unique=True)
    rol = models.ForeignKey(
        Rol,
        on_delete=models.SET_NULL,
        null=True,
        related_name="profesionales"
    )
    fecha_alta = models.DateTimeField(
        default=timezone.now,
        db_index=True
    )

    class Meta:
        ordering = ["apellido", "nombre"]
        indexes = [
            models.Index(fields=["apellido", "nombre"]),
        ]

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rol})"

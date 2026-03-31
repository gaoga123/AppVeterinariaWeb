from django.db import models

from appmascotas.models import Mascota
from appusuarios.models import Profesional

# Create your models here.


class EstadoCita(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Cita(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE,
                                related_name="citas")
    veterinario = models.ForeignKey(Profesional, on_delete=models.SET_NULL,
                                    null=True, related_name="citas")
    fecha = models.DateTimeField()
    motivo = models.TextField()
    estado = models.ForeignKey(EstadoCita, on_delete=models.SET_NULL,
                               null=True)

    def __str__(self):
        return f"Cita de {self.mascota.nombre} para el {self.fecha.strftime('%d/%m/%Y %H:%M')}"

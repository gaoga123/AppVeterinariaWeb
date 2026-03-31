from django.contrib import admin
from django.db.models.functions import Upper
from django.shortcuts import render

from .models import Cita, EstadoCita

# Register your models here.


def marcar_como_atendida(modeladmin, request, queryset):
    estado_atendida, _ = EstadoCita.objects.get_or_create(nombre="Atendida")
    queryset.update(estado=estado_atendida)


marcar_como_atendida.short_description = "Marcar citas como 'Atendidas'"


def normalizar_nombres(modeladmin, request, queryset):
    for estado in queryset:
        estado.nombre = estado.nombre.capitalize()

    EstadoCita.objects.bulk_update(queryset, ["nombre"])


normalizar_nombres.short_description = "Normalizar nombres (Mayúscula inicial)"


def confirmar_citas(modeladmin, request, queryset):
    estado_confirmada, _ = EstadoCita.objects.get_or_create(
        nombre="Confirmada")

    if request.method == "POST" and "apply" in request.POST:
        queryset.update(estado=estado_confirmada)
        modeladmin.message_user(
            request,
            "Las citas fueron confirmadas correctamente."
        )
        return None

    return render(
        request,
        "admin/acciones/confirmar_cita.html",
        {
            "citas": queryset,
            "action": "confirmar_citas",
        },
    )


confirmar_citas.short_description = "Confirmar citas seleccionadas"


class CitaAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Datos de la Cita", {"fields": [
         "mascota", "veterinario"]}),
        ("Detalles de la Cita", {"fields": [
         "fecha", "motivo", "estado"]}),
    ]
    list_display = ["mascota", "veterinario", "fecha", "estado"]
    list_select_related = ["mascota", "veterinario", "estado"]
    list_filter = ["estado", "veterinario", "fecha"]
    search_fields = ["mascota__nombre", "veterinario__nombre"]
    ordering = ["-fecha"]
    actions = [marcar_como_atendida, confirmar_citas]


class EstadoCitaAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Datos del Estado de la Cita", {"fields": [
         "nombre"]}),
    ]
    list_display = ["nombre"]
    ordering = ["-nombre"]
    actions = [normalizar_nombres]


admin.site.register(Cita, CitaAdmin)
admin.site.register(EstadoCita, EstadoCitaAdmin)

from django.contrib import admin

from .models import Resenia


@admin.action(description="Aprobar reseñas seleccionadas")
def aprobar_resenias(modeladmin, request, queryset):
    queryset.update(aprobada=True)


class ReseniaAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Datos de la Reseña", {
            "fields": ["cliente", "puntuacion", "comentarios", "fecha", "aprobada"]
        }),
    ]

    list_display = ["cliente", "puntuacion", "aprobada", "fecha"]
    ordering = ["-fecha"]
    list_filter = ["aprobada", "puntuacion", "fecha"]
    search_fields = ["cliente__user__username", "comentarios"]

    actions = [aprobar_resenias]


admin.site.register(Resenia, ReseniaAdmin)

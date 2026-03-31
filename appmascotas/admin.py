from django.contrib import admin
from django.utils.text import capfirst

from .models import Especie, Mascota, Raza

# Register your models here.


def normalizar_nombre(modeladmin, request, queryset):
    for obj in queryset:
        obj.nombre = capfirst(obj.nombre.strip())
        obj.save()


normalizar_nombre.short_description = "Normalizar nombre (capitalizar y limpiar)"


def marcar_mascotas_adultas(modeladmin, request, queryset):
    queryset.update(notas="Mascota marcada como adulta desde el panel admin")


marcar_mascotas_adultas.short_description = "Marcar mascotas como adultas (nota automática)"


def limpiar_imagen_mascota(modeladmin, request, queryset):
    for mascota in queryset:
        mascota.imagen = None
        mascota.save()


limpiar_imagen_mascota.short_description = "Eliminar imagen de mascota"


def agregar_nota_revision(modeladmin, request, queryset):
    for mascota in queryset:
        texto = mascota.notas or ""
        mascota.notas = f"{texto}\nRevisado desde el panel admin."
        mascota.save()


agregar_nota_revision.short_description = "Agregar nota de revisión"


class EspecieAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Datos de la Especie", {"fields": [
         "nombre"]}),
    ]
    list_display = ["nombre"]
    ordering = ["-nombre"]


class MascotaAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Datos de la Mascota", {"fields": [
         "nombre", "raza", "especie", "sexo", "edad", "imagen"]}),
        ("Datos de la Consulta", {"fields": [
         "notas", "fecha_alta"]}),
        ("Dueño", {"fields": ["cliente"]}),
    ]
    list_display = ["nombre", "especie", "raza",
                    "sexo", "edad", "fecha_alta", "cliente"]
    ordering = ["-fecha_alta"]
    list_filter = ["especie", "sexo"]

    actions = [
        marcar_mascotas_adultas,
        limpiar_imagen_mascota,
        agregar_nota_revision
    ]


class RazaAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Datos de la Raza", {"fields": [
         "nombre", "especie"]}),
    ]
    list_display = ["nombre", "especie"]
    ordering = ["-especie"]

    actions = [normalizar_nombre]


admin.site.register(Especie, EspecieAdmin)
admin.site.register(Mascota, MascotaAdmin)
admin.site.register(Raza, RazaAdmin)

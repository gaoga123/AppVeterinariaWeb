from django.contrib import admin
from django.utils.timezone import now

from .models import Cliente, Profesional, Rol

# Register your models here.


def actualizar_fecha_registro(modeladmin, request, queryset):
    queryset.update(fecha_registro=now())


actualizar_fecha_registro.short_description = "Actualizar fecha de registro a HOY"


def asignar_rol_veterinario(modeladmin, request, queryset):
    rol_veterinario = Rol.objects.get(nombre="Veterinario")
    queryset.update(rol=rol_veterinario)


asignar_rol_veterinario.short_description = "Asignar rol VETERINARIO"


def normalizar_roles(modeladmin, request, queryset):
    for rol in queryset:
        rol.nombre = rol.nombre.capitalize()
        rol.save()


normalizar_roles.short_description = "Normalizar nombres de roles"


class ClienteAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Usuario asociado al Dueño", {"fields": [
         "user"]}),
        ("Datos del Dueño", {"fields": ["fecha_registro"]}),
    ]
    list_display = ["user", "fecha_registro"]
    ordering = ["-fecha_registro"]
    actions = [actualizar_fecha_registro]


class ProfesionalAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Datos del Profesional", {"fields": [
         "nombre", "apellido", "email", "rol", "fecha_alta"]}),
    ]
    list_display = ["nombre", "apellido", "email", "rol"]
    ordering = ["-fecha_alta"]
    list_filter = ["rol"]
    actions = [asignar_rol_veterinario]


class RolAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Datos del Rol", {"fields": [
         "nombre"]}),
    ]
    list_display = ["nombre"]
    ordering = ["-nombre"]
    actions = [normalizar_roles]


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Profesional, ProfesionalAdmin)
admin.site.register(Rol, RolAdmin)

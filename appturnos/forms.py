from django import forms
from django.core.exceptions import ValidationError
from django.utils.timezone import now

from appmascotas.models import Mascota

from .models import Cita


class CitaForm(forms.ModelForm):

    class Meta:
        model = Cita
        fields = ["mascota", "veterinario", "fecha", "motivo"]
        exclude = ["estado"]

        widgets = {

            "mascota": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "veterinario": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "fecha": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "class": "form-control",
                },
                format="%Y-%m-%dT%H:%M"
            ),

            "motivo": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Motivo de la consulta"
                }
            ),

        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        if user and hasattr(user, "cliente"):
            self.fields["mascota"].queryset = Mascota.objects.filter(
                cliente=user.cliente
            )
        else:
            self.fields["mascota"].queryset = Mascota.objects.none()

    def clean_fecha(self):
        fecha = self.cleaned_data.get("fecha")

        if fecha and fecha < now():
            raise ValidationError("No se puede seleccionar una fecha pasada.")

        return fecha

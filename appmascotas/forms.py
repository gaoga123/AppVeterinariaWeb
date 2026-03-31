from django import forms

from .models import Mascota, Raza


class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota
        fields = ["especie", "raza", "nombre", "sexo", "edad", "imagen"]
        exclude = ["cliente"]

        widgets = {
            "especie": forms.Select(
                attrs={
                    "class": "form-select",
                    "onchange": "this.form.submit();"
                }
            ),

            "raza": forms.Select(
                attrs={"class": "form-select"}
            ),

            "sexo": forms.Select(
                attrs={"class": "form-select"}
            ),

            "nombre": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "edad": forms.NumberInput(
                attrs={"class": "form-control"}
            ),

            "imagen": forms.ClearableFileInput(
                attrs={"class": "form-control"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["raza"].queryset = Raza.objects.none()

        if "especie" in self.data:
            try:
                especie_id = int(self.data.get("especie"))
                self.fields["raza"].queryset = Raza.objects.filter(
                    especie_id=especie_id
                ).order_by("nombre")
            except (ValueError, TypeError):
                pass

        elif self.instance.pk and self.instance.especie:
            self.fields["raza"].queryset = Raza.objects.filter(
                especie=self.instance.especie
            )

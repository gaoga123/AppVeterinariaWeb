from django import forms

from .models import Resenia


class ReseniaForm(forms.ModelForm):

    class Meta:
        model = Resenia
        fields = ["puntuacion", "comentarios"]

        widgets = {
            "puntuacion": forms.Select(
                attrs={"class": "form-select"}
            ),
            "comentarios": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Escribe tu reseña...",
                    "maxlength": 300
                }
            ),
        }

    def clean_comentarios(self):
        data = self.cleaned_data.get("comentarios", "")
        return data.strip()

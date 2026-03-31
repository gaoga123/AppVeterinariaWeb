from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from appturnos.models import EstadoCita

from .forms import CitaForm
from .models import Cita

# Create your views here.


class CitaCreateView(FormView):
    template_name = "appturnos/citas.html"
    form_class = CitaForm
    success_url = reverse_lazy("cita_creada")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        estado_pendiente, _ = EstadoCita.objects.get_or_create(
            nombre="Pendiente")
        cita = form.save(commit=False)
        cita.estado = estado_pendiente
        cita.save()
        return super().form_valid(form)


def cita_creada(request):
    params = {}
    citas = (
        Cita.objects
        .filter(mascota__cliente=request.user.cliente)
        .select_related("mascota", "mascota__cliente", "veterinario", "estado")
        .order_by("-fecha")[:4]
    )
    params['citas'] = citas
    return render(request, 'appturnos/cita_creada.html', params)

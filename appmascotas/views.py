from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .forms import MascotaForm
from .models import Mascota


class MascotaCreateView(FormView):
    template_name = "appmascotas/mascotas.html"
    form_class = MascotaForm
    success_url = reverse_lazy("mascota_creada")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        mascota = form.save(commit=False)
        mascota.cliente = self.request.user.cliente
        mascota.save()
        return super().form_valid(form)


@login_required
def opciones_mascotas(request):
    return render(request, 'appmascotas/opciones_mascotas.html')


@login_required
def buscar_mascotas(request):
    return render(request, 'appmascotas/buscar_mascotas.html')


@login_required
def mascota_creada(request):
    mascotas = (
        Mascota.objects
        .filter(cliente=request.user.cliente)
        .select_related("especie", "raza")
        .only("id", "nombre", "edad", "especie__nombre", "raza__nombre")
    )

    return render(request, 'appmascotas/mascota_creada.html', {
        'mascotas': mascotas
    })


@login_required
def buscar_mascotas_ajax(request):
    query = request.GET.get("q", "").strip()

    mascotas = (
        Mascota.objects
        .filter(
            cliente=request.user.cliente,
            nombre__icontains=query
        )
        .select_related("especie", "raza")
        .only("id", "nombre", "edad", "especie__nombre", "raza__nombre")
        .order_by("nombre")[:10]
    )

    data = [
        {
            "id": m.id,
            "nombre": m.nombre,
            "especie": m.especie.nombre if m.especie else "",
            "raza": m.raza.nombre if m.raza else "",
            "edad": m.edad
        }
        for m in mascotas
    ]

    return JsonResponse(data, safe=False)

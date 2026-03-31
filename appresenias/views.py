from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .forms import ReseniaForm
from .models import Resenia


class ReseniaCreateView(FormView):
    template_name = "appresenias/resenias.html"
    form_class = ReseniaForm
    success_url = reverse_lazy("resenia_creada")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        resenia = form.save(commit=False)
        resenia.cliente = self.request.user.cliente
        resenia.save()
        return super().form_valid(form)


@login_required
def resenia(request):
    resenias = (
        Resenia.objects
        .select_related("cliente__user")
        .only("id", "puntuacion", "comentarios", "fecha", "cliente__user__username")
        .order_by("-fecha")
    )

    return render(request, 'appresenias/resenias.html', {
        'nombre_sitio': 'Veterinaria Web',
        'resenias': resenias
    })


@login_required
def resenia_creada(request):
    resenia = (
        Resenia.objects
        .filter(cliente=request.user.cliente)
        .select_related("cliente__user")
        .order_by("-id")
        .first()
    )

    return render(request, 'appresenias/resenia_creada.html', {
        'nombre_sitio': 'Veterinaria Web',
        'resenias': resenia
    })

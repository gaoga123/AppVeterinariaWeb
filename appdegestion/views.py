from django.shortcuts import render
from django.views.decorators.cache import cache_page

from appmascotas.models import Mascota
from appresenias.models import Resenia


def terminos(request):
    return render(request, 'appdegestion/terminos.html')


def privacidad(request):
    return render(request, 'appdegestion/privacidad.html')


@cache_page(60 * 10)
def index(request):
    mascotas = Mascota.objects.only(
        "nombre", "especie", "edad", "imagen")[:10]
    resenias = Resenia.objects.only(
        "cliente", "puntuacion", "comentarios")[:10]

    return render(request, 'appdegestion/index.html', {
        'mascotas': mascotas,
        'resenias': resenias
    })


def panel(request):
    if request.user.is_authenticated:
        return render(request, 'appdegestion/panel.html')
    else:
        mascotas = Mascota.objects.only(
            "nombre", "especie", "edad", "imagen")[:10]
        resenias = Resenia.objects.only(
            "cliente", "puntuacion", "comentarios")[:10]
        return render(request, 'appdegestion/index.html', {
            'mascotas': mascotas,
            'resenias': resenias
        })

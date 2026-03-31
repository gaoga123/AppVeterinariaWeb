import json

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from appfacturacion.utils import crear_factura_desde_pedido
from appinventario.models import Producto

from .models import DetallePedido, Pedido

# Create your views here.


def carrito(request):
    productos = Producto.objects.filter(stock__gt=0)
    context = {
        "productos": productos
    }
    return render(request, 'appcarrito/carrito.html', context)


@login_required
@csrf_exempt
def checkout(request):

    if request.method == "POST":

        data = json.loads(request.body)
        carrito = data.get("carrito", [])

        if not carrito:
            return JsonResponse({"success": False, "error": "Carrito vacío"})

        try:
            with transaction.atomic():

                ids = [int(item["id"]) for item in carrito]

                productos = Producto.objects.select_for_update().filter(id__in=ids)
                productos_dict = {p.id: p for p in productos}

                total = 0
                detalles = []

                pedido = Pedido.objects.create(
                    cliente=request.user,
                    total=0
                )

                for item in carrito:

                    producto = productos_dict.get(int(item["id"]))
                    cantidad = int(item["cantidad"])

                    if not producto:
                        raise Exception("Producto no encontrado")

                    if producto.stock < cantidad:
                        raise Exception(
                            f"No hay stock suficiente para {producto.nombre}"
                        )

                    subtotal = producto.precio * cantidad
                    total += subtotal

                    detalles.append(
                        DetallePedido(
                            pedido=pedido,
                            producto=producto,
                            cantidad=cantidad,
                            precio=producto.precio,
                            subtotal=subtotal
                        )
                    )

                    Producto.objects.filter(id=producto.id).update(
                        stock=F("stock") - cantidad
                    )

                DetallePedido.objects.bulk_create(detalles)

                pedido.total = total
                pedido.save()

                crear_factura_desde_pedido(pedido)

                return JsonResponse({
                                    "success": True,
                                    "redirect_url": "/compras/pedido-creado/"
                                    })

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})


@login_required
def pedido_creado(request):
    pedido = (
        Pedido.objects
        .filter(cliente=request.user)
        .prefetch_related("detalles__producto")
        .order_by("-id")
        .first()
    )

    return render(request, "appcarrito/pedido_creado.html", {
        "pedido": pedido
    })

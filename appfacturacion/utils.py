from django.utils import timezone

from .models import DetalleFactura, Factura


def generar_numero_factura():
    ultima = Factura.objects.order_by("-id").first()

    if ultima:
        numero = int(ultima.numero.split("-")[-1]) + 1
    else:
        numero = 1

    return f"FAC-{numero:08d}"


def crear_factura_desde_pedido(pedido):

    factura = Factura.objects.create(
        cliente=pedido.cliente.cliente,
        pedido=pedido,
        numero=generar_numero_factura(),
        fecha=timezone.now(),
        total=0,
        metodo_pago="efectivo",
        estado="pagada"
    )

    total = 0

    for detalle in pedido.detalles.all():

        subtotal = detalle.precio * detalle.cantidad
        total += subtotal

        DetalleFactura.objects.create(
            factura=factura,
            producto=detalle.producto,
            cantidad=detalle.cantidad,
            precio_unitario=detalle.precio,
            subtotal=subtotal
        )

    factura.total = total
    factura.save()

    return factura

from django.contrib.auth.models import User
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Cliente


@receiver(post_save, sender=User)
def crear_cliente_para_usuario(sender, instance, created, **kwargs):

    if not created:
        return

    with transaction.atomic():
        Cliente.objects.get_or_create(user=instance)

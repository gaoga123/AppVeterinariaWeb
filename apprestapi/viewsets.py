from rest_framework import viewsets

from .models import ReseniaRestApi
from .serializer import ReseniaRestApiSerializer


class ReseniaRestApiViewSet(viewsets.ModelViewSet):
    queryset = ReseniaRestApi.objects.all()
    serializer_class = ReseniaRestApiSerializer

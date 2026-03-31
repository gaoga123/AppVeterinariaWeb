from rest_framework import serializers

from .models import ReseniaRestApi


class ReseniaRestApiSerializer (serializers.ModelSerializer):
    class Meta:
        model = ReseniaRestApi
        fields = "__all__"

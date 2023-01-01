from rest_framework import serializers
from .models import Avaliacao


class AvaliacaoSerializer(serializers.Serializer):
    class Meta:
        model = Avaliacao
        fields = [
            "usuario",
            "comentario",
            "nota",
            "data",
        ]

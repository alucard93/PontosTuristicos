from rest_framework import serializers
from .models import Comentario


class ComentarioSerializer(serializers.Serializer):
    class Meta:
        model = Comentario
        fields = [
            "usuario",
            "comentario",
            "data",
            "aprovado",
        ]

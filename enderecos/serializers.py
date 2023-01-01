from rest_framework import serializers
from .models import Endereco


class EnderecoSerializer(serializers.Serializer):
    class Meta:
        model = Endereco
        fields = [
            "linha1",
            "linha2",
            "cidade",
            "estado",
            "pais",
            "latitude",
            "longitude",
        ]

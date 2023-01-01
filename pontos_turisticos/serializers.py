from rest_framework import serializers
from .models import PontoTuristico


class PontoTuristicoSerializer(serializers.Serializer):
    class Meta:
        model = PontoTuristico
        fields = [
            "id",
            "nome",
            "descrição",
        ]

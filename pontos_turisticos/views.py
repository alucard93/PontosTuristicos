from django.shortcuts import render

from pontos_turisticos.serializers import PontoTuristicoSerializer
from .models import PontoTuristico
from rest_framework.filters import SearchFilter

from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

class PontoTuristicoView(generics.ListCreateAPIView):
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao','endereco__linha1')
    lookup_field ='nome' #caso eu queira mudar o padrão que é id com isso a busca vai vira nome por padrão
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)
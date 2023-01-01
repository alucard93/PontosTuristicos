from django.shortcuts import render
from rest_framework import generics
from .models import Avaliacao

from avaliacoes.serializers import AvaliacaoSerializer

class AvaliacoesView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

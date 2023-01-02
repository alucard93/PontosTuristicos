from django.shortcuts import render
from rest_framework import generics
from .models import Atracao


from atracoes.serializers import AtracaoSerializer

class AtracoesView(generics.ListCreateAPIView):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_fields = ('nome', 'descricao') # FILTRO USANDO OS 2 ATRIBUTOS
    

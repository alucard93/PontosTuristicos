from django.shortcuts import render
from rest_framework import generics
from .models import Endereco

from enderecos.serializers import EnderecoSerializer

class EnderecosView(generics.ListCreateAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

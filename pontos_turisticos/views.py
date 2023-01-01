from django.shortcuts import render

from pontos_turisticos.serializers import PontoTuristicoSerializer
from .models import PontoTuristico

from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

class PontoTuristicoView(generics.ListCreateAPIView):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer



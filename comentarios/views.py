from django.shortcuts import render
from rest_framework import generics
from .models import Comentario

from comentarios.serializers import ComentarioSerializer

class ComentariosView(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

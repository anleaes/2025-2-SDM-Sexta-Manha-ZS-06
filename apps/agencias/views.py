from django.shortcuts import render
from .models import Agencia
from rest_framework import viewsets
from .serializer import AgenciaSerializer

# Create your views here.

class AgenciaViewSet(viewsets.ModelViewSet):
    queryset = Agencia.objects.all()
    serializer_class = AgenciaSerializer

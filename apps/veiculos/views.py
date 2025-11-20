from django.shortcuts import render
from rest_framework import viewsets
from .models import Veiculo
from .serializer import VeiculoSerializer

# Create your views here.

class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

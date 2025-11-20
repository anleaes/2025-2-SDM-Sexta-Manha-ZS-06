from django.shortcuts import render
from rest_framework import viewsets
from .models import Modelo
from .serializer import ModeloSerializer

# Create your views here.

class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer

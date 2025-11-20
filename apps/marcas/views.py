from django.shortcuts import render
from rest_framework import viewsets
from .models import Marca
from .serializer import MarcaSerializer

# Create your views here.

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer  
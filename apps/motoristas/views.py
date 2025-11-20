from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Motorista
from .serializer import MotoristaSerializer

# Create your views here.

class MotoristaViewSet(ModelViewSet):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer


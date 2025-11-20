from rest_framework import viewsets
from .models import ModoPagamento
from .serializer import ModoPagamentoSerializer

class ModoPagamentoViewSet(viewsets.ModelViewSet):
    queryset = ModoPagamento.objects.all()
    serializer_class = ModoPagamentoSerializer

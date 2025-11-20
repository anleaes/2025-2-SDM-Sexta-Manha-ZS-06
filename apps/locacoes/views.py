from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Locacao
from .serializer import LocacaoSerializer


class LocacaoViewSet(viewsets.ModelViewSet):
    queryset = Locacao.objects.all()
    serializer_class = LocacaoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'status',
        'cliente',
        'veiculo',
        'seguro_incluso',
        
    ]

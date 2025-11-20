from rest_framework import serializers
from .models import ModoPagamento

class ModoPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModoPagamento
        fields = [
            'id',
            'data_pagamento',
            'valor',
            'metodo',
            'status',
            'comprovante',
            'parcelado',
            'numero_parcelas',
        ]

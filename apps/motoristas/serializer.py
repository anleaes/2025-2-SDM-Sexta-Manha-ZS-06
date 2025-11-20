from rest_framework import serializers
from .models import Motorista

class MotoristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorista
        fields = [
            'id',
            'nome',
            'cnh',
            'data_validade_cnh',
            'categoria_cnh',
            'data_nascimento',
            'telefone',
            'email',
            'autenticado',
        ]

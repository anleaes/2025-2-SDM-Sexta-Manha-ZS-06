from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'id',
            'nome',
            'cpf',
            'data_nascimento',
            'endereco',
            'telefone',
            'email',
            'ativo',
        ]
from rest_framework import serializers
from .models import Locacao, MotoristaLocacao
from motoristas.models import Motorista

class MotoristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorista
        fields = ['id', 'nome', 'cnh']

class LocacaoSerializer(serializers.ModelSerializer):
    motoristas = MotoristaSerializer(many=True, read_only=True)
    motorista_ids = serializers.PrimaryKeyRelatedField(
        queryset=Motorista.objects.all(),
        many=True,
        write_only=True,
        required=False
    )

    class Meta:
        model = Locacao
        fields = [
            'id',
            'data_inicio',
            'data_fim',
            'valor_total',
            'status',
            'observacoes',
            'data_criacao',
            'seguro_incluso',
            'cliente',
            'pagamento',
            'veiculo',
            'motoristas',
            'motorista_ids',
        ]

    def create(self, validated_data):
        motorista_ids = validated_data.pop('motorista_ids', [])
        locacao = Locacao.objects.create(**validated_data)
        for motorista in motorista_ids:
            MotoristaLocacao.objects.create(locacao=locacao, motorista=motorista)
        locacao.calcular_valor_total()
        return locacao

    def update(self, instance, validated_data):
        motorista_ids = validated_data.pop('motorista_ids', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if motorista_ids is not None:
            instance.motoristas.clear()
            for motorista in motorista_ids:
                MotoristaLocacao.objects.create(locacao=instance, motorista=motorista)
        instance.calcular_valor_total()
        return instance
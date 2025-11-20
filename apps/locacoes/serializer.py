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

    valor_total = serializers.SerializerMethodField(read_only=True)

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
        read_only_fields = ['valor_total', 'data_criacao']

    def get_valor_total(self, obj):
        try:
            dias = (obj.data_fim - obj.data_inicio).days
            if dias < 1:
                dias = 1
            if obj.veiculo and hasattr(obj.veiculo, "valor_diaria"):
                return dias * obj.veiculo.valor_diaria
            return 0
        except:
            return 0

    def create(self, validated_data):
        motorista_ids = validated_data.pop('motorista_ids', [])
        locacao = Locacao.objects.create(**validated_data)
        for motorista in motorista_ids:
            MotoristaLocacao.objects.create(locacao=locacao, motorista=motorista)
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
        return instance

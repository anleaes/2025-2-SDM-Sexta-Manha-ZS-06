from django.db import models
from django.utils import timezone
from veiculos.models import Veiculo
from clientes.models import Cliente
from modopagamentos.models import ModoPagamento
from motoristas.models import Motorista


class Locacao(models.Model):
    STATUS_LOCACAO_CHOICES = [
        ('ativa', 'Ativa'),
        ('finalizada', 'Finalizada'),
        ('cancelada', 'Cancelada'),
        ('atrasada', 'Atrasada'),
    ]

    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_LOCACAO_CHOICES, default='ativa')
    observacoes = models.TextField(null=True, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    seguro_incluso = models.BooleanField(default=False)

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='locacoes')
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name='locacoes')
    pagamento = models.OneToOneField(ModoPagamento, on_delete=models.SET_NULL, null=True, blank=True, related_name='locacao')

    motoristas = models.ManyToManyField(Motorista, through='MotoristaLocacao', related_name='locacoes')

    def finalizar_locacao(self):
        self.status = 'finalizada'
        self.save()

    def renovar_locacao(self, nova_data_fim):
        self.data_fim = nova_data_fim
        self.save()

    def __str__(self):
        return f"Locação #{self.id} - {self.cliente.nome}"


class MotoristaLocacao(models.Model):
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    locacao = models.ForeignKey(Locacao, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.motorista.nome} - Locação #{self.locacao.id}"

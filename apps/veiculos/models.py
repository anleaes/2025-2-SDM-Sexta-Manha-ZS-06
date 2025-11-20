from django.db import models
from agencias.models import Agencia
from modelos.models import Modelo

# Create your models here.

class Veiculo(models.Model):
    placa = models.CharField('Placa', max_length=20)
    cor = models.CharField('Cor', max_length=30)
    ano = models.IntegerField('Ano')
    chassi = models.CharField('Chassi', max_length=50)
    renavam = models.CharField('Renavam', max_length=20)
    tipo_combustivel = models.CharField('Tipo de Combustível', max_length=30)
    numero_portas = models.IntegerField('Número de Portas')
    quilometragem = models.FloatField('Quilometragem')
    valor_diaria = models.FloatField('Valor da Diária')
    disponivel = models.BooleanField('Disponível', default=True)

    agencia = models.ForeignKey(
        Agencia,
        on_delete=models.CASCADE,
        related_name='veiculos'
    )

    modelo = models.ForeignKey(
        Modelo,
        on_delete=models.CASCADE,
        related_name='veiculos'
    )

    class Meta:
        verbose_name = "veículo"
        verbose_name_plural = "veículos"
        ordering = ['id']

    def __str__(self):
        return f"{self.placa} - {self.modelo}"
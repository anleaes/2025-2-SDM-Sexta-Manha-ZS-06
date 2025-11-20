from django.db import models
from marcas.models import Marca 

# Create your models here.

class Modelo(models.Model):
    nome = models.CharField('Nome', max_length=100)
    ano_lancamento = models.IntegerField('Ano de Lançamento', null=True, blank=True)
    categoria = models.CharField('Categoria', max_length=50)
    passageiros = models.IntegerField('Número de Passageiros', null=True, blank=True)
    tipo = models.CharField('Tipo', max_length=50, null=True, blank=True)  
    motor = models.CharField('Motor', max_length=50, null=True, blank=True)
    acessorios = models.TextField('Acessórios', blank=True, null=True)

    marca = models.ForeignKey(
        Marca,
        on_delete=models.CASCADE,
        related_name='modelos'
    )

    class Meta:
        verbose_name = 'modelo'
        verbose_name_plural = 'modelos'
        ordering = ['id']

    def __str__(self):
        return f"{self.nome} - {self.marca}"


    def listar_acessorios(self):
        if not self.acessorios:
            return []
        return [item.strip() for item in self.acessorios.split(',')]

    def verificar_categoria(self):
        return self.categoria
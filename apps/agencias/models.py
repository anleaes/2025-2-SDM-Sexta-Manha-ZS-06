from django.db import models

# Create your models here.

class Agencia(models.Model):
    nome = models.CharField('Nome', max_length=100)
    endereco = models.TextField('Endereço', max_length=200)
    telefone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('E-mail', max_length=100)
    horario_funcionamento = models.CharField('Horário de Funcionamento', max_length=100)
    capacidade_frota = models.IntegerField('Capacidade da Frota')
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        verbose_name = 'agência'
        verbose_name_plural = 'agências'
        ordering = ['id']

    def __str__(self):
        return f"{self.nome} - ({self.endereco})"

    def consultar_disponibilidade(self):
        pass

    def gerar_relatorio(self):
        pass
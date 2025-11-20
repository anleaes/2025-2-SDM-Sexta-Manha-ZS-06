from django.db import models
from datetime import date

# Create your models here.

class Motorista(models.Model):

    CATEGORIA_CNH_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('AB', 'AB'),
        ('AC', 'AC'),
        ('AD', 'AD'),
        ('AE', 'AE'),
    ]

    nome = models.CharField(max_length=100)
    cnh = models.CharField(max_length=20, unique=True)
    data_validade_cnh = models.DateField()
    categoria_cnh = models.CharField(max_length=5, choices=CATEGORIA_CNH_CHOICES)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    autenticado = models.BooleanField(default=False)

    def validar_cnh(self):
        return self.data_validade_cnh >= date.today()

    def atualizar_dados(self, **kwargs):
        for campo, valor in kwargs.items():
            setattr(self, campo, valor)
        self.save()

    def __str__(self):
        return f"{self.nome} - CNH {self.cnh}"

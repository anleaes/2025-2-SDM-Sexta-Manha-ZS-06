from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=150)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    data_nascimento = models.DateField('Data de Nascimento')
    endereco = models.CharField('Endereço', max_length=255)
    telefone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('E-mail', unique=True)
    ativo = models.BooleanField('Ativo', default=True)
from django.db import models

# Create your models here.

class Marca(models.Model):
    name = models.CharField('Nome', max_length=50)
    nacionalidade = models.CharField('Nacionalidade', max_length=50)
    ano_fundacao = models.IntegerField('Ano de Fundação')
    descricao = models.TextField('Descrição', max_length=500)
    ativo = models.BooleanField('Ativo', default=True)
    site_oficial = models.URLField('Site Oficial', max_length=200)
    logo_url = models.URLField('Logo URL', max_length=300)
from django.db import models

class Marca(models.Model):
    name = models.CharField('Nome', max_length=50)
    nacionalidade = models.CharField('Nacionalidade', max_length=50)
    ano_fundacao = models.IntegerField('Ano de Fundação')
    descricao = models.TextField('Descrição', max_length=500)
    ativo = models.BooleanField('Ativo', default=True)
    site_oficial = models.URLField('Site Oficial', max_length=200)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['id']

    def __str__(self):
        return self.name

    def consultar_site(self):
        return self.site_oficial

    def verificar_ativo(self):
        return "Marca ativa" if self.ativo else "Marca inativa"

from django.db import models

# Create your models here.

class ModoPagamento(models.Model):
    STATUS_PAGAMENTO_CHOICES = [
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('recusado', 'Recusado'),
        ('estornado', 'Estornado'),
    ]

    METODO_PAGAMENTO_CHOICES = [
        ('credito', 'Cartão de Crédito'),
        ('debito', 'Cartão de Débito'),
        ('pix', 'PIX'),
        ('dinheiro', 'Dinheiro'),
    ]

    data_pagamento = models.DateTimeField(null=True, blank=True)
    valor = models.FloatField()
    metodo = models.CharField(max_length=20, choices=METODO_PAGAMENTO_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_PAGAMENTO_CHOICES)
    comprovante = models.CharField(max_length=255, null=True, blank=True)
    parcelado = models.BooleanField(default=False)
    numero_parcelas = models.IntegerField(default=1)

    def registrar_pagamento(self):
        self.status = 'pago'
        self.save()

    def validar_comprovante(self):
        return bool(self.comprovante)

    def __str__(self):
        return f"Pagamento #{self.id} - {self.status}"
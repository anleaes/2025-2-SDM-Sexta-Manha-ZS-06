from django.db import models

# Create your models here.

class ModoPagamento(models.Model):
    STATUS_PAGAMENTO_CHOICES = [
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('recusado', 'Recusado'),
        ('estornado', 'Estornado'),
    ]
from django.db import models

import uuid


class Alvo(models.Model):
    identificador = models.UUIDField(verbose_name='UUID', default=uuid.uuid4, unique=True, primary_key=True)
    nome = models.CharField(max_length=30, verbose_name='Nome do Alvo')
    latitude = models.DecimalField(max_digits=10, decimal_places=6, verbose_name='Latitude', help_text='exemplo: 12.222200')
    longitude = models.DecimalField(max_digits=10, decimal_places=6, verbose_name='Longitude', help_text='exemplo: -12.222200')
    data_expiracao = models.DateField(null=True, verbose_name='Data da Expiracao', help_text='formato: YYYY-MM-DD')

    def __str__(self):
        return self.nome

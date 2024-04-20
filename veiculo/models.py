from django.db import models
from django.utils.translation import gettext_lazy as _

from core.basics.models.basic_models import BasicModel


class Veiculo(BasicModel):
    placa = models.CharField(verbose_name=_('Placa'), max_length=7)
    marca = models.CharField(verbose_name=_('Marca'), max_length=100)
    veiculo = models.TextField(verbose_name=_('Veículo'))
    km_troca_oleo = models.DecimalField(
        verbose_name=_('Quilometros até a próxima troca'), default=0, max_digits=10, decimal_places=2
    )

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'
        db_table = 'veiculo'

    def __str__(self):
        return f'{self.marca} - {self.placa}'

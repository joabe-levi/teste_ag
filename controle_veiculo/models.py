from django.db import models
from django.utils.translation import gettext_lazy as _

from controle_veiculo.business import ControleVeiculoBusiness
from core.basics.business.basic_business import BaseModelBusiness
from core.basics.models.basic_models import BasicModel


class ControleVeiculo(BaseModelBusiness, BasicModel):
    veiculo = models.ForeignKey(
        'veiculo.Veiculo', verbose_name=_('Veículo'), related_name='controles', on_delete=models.CASCADE
    )
    motorista = models.ForeignKey(
        'motorista.Motorista', verbose_name=_('Motorista'), related_name='controles', on_delete=models.CASCADE
    )

    data_saida = models.DateField(verbose_name=_('Data da saída'))
    hora_saida = models.TimeField(verbose_name=_('Hora da saída'))
    km_saida = models.DecimalField(verbose_name=_('Km da saída'), max_digits=10, decimal_places=2)

    destino = models.CharField(verbose_name=_('Destino'), max_length=300, null=True, blank=True)

    data_retorno = models.DateField(verbose_name=_('Data do retorno'), null=True, blank=True)
    hora_retorno = models.TimeField(verbose_name=_('Hora da chegada'), null=True, blank=True)
    km_retorno = models.DecimalField(
        verbose_name=_('Km da volta'), max_digits=10, decimal_places=2, null=True, blank=True
    )

    km_percorrido = models.DecimalField(
        verbose_name=_('Km percorridos'), max_digits=10, decimal_places=2, null=True, blank=True
    )

    business_class = ControleVeiculoBusiness

    class Meta:
        verbose_name = 'Controle do veículo'
        verbose_name_plural = 'Controle dos veículos'
        db_table = 'controle'

    def __str__(self):
        return f'{self.veiculo} - {self.motorista}'

    def save(self, *args, **kwargs):
        if not self.km_percorrido:
            if self.km_saida and self.km_retorno:
                self.km_percorrido = self.km_retorno - self.km_saida

        super().save(args, **kwargs)

from django.db import models
from django.utils.translation import gettext_lazy as _

from core.basics.models.basic_models import BasicModel


class Motorista(BasicModel):
    cod_motorista = models.CharField(verbose_name=_('Código do motorista'), max_length=50)
    nome = models.CharField(verbose_name=_('Nome'), max_length=300)
    telefone = models.CharField(verbose_name=_('Telefone'), max_length=300, null=True, blank=True)
    cnh = models.CharField(verbose_name=_('Carteira Nacional de Habilitação'), max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = 'Motorista'
        verbose_name_plural = 'Motoristas'
        db_table = 'motorista'

    def __str__(self):
        return f'{self.cod_motorista} - {self.nome}'

    @property
    def telefone_display(self):
        return f'({self.telefone[:2]}) {self.telefone[2:7]}-{self.telefone[7:]}'

from core.basics.filters.basic_filters import BasicFilter
from . import models


class VeiculoFilter(BasicFilter):

    class Meta:
        model = models.Veiculo
        fields = ('marca', 'placa', 'veiculo')
        search_fields = ('marca', '^placa', 'veiculo')

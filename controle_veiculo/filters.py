import django_filters

from controle_veiculo.models import ControleVeiculo
from core.basics.filters.basic_filters import BasicFilter


class ControleVeiculoFilter(BasicFilter):
    data = django_filters.DateFilter(method='get_data')

    class Meta:
        model = ControleVeiculo
        fields = ('data', 'veiculo__placa', 'veiculo__marca', 'motorista__nome')
        search_fields = ('veiculo__placa', 'veiculo__marca', 'motorista__nome', 'data')

    def get_data(self, queryset, name, value):
        if value:
            return queryset.filter(data_saida=value)
        return queryset

from core.basics.filters.basic_filters import BasicFilter
from motorista.models import Motorista


class MotoristaFilter(BasicFilter):
    class Meta:
        model = Motorista
        fields = ('cod_motorista', 'nome', 'telefone', 'cnh')
        search_fields = ('cod_motorista', 'nome', 'telefone', 'cnh')

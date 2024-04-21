from django.urls import reverse

from core.basics.views import basic_views
from motorista.filters import MotoristaFilter
from motorista.forms import MotoristaForm
from motorista.models import Motorista
from veiculo.forms import VeiculoForm
from veiculo.models import Veiculo


class MotoristaMixin:
    form_class = MotoristaForm
    title = 'Veículos'
    model = Motorista
    template_name = 'menu/base_form.html'

    def get_success_url(self):
        return reverse('motorista:detail', args=[self.object.id])


class MotoristaListView(MotoristaMixin, basic_views.BasicListView):
    filterset_class = MotoristaFilter
    template_name = 'motorista/list.html'


class MotoristaDetailView(MotoristaMixin, basic_views.BasicDetailView):
    template_name = 'motorista/detail.html'

    def get_title_detail(self):
        return f'Detalhes do motorista {self.object.nome}'


class MotoristaCreateView(MotoristaMixin, basic_views.BasicCreateView):
    pass


class MotoristaUpdateView(MotoristaMixin, basic_views.BasicUpdateView):
    pass


class MotoristaDeleteView(MotoristaMixin, basic_views.BasicDeleteView):
    pass

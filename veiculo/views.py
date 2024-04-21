from django.urls import reverse

from core.basics.views import basic_views
from core.basics.views.basic_alerts import BasicModelAlertViewMixin
from veiculo.alerts import VeiculoAlert
from veiculo.filters import VeiculoFilter
from veiculo.forms import VeiculoForm
from veiculo.models import Veiculo


class VeiculoMixin:
    form_class = VeiculoForm
    title = 'Veículos'
    model = Veiculo
    template_name = 'menu/base_form.html'

    def get_success_url(self):
        return reverse('veiculo:detail', args=[self.object.id])


class VeiculoListView(VeiculoMixin, basic_views.BasicListView):
    filterset_class = VeiculoFilter
    template_name = 'veiculo/list.html'


class VeiculoDetailView(VeiculoMixin, BasicModelAlertViewMixin, basic_views.BasicDetailView):
    alert_class = VeiculoAlert
    template_name = 'veiculo/detail.html'

    def get_title_detail(self):
        return f'Detalhes do veículo {self.object.veiculo}'


class VeiculoCreateView(VeiculoMixin, basic_views.BasicCreateView):
    pass


class VeiculoUpdateView(VeiculoMixin, basic_views.BasicUpdateView):
    pass


class VeiculoDeleteView(VeiculoMixin, basic_views.BasicDeleteView):
    pass

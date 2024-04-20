from django.urls import reverse

from controle_veiculo.filters import ControleVeiculoFilter
from controle_veiculo.forms import ControleForm
from controle_veiculo.models import ControleVeiculo
from core.basics.views import basic_views


class ControleVeiculoMixin:
    form_class = ControleForm
    title = 'Controles dos Veículos'
    model = ControleVeiculo
    template_name = 'menu/base_form.html'

    def get_success_url(self):
        return reverse('controle-veiculo:detail', args=[self.object.id])


class ControleVeiculoListView(ControleVeiculoMixin, basic_views.BasicListView):
    template_name = 'controle_veiculo/list.html'
    filterset_class = ControleVeiculoFilter

    def get_queryset(self):
        return ControleVeiculo.objects.select_related('veiculo', 'motorista').order_by('-data_saida')


class ControleVeiculoDetailView(ControleVeiculoMixin, basic_views.BasicDetailView):
    template_name = 'controle_veiculo/detail.html'

    def get_title_detail(self):
        return f'Detalhes do veículo {self.object.veiculo}'


class ControleVeiculoCreateView(ControleVeiculoMixin, basic_views.BasicCreateView):

    def do_create(self, form):
        super().do_create(form)
        self.object.business.atualizar_km_ate_proxima_troca()


class ControleVeiculoUpdateView(ControleVeiculoMixin, basic_views.BasicUpdateView):

    def do_update(self, form):
        super().do_update(form)
        self.object.business.atualizar_km_ate_proxima_troca()


class ControleVeiculoDeleteView(ControleVeiculoMixin, basic_views.BasicDeleteView):
    template_name = ''

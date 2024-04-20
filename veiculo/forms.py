from django.forms import ModelForm, forms

from veiculo.models import Veiculo


class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = ('placa', 'marca', 'veiculo', 'km_troca_oleo')

    def clean_placa(self):
        placa = self.cleaned_data.get('placa')
        veiculos = Veiculo.objects.filter(placa=placa)

        if veiculos.exists():
            raise forms.ValidationError('Já existem veículos cadastrados com essa mesma placa.')

        return placa

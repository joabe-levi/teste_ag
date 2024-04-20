from django.forms import ModelForm
from django import forms

from .models import ControleVeiculo


class ControleForm(ModelForm):

    class Meta:
        model = ControleVeiculo
        fields = (
            'veiculo', 'motorista', 'data_saida', 'hora_saida', 'km_saida', 'destino', 'data_retorno', 'hora_retorno',
            'km_retorno', 'km_percorrido'
        )

        widgets = {
            'data_saida': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'}),
            'hora_saida': forms.TimeInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'time'}),

            'data_retorno': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'}),
            'hora_retorno': forms.TimeInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'time'}),
        }

    def clean_km_retorno(self):
        km_retorno = self.cleaned_data.get('km_retorno')
        km_saida = self.cleaned_data.get('km_saida')

        if km_retorno < km_saida:
            raise forms.ValidationError('Km de retorno não pode ser menor que o da saída.')

        return km_retorno

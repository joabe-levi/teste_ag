from django.forms import ModelForm, forms

from motorista.models import Motorista


class MotoristaForm(ModelForm):
    class Meta:
        model = Motorista
        fields = ('cod_motorista', 'nome', 'telefone', 'cnh',)

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')

        if not telefone.isnumeric():
            raise forms.ValidationError('Informe apenas números ao telefone.')

        if len(telefone) != 11:
            raise forms.ValidationError('Número de telefone inválido')

        return telefone

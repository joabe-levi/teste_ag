
class ControleVeiculoBusiness:

    def __init__(self, object):
        self.object = object

    @property
    def controle_veiculo(self):
        return self.object

    def atualizar_km_ate_proxima_troca(self):
        self.controle_veiculo.veiculo.km_troca_oleo -= self.controle_veiculo.km_percorrido
        self.controle_veiculo.veiculo.save()

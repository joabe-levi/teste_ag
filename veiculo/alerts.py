from core.basics.alerts.basic_model_alerts import BasicAlert


class VeiculoAlert(BasicAlert):
    alerts = ['proxima_troca_oleo']

    def alert_proxima_troca_oleo(self):
        if self.object.km_troca_oleo <= 0:
            return 'É necessário que o veiculo faça a troca de óleo', 'danger'

        if self.object.km_troca_oleo < 100:
            return 'Veículo com a quilometragem próxima da necessidade de troca de óleo.', 'warning'

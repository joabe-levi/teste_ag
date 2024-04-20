class BasicAlert:

    alerts = []

    def __init__(self, object):
        self.object = object
        self.alerts_sends = []
        self._clean_alerts()

    def _clean_alerts(self):
        for alert in self.alerts:
            if hasattr(self, 'alert_%s' % alert):
                method_alert = getattr(self, 'alert_%s' % alert)()
                self.alerts_sends.append(method_alert)

    @property
    def count_alerts(self):
        return len(self.alerts_sends)

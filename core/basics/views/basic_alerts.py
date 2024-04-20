
class BasicModelAlertViewMixin:

    alert_class = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['basic_alerts'] = self.alert_class(self.get_alert_object())
        return context

    def get_alert_object(self):
        if hasattr(self, 'object'):
            return self.object

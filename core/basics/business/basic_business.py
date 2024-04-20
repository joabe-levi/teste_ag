
class BaseModelBusiness:
    _business = None
    business_class = None

    def get_model_business_class(self, object):
        return self.business_class(object)

    @property
    def business(self):
        if not self._business:
            self._business = self.get_model_business_class(self)
        return self._business

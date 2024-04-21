from django.contrib import admin

from core.basics.admins.basic_admins import BasicAdmin
from veiculo.models import Veiculo


@admin.register(Veiculo)
class VeiculoAdmin(BasicAdmin):
    pass

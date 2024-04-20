from django.contrib import admin

from controle_veiculo.models import ControleVeiculo
from core.basics.admins.basic_admins import BasicAdmin


@admin.register(ControleVeiculo)
class ControleVeiculoAdmin(BasicAdmin):
    pass

from django.contrib import admin

from core.basics.admins.basic_admins import BasicAdmin
from motorista.models import Motorista


@admin.register(Motorista)
class MotoristaAdmin(BasicAdmin):
    pass

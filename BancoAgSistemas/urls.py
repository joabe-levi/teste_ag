from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),

    path('veiculos/', include('veiculo.urls')),
    path('motoristas/', include('motorista.urls')),
    path('controle_veiculos/', include('controle_veiculo.urls')),
]

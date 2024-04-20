from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
from django.urls import path

app_name = 'controle-veiculo'

urlpatterns = [
      path('', views.ControleVeiculoListView.as_view(), name='list'),
      path('detalhes/<int:pk>/', views.ControleVeiculoDetailView.as_view(), name='detail'),
      path('incluir/', views.ControleVeiculoCreateView.as_view(), name='create'),
      path('atualizar/<int:pk>/', views.ControleVeiculoUpdateView.as_view(), name='update'),
      path('excluir/<int:pk>/', views.ControleVeiculoDeleteView.as_view(), name='delete'),
] + staticfiles_urlpatterns()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
from django.urls import path

app_name = 'veiculo'

urlpatterns = [
      path('', views.VeiculoListView.as_view(), name='list'),
      path('detalhes/<int:pk>/', views.VeiculoDetailView.as_view(), name='detail'),
      path('incluir/', views.VeiculoCreateView.as_view(), name='create'),
      path('atualizar/<int:pk>/', views.VeiculoUpdateView.as_view(), name='update'),
      path('excluir/<int:pk>/', views.VeiculoDeleteView.as_view(), name='delete'),
] + staticfiles_urlpatterns()

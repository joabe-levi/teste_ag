from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
from django.urls import path

app_name = 'motorista'


urlpatterns = [
      path('', views.MotoristaListView.as_view(), name='list'),
      path('detalhes/<int:pk>/', views.MotoristaDetailView.as_view(), name='detail'),
      path('incluir/', views.MotoristaCreateView.as_view(), name='create'),
      path('atualizar/<int:pk>/', views.MotoristaUpdateView.as_view(), name='update'),
      path('excluir/<int:pk>/', views.MotoristaDeleteView.as_view(), name='delete'),
] + staticfiles_urlpatterns()

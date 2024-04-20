from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
from django.urls import path

app_name = 'core'

urlpatterns = [
      path('', views.ClassIndexView.as_view(), name='index'),
] + staticfiles_urlpatterns()

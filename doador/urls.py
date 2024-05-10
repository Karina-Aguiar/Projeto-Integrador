from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro', views.doador, name = "doador"),
    path('resposta-cadastro', views.doadorResponse, name = "resposta-cadastro")

]

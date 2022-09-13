from django.contrib import admin
from django.urls import path
from acomodacoes.views import listar_acomodacoes, detalhe

urlpatterns = [
    path('', listar_acomodacoes),
    path('detalhe/<int:acomodacao_id>/', detalhe),
]

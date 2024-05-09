from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('clientes/', views.clientes_list, name = 'clientes_list'),
    path('crearCliente/', csrf_exempt(views.crear_cliente),name='userCreate'),
]
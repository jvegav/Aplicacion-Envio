from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('crearCliente/', csrf_exempt(views.crear_cliente),name='userCreate'),
]
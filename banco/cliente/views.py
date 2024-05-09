import requests
from django.shortcuts import render

from .forms import ClienteForm

from .logic.cliente_logic import *

import json

# Create your views here.
def crear_cliente(request):
    if request.method =='POST':
        form =  ClienteForm(request.POST)
        if form.is_valid():
            # Crear llave publica y privada
            llave_publica, llaveprivada = generate_key_pair()
            # Sacar datos de el form
            data_form = form.cleaned_data
            # Cifrar uno por uno
            # Cifrado nombre
            nombre = data_form.get('nombre')
            nombreCifrado = encrypt_message(llaveprivada,nombre)
            # Cifrado documento
            documento = data_form.get('documento')
            documentoCifrado = encrypt_message(llaveprivada,documento)
            # Cifrado celular
            celular = data_form.get('celular')
            celularCifrado = encrypt_message(llaveprivada,celular)
            # Cifrado email
            email = data_form.get('email')
            emailCifrado = encrypt_message(llaveprivada,email)

            # HASH CIFRADO DE TODOS
            data_completa = nombre + documento +celular + email
            # Hacer hash de estos
            data_completa_hash = calculate_hash(data_completa)
            

            # serializamos el form
            serialized_form = json.loads(json.dumps(form.cleaned_data))


            # CREAR RESPUESTA
            data_cifrada = {
                'nombre': nombreCifrado,
                'documento': documentoCifrado,
                'celular': celularCifrado,
                'email': emailCifrado,
                'llave_publica': llaveprivada,
                'hash':data_completa_hash,
                'form' :serialized_form
            }
            print(nombreCifrado)
            response = requests.post('http://localhost:8001/verificar/', data=data_cifrada)
            if response.status_code == 200:
                response_data = response.json()
                message = response_data.get('message')
                print(message)
            else:
                print("Comunicacion rara")
        else:
            print(form.errors)
    else:
        form = ClienteForm()

    context ={
        'form': form,
    }

    return render(request, "Cliente/crearCliente.html", context)

    
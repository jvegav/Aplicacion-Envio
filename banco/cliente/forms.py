from django import forms

from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre',
            'documento',
            'celular',
            'email'
        ]

        labels = {
            'nombre' : 'Nombre',
            'documento' : 'Numero De Documento',
            'celular' : 'Numero De Celular',
            'email' : 'Correo',

        }
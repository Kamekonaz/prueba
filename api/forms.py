from django import forms
from django.forms import ModelForm
from api.models import Venta


class Ventaform(ModelForm):
    class Meta:
        model = Venta
        fields = ['nombre','correo','telefono','cantidad','direccion','tipo','comentario']

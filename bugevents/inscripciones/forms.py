from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Paquete


'''
PaqueteForm -> Creacion, modificacion y validacion de Paquetes
Clase relacionada -> CD18 [Control]
Casos de Uso relacionados -> {BE15, BE16}
'''
class PaqueteForm(ModelForm):
    class Meta:
        model = Paquete
        fields = '__all__'

    def clean(self):
        precio_base = self.cleaned_data.get('precio_base')
        if precio_base < 0:
            raise ValidationError("El valor del precio base debe ser un número no negativo")

from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Paquete, Promocion


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

"""
Promoción ->creación, modificación de promociones
clase relacionada ->CD08 [control]
caso de Uso relacionado -> {BE17, BE18}
"""
class PromocionForm(ModelForm):
    class Meta:
        model =Promocion
        fields='__all__'
        
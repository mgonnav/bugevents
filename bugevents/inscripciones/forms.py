from django.forms import ModelForm, TextInput
from django.core.exceptions import ValidationError

from .models import Paquete, Promocion

'''
Código: INS03
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
            raise ValidationError("El valor del precio base debe ser un número no negativo.")

"""
Código: INS04
Promoción ->creación, modificación de promociones
clase relacionada ->CD08 [control]
caso de Uso relacionado -> {BE17, BE18}
"""
class PromocionForm(ModelForm):
    class Meta:
        model = Promocion
        fields = '__all__'
        widgets = {
            'porcentaje_descuento': TextInput(attrs={"type": "number",
                                                     "min": "0",
                                                     "max": "100"})
        }

    def clean(self):
        descuento = self.cleaned_data.get('porcentaje_descuento')
        if descuento < 0 or descuento > 100:
            raise ValidationError("El valor del descuento debe ser un número de 0 a 100.")
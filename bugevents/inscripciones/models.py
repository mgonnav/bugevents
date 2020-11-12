from django.db import models
from configuracion.models import Actividad


'''
Paquete -> Entidad del sistema
Clase relacionada -> CD17 [Entity]
'''
class Paquete(models.Model):
    nombre = models.CharField(max_length=20)
    precio_base = models.FloatField()
    actividades = models.ManyToManyField(Actividad)

""" 
Promocion -> Entidad del sistema
clase relacionada -> CD07 [Entity]
"""
class Promocion(models.Model):
    nombre = models.CharField(max_length=50)
    porcentaje_descuento = models.FloatField()
    categoria = models.CharField(max_length=15)
    paquete = models.ForeignKey(Paquete,  on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Promociones"

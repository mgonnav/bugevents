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

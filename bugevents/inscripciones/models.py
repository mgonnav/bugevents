from django.db import models
from configuracion.models import Actividad

'''
Código: {INS05, INS06, INS07,INS08, INS09}
Paquete -> Entidad del sistema
Modelo Relacional -> MR11
Clase relacionada -> CD17 [Entity]
'''
class Paquete(models.Model):
    nombre = models.CharField(max_length=20)
    precio_base = models.FloatField()
    actividades = models.ManyToManyField(Actividad)

    def __str__(self):
        return f"{self.nombre} a {self.precio_base} soles."


'''
'''
class TipoParticipante(models.Model):
    nombre_tipo=models.CharField(max_length=20)
    
    class Meta:
        verbose_name = "Tipo de Participante"
        verbose_name_plural = "Tipo de Participantes"
        
    def __str__(self):
        return f"{self.nombre_tipo}"
  
'''
Código: {INS04, INS08, INS09}
Promocion -> Entidad del sistema
Modelo Relacional -> MR16
clase relacionada -> CD07 [Entity]
'''
class Promocion(models.Model):
    nombre = models.CharField(max_length=50)
    porcentaje_descuento = models.FloatField(default=0)
    tipo_participante = models.ForeignKey(TipoParticipante, on_delete=models.CASCADE, default=0)
    paquete = models.ForeignKey(Paquete,  on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Promociones"

    def __str__(self):
        return f"{self.nombre} para {self.paquete}"


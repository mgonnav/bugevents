from django.db import models
from django.utils import timezone

'''
Código: CFG03
Ambiente -> Entidad del sistema
Clase relacionada -> CD24 [Entity]
Modelo Relacional -> MR07
'''
class Ambiente(models.Model):
    nombre = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=50)
    aforo = models.IntegerField(default=40)

    def __str__(self):
        return f"{self.nombre}: Sala {self.ubicacion} con un aforo de {self.aforo} personas."


def one_day_hence():
    return timezone.now() + timezone.timedelta(days=1)

'''
Código: {CFG02, CFG04}
Evento -> Entidad del sistema
Clase relacionada -> CD83 [Entity]
Modelo Relacional -> MR04
'''
class Evento(models.Model):
    nombre = models.CharField(max_length=80)
    ubicacion = models.CharField(max_length=60)
    fecha_inicio = models.DateField(default=one_day_hence)
    fecha_fin = models.DateField(default=one_day_hence)

    def __str__(self):
        return f"Evento {self.nombre} con lugar en {self.ubicacion}."


'''
Modelo Relacional -> MR23
'''
class TipoActividad(models.Model):
    nombre_tipo = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Tipo de actividad"
        verbose_name_plural = "Tipos de actividades"

    def __str__(self):
        return f"{self.nombre_tipo}"

'''
Código: CFG06
Ponente -> Entidad del sistema
Clase relacionada -> CD73 [Entity]
Modelo Relacional -> MR09
'''
class Ponente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    especialidad = models.CharField(max_length=30)

    class Meta:
        ordering = ['apellido']

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

'''
Código: CFG07
Material -> Entidad del sistema 
Clase relacionada -> CD37 [Entity]
Modelo Relacional -> MR21
'''
class Material(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(null=True, blank=True, max_length=100)

    class Meta:
        verbose_name_plural = "Materiales"

    def __str__(self):
        return f"{self.nombre}"

'''
Código: AST04
Catalogo -> Entidad del sistema 
Clase relacionada -> CD54 [Entity]
Modelo Relacional -> MR19
'''
class Catalogo(models.Model):
    descripcion = models.CharField(max_length=50)
    materiales = models.ManyToManyField(Material, through='Item')

    def __str__(self):
        return f"{self.descripcion}"


'''
Modelo Relacional -> MR20
'''
class Item(models.Model):
    catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)


'''
Código: {AST04, AST02, CFG05, CFG02}
Actividad -> Entidad del sistema
Clase relacionada -> CD01 [Entity]
Modelo Relacional -> MR05
'''
class Actividad(models.Model):
    nombre = models.CharField(max_length=80)
    evento = models.ForeignKey(Evento,  on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoActividad, on_delete=models.CASCADE)
    catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE, null=True, blank=True)
    ctlgos_restantes = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Actividades"

    def __str__(self):
        return f"{self.tipo}: {self.nombre}."


'''
Código: CFG06
Turno -> Entidad del sistema
Clase relacionada -> CD44 [Entity]
Modelo Relacional -> MR06
'''
class Turno(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=15)
    hora_inicio = models.TimeField(default=timezone.now)
    hora_fin = models.TimeField(default=timezone.now)
    ponentes = models.ManyToManyField(Ponente)

    def __str__(self):
        return f"{self.nombre}"


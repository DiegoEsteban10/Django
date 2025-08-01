from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    cupos = models.IntegerField()
    precio = models.DecimalField(max_digits=11, decimal_places=2)
    fecha_inicio = models.DateField()
    
    def __str__(self):
        return self.nombre

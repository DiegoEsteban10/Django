from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=80)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre} - Precio: {self.precio:2f,}"
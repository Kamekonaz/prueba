from django.db import models

# Create your models here.
class Venta(models.Model):
    nombre = models.CharField(max_length = 30)
    correo = models.CharField(max_length = 30)
    telefono = models.IntegerField()
    cantidad = models.CharField(max_length = 30)
    direccion = models.CharField(max_length = 30)
    tipo = models.CharField(max_length = 30)
    comentario = models.CharField(max_length = 30)

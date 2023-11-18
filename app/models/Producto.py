from django.db import models

from app.models.Suministrador import Suministrador


class Producto (models.Model):
    id = models.AutoField(primary_key = True)
    id_suministador = models.ForeignKey(Suministrador, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50)
    fecha_produccion = models.DateField()


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
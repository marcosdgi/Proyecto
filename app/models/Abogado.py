from django.db import models
from base.models.Trabajadores import BaseTrabajador


class Abogado(BaseTrabajador):
    direccion = models.CharField(max_length=50)
    division = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Abogado'
        verbose_name_plural = 'Abogados'


    def __str__(self):
        return '%s'%(self.nombre)
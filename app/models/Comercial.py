from django.db import models

from app.models.DepartamentoComercial import DepartamentoComercial
from base.models.Trabajadores import BaseTrabajador

class Comercial(BaseTrabajador):
    cantidad_contratos = models.IntegerField()


    class Meta:
        verbose_name = 'Comercial'
        verbose_name_plural = 'Comerciales'

    def __str__(self):
        return '%s'%(self.nombre)
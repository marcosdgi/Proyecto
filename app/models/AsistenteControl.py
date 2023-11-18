from django.db import models
from base.models.Trabajadores import BaseTrabajador
from app.models.DepartamentoComercial import DepartamentoComercial
class AsistenteControl(BaseTrabajador):
    grado_academico = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Asistente de Control'
        verbose_name_plural = 'Asistentes de Control'

    def __str__(self):
        return '%s'%(self.nombre)
from django.db import models
from base.models.BaseDepartamento import BaseDepartamento


class DepartamentoLegal(BaseDepartamento):
    ano = models.CharField(max_length=5)
    class Meta:
        verbose_name = 'Departamento Legal'
        verbose_name_plural = 'Departamentos Legales'

    def __str__(self):
        return '%s'%(self.nombre)
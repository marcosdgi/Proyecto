from django.db import models
from base.models.BaseDepartamento import BaseDepartamento
from app.models.DepartamentoLegal import DepartamentoLegal
class DepartamentoComercial(BaseDepartamento):
    codigo = models.CharField(max_length=6, unique=True)
    fecha_comunicacion = models.DateTimeField(default='')
    id_DepartamentoLegal = models.ForeignKey(DepartamentoLegal, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Departamento Comercial'
        verbose_name_plural = 'Departamentos Comerciales'

    def __str__(self):
        return '%s'%(self.nombre)
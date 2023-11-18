from django.db import models
from base.models.Trabajadores import BaseTrabajador
from app.models.DepartamentoLegal import DepartamentoLegal
class Contrato(models.Model):
    id_contrato = models.AutoField(primary_key = True)
    id_trabajador = models.OneToOneField(BaseTrabajador, on_delete=models.CASCADE)
    id_departamentolegal = models.ForeignKey(DepartamentoLegal, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)


    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'


    def __str__(self):
        return '%s'%(self.descripcion)
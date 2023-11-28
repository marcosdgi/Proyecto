from django.db import models
from app.models.Contrato import Contrato


class Informe(models.Model):

    id_contrato = models.OneToOneField(Contrato, on_delete=models.CASCADE)
    codigo = models.IntegerField(unique=True)
    modificaciones = models.CharField(max_length=50, default='', null=False)


    class Meta:
        verbose_name = 'Informe'
        verbose_name_plural = 'Informes'

    def __str__(self):
        return'%s'%(self.codigo)
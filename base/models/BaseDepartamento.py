from django.db import models


class BaseDepartamento(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField(max_length=200, default='')
    nombre = models.CharField(max_length=50, null=False)
    direccion = models.CharField(max_length=100, null=False)


    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return 'Dpt. %s'%(self.nombre)
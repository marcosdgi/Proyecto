from django.db import models


class Suministrador(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=50)
    nombre_calle = models.CharField(max_length=50)
    numero_calle = models.IntegerField()
    municipio = models.CharField(max_length=60)
    provincia = models.CharField(max_length=60)
    clasificacion = models.CharField(max_length=50)


    class Meta:
        verbose_name = 'Suministrador'
        verbose_name_plural = 'Suministradores'

    def __str__(self):
        return '%s'%(self.nombre)
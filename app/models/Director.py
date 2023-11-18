from django.db import models

from base.models.Trabajadores import BaseTrabajador


class Director(BaseTrabajador):
    grado_adademico = models.CharField(max_length=50)


    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directores'

    def __str__(self):
        return '%s'%(self.nombre)
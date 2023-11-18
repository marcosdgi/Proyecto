from django.db import models

from app.models.Director import Director


class Evaluacion(models.Model):
    id = models.AutoField(primary_key = True)
    id_director = models.ForeignKey(Director, on_delete=models.CASCADE)
    valor = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Evaluacion'
        verbose_name_plural = 'Evaluaciones'


    def __str__(self):
        return '%s, %s, %s'%(self.id, self.id_director, self.valor)
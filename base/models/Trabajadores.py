from django.db import models
from base.models.BaseDepartamento import BaseDepartamento

class BaseTrabajador(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=50, null=False)
    primer_apellido = models.CharField(max_length=50, null=False)
    segundo_apellido = models.CharField(max_length=50, null=False)
    fecha_nacimiento = models.DateTimeField(default='', null=True)
    edad = models.IntegerField()
    annos_experiencia = models.IntegerField()
    ocupacion = models.CharField(max_length=50, default='trabajador')
    id_departamento = models.ForeignKey(BaseDepartamento, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'

    def __str__(self):
        return('%s %s %s %s %s %s %s %s %s')%(self.id, self.nombre, self.primer_apellido,
                                              self.segundo_apellido, self.fecha_nacimiento
                                              ,self.edad, self.annos_experiencia,
                                              self.ocupacion, self.id_departamento)
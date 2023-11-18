from django.db import models
from base.models.BaseDepartamento import BaseDepartamento
from app.models.DepartamentoLegal import DepartamentoLegal

class Division(DepartamentoLegal):
    clasificacion = models.CharField(max_length=5)


    class Meta:
        verbose_name = 'Division'
        verbose_name_plural = 'Divisiones'
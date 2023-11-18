from django.db import models

from app.models.Comercial import Comercial
from app.models.Suministrador import Suministrador


class Venta(models.Model):
    id_suministrador = models.OneToOneField(Suministrador, on_delete=models.CASCADE)
    id_comercial = models.OneToOneField(Comercial, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
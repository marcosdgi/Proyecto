from django.contrib import admin
from base.models.Trabajadores import BaseTrabajador
from base.models.BaseDepartamento import BaseDepartamento
# Register your models here.
admin.site.register(BaseTrabajador)
admin.site.register(BaseDepartamento)
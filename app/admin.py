from django.contrib import admin

from app.models import Comercial_Suministrador
from app.models.Abogado import Abogado
from app.models.AsistenteControl import AsistenteControl
from app.models.Comercial import Comercial
from app.models.Comercial_Suministrador import Venta
from app.models.Contrato import Contrato
from app.models.DepartamentoComercial import DepartamentoComercial
from app.models.DepartamentoLegal import DepartamentoLegal
from app.models.Director import Director
from app.models.Division import Division
from app.models.Evaluacion import Evaluacion
from app.models.Producto import Producto
from app.models.Suministrador import Suministrador
from django.contrib import  admin
from app.models.Informe import Informe
# Register your models here.

class GestorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Abogado)
admin.site.register(Suministrador)
admin.site.register(AsistenteControl)
admin.site.register(DepartamentoLegal)
admin.site.register(Venta)
admin.site.register(Comercial)
admin.site.register(Contrato)
admin.site.register(DepartamentoComercial)
admin.site.register(Division)
admin.site.register(Director)
admin.site.register(Evaluacion)
admin.site.register(Producto)
admin.site.register(Informe)

admin.site.site_header = "Panel de Administracion de la Empresa de Materias Primas"
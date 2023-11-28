from django.urls import path

from app.views.TrabajadorView import buscar_trabajador
from app.views.DirectorView import  buscar_director
from app.views.ComercialView  import buscar_comercial
from app.views.AsistenteControlView  import buscar_asistente
from app.views.AbogadoView  import buscar_abogado
from app.views.Inicio import inicio
from app.views.ContratoView import buscar_contrato
from app.views.DivisionesView import buscar_division
from app.views.DepartamentoView import buscar_departamento
from app.views.ProductoView import buscar_producto
from app.views.DepartamentoLegalView import  buscar_departamentolegal
from app.views.DepartamentoComercialVIew import  buscar_departamentocomercial
from app.views.SuministradorView import buscar_suministrador


from app.views.InformeView import buscar_informe

urlpatterns = [
    path('trabajador/', buscar_trabajador, name='trabajador'),
    #Director
    path('director/', buscar_director, name='director'),
    #comerciales
    path('comercial/', buscar_comercial, name='comercial'),
    #Asistente de Control
    path('asistente/',buscar_asistente, name='asistente'),
    #abogado
    path('abogado/', buscar_abogado, name='abogado'),
    #Contratos
    path('contrato/',buscar_contrato, name='contrato'),

    #Divisiones
    path('division/',buscar_division, name='division'),

    #Departamento
    path('departamento/', buscar_departamento, name='departamento'),

    #Producto
    path('producto/',buscar_producto, name='producto'),
    #Departamento Legal
    path('departamentolegal/', buscar_departamentolegal, name='departamentolegal'),
    #Departamento Comercial
    path('departamentocomercial/', buscar_departamentocomercial, name='departamentocomercial'),

    #Suministrador
    path('suministrador/', buscar_suministrador, name='suministrador'),
    #Informe
    path('informe/',buscar_informe, name = 'informe'),
              ]+[
    #rutas de la pagina
    path('',inicio, name = 'inicio' ),
]

from django.urls import path

from app.views.TrabajadorView import trabajador_list,trabajador_detail, trabajador_edit, trabajador_new, trabajador_delete
from app.views.DirectorView import director_list,director_new,director_edit,director_detail,director_delete
from app.views.ComercialView  import comercial_list,comercial_new,comercial_delete,comercial_detail,comercial_edit
from app.views.AsistenteControlView  import asistente_delete, asistente_detail, asistente_new,asistente_edit,asistente_list
from app.views.AbogadoView  import abogado_delete,abogado_new,abogado_edit,abogado_list,abogado_detail
from app.views.Inicio import inicio
from app.views.ContratoView import contrato_list,contrato_edit,contrato_new,contrato_delete,contrato_detail
from app.views.DivisionesView import division_list,division_new,division_edit,division_delete,division_detail
from app.views.DepartamentoView import departamento_edit,departamento_list,departamento_new,departamento_delete,departamento_detail
from app.views.ProductoView import producto_new,producto_edit,producto_list,producto_delete,producto_detail
from app.views.DepartamentoLegalView import departamentolegal_list,departamentolegal_new,departamentolegal_edit,departamentolegal_delete,departamentolegal_detail
from app.views.DepartamentoComercialVIew import departamentocomercial_delete, departamentocomercial_edit,departamentocomercial_list,departamentocomercial_new,departamentocomercial_detail
from app.views.SuministradorView import suministrador_delete,suministrador_new,suministrador_edit,suministrador_list

urlpatterns = [
    path('trabajador/', trabajador_list, name='trabajador'),
    path('trabajador/<int:pk>/', trabajador_detail, name='trabajador_detalle'),
    path('trabajador/nuevo/', trabajador_new, name='trabajador_nuevo'),
    path('trabajador/<int:pk>/editar/',trabajador_edit, name='trabajador_editar'),
    path('trabajador/<int:pk>/borrar/', trabajador_delete, name='trabajador_borrar'),
    #Director
    path('director/', director_list, name='director'),
    path('director/<int:pk>/', director_detail, name='director_detalle'),
    path('director/nuevo/', director_new, name='director_nuevo'),
    path('director/<int:pk>/editar/', director_edit, name='director_editar'),
    path('director/<int:pk>/borrar/', director_delete, name='director_borrar'),
    #comerciales
    path('comercial/', comercial_list, name='comercial'),
    path('comercial/<int:pk>/', comercial_detail, name='comercial_detalle'),
    path('comercial/nuevo/', comercial_new, name='comercial_nuevo'),
    path('comercial/<int:pk>/editar/', comercial_edit, name='comercial_editar'),
    path('comercial/<int:pk>/borrar/', comercial_delete, name='comercial_borrar'),
    #Asistente de Control
    path('asistente/',asistente_list, name='asistente'),
    path('asistente/<int:pk>/',asistente_detail, name = 'asistente_detalle'),
    path('asistente/nuevo/',asistente_new, name = 'asistente_nuevo'),
    path('asistente/<int:pk>/editar/',asistente_edit, name='asistente_editar'),
    path('asistente/<int:pk>/borrar/',asistente_delete, name='asistente_borrar'),
    #abogado
    path('abogado/', abogado_list, name='abogado'),
    path('abogado/<int:pk>/', abogado_detail, name='abogado_detalle'),
    path('abogado/nuevo/', abogado_new, name='abogado_nuevo'),
    path('abogado/<int:pk>/editar/', abogado_edit, name='abogado_editar'),
    path('abogado/<int:pk>/borrar/', abogado_delete, name='abogado_borrar'),
    #Contratos
    path('contrato/',contrato_list, name='contrato'),
    path('contrato/<int:pk>/',contrato_detail, name='contrato_detalle'),
    path('contrato/nuevo/',contrato_new, name='contrato_nuevo'),
    path('contrato/<int:pk>/editar/',contrato_edit, name='contrato_editar'),
    path('contrato/<int:pk>/borrar/',contrato_delete, name='contrato_borrar'),

    #Divisiones
    path('division/',division_list, name='division'),
    path('division/<int:pk>/',division_detail, name='division_detalle'),
    path('division/nuevo/',division_new, name='division_nuevo'),
    path('division/<int:pk>/editar/',division_edit, name='division_editar'),
    path('division/<int:pk>/borrar/',division_delete, name='division_borrar'),

    #Departamento
    path('departamento/', departamento_list, name='departamento'),
    path('departamento/<int:pk>/', departamento_detail, name='departamento_detalle'),
    path('departamento/nuevo/', departamento_new, name='departamento_nuevo'),
    path('departamento/<int:pk>/editar/', departamento_edit, name='departamento_editar'),
    path('departamento/<int:pk>/borrar/', departamento_delete, name='departamento_borrar'),

    #Producto
    path('producto/',producto_list, name='producto'),
    path('producto/nuevo/',producto_new, name='producto_nuevo'),
    path('producto/<int:pk>/editar/',producto_edit, name='producto_editar'),
    path('producto/<int:pk>/borrar/',producto_delete, name='producto_borrar'),
    #Departamento Legal
    path('departamentolegal/', departamentolegal_list, name='departamentolegal'),
    path('departamentolegal/nuevo/', departamentolegal_new, name='departamentolegal_nuevo'),
    path('departamentolegal/<int:pk>/editar/', departamentolegal_edit, name='departamentolegal_editar'),
    path('departamentolegal/<int:pk>/borrar/', departamentolegal_delete, name='departamentolegal_borrar'),
    #Departamento Comercial
    path('departamentocomercial/', departamentocomercial_list, name='departamentocomercial'),
    path('departamentocomercial/nuevo/', departamentocomercial_new, name='departamentocomercial_nuevo'),
    path('departamentocomercial/<int:pk>/editar/', departamentocomercial_edit, name='departamentocomercial_editar'),
    path('departamentocomercial/<int:pk>/borrar/', departamentocomercial_delete, name='departamentocomercial_borrar'),

    #Suministrador
    path('suministrador/', suministrador_list, name='suministrador'),
    path('suministrador/nuevo/', suministrador_new, name='suministrador_nuevo'),
    path('suministrador/<int:pk>/editar/', suministrador_edit,name='suministrador_editar'),
    path('suministrador/<int:pk>/borrar/', suministrador_delete,name='suministrador_borrar')

              ]+[
    #rutas de la pagina
    path('',inicio, name = 'inicio' )
]

from django.urls import  path

from autenticacion.views.IniciarSesion import inicio_sesion, CustomLoginView
from autenticacion.views.RegistrarUsuario import registro

urlpatterns = [
    path('registro/',registro, name = 'registro'),
    path('login/', CustomLoginView.as_view(), name='inicio_sesion'),

]
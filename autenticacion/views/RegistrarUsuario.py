from django.shortcuts import render

from autenticacion.Forms.UserForm import Usuario


def registro(request):
    if request.method == 'POST':
        FormularioRegistro = Usuario(request.POST)
        if FormularioRegistro.is_valid():
            FormularioRegistro.save()
            return render(request, 'UsuarioCreado.html')

    else:
        FormularioRegistro = Usuario()

    return render(request, 'Registro.html', {'FormularioRegistro': FormularioRegistro})

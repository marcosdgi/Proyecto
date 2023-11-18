from django.shortcuts import render, get_object_or_404, redirect

from base.models.Trabajadores import BaseTrabajador
from app.Forms.TrabajadorForm import TrabajadorForm



def trabajador_list(request):
    trabajadores = BaseTrabajador.objects.all()
    return render(request, 'Trabajador.html',
                  {'trabajadores': trabajadores})

def trabajador_detail(request, pk):
    trabajador = get_object_or_404(BaseTrabajador, pk=pk)
    return render(request, 'Trabajador.html',
                  {'trabajador': trabajador})

def trabajador_new(request):
    if request.method == "POST":
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            trabajador = form.save()
            return redirect('Trabajador.html', pk=trabajador.pk)
    else:
        form = TrabajadorForm()
    return render(request, 'Trabajador.html',
                  {'form': form})

def trabajador_edit(request, pk):
    trabajador = get_object_or_404(BaseTrabajador, pk=pk)
    if request.method == "POST":
        form = TrabajadorForm(request.POST, instance=trabajador)
        if form.is_valid():
            trabajador = form.save()
            return redirect('trabajador_detail', pk=trabajador.pk)
    else:
        form = TrabajadorForm(instance=trabajador)
    return render(request, 'Trabajador.html',
                  {'form': form})

def trabajador_delete(request, pk):
    trabajador = get_object_or_404(BaseTrabajador, pk=pk)
    if request.method == 'POST':
        trabajador.delete()
        return redirect('trabajadores')
    return render(request, 'Trabajador.html',
                  {'object': trabajador})

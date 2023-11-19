from django.shortcuts import render, get_object_or_404, redirect

from app.models.Suministrador import Suministrador
from app.Forms.SuministradorForm import SuministradorForm



def suministrador_list(request):
    suministradores = Suministrador.objects.all()
    return render(request, 'Suministrador.html',
                  {'suministradores': suministradores})

def suministrador_detail(request, pk):
    suministrador = get_object_or_404(Suministrador, pk=pk)
    return render(request, 'Suministrador.html',
                  {'suministrador': suministrador})

def suministrador_new(request):
    if request.method == "POST":
        form = SuministradorForm(request.POST)
        if form.is_valid():
            suministrador = form.save()
            return redirect('Index.html', pk=suministrador.pk)
    else:
        form = SuministradorForm()
    return render(request, 'Suministrador.html',
                  {'form': form})

def suministrador_edit(request, pk):
    suministrador = get_object_or_404(Suministrador, pk=pk)
    if request.method == "POST":
        form = SuministradorForm(request.POST, instance=suministrador)
        if form.is_valid():
            suministrador = form.save()
            return redirect('suministrador_detail', pk=suministrador.pk)
    else:
        form = SuministradorForm(instance=suministrador)
    return render(request, 'Suministrador.html',
                  {'form': form})

def suministrador_delete(request, pk):
    suministrador = get_object_or_404(Suministrador, pk=pk)
    if request.method == 'POST':
        suministrador.delete()
        return redirect('suministradores')
    return render(request, 'Suministrador.html',
                  {'object': suministrador})

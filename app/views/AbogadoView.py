from django.shortcuts import render, get_object_or_404, redirect

from app.models.Abogado import Abogado
from app.Forms.AbogadoForm import AbogadoForm



def abogado_list(request):
    abogados = Abogado.objects.all()
    return render(request, 'Abogado.html',
                  {'abogadoes': abogados})

def abogado_detail(request, pk):
    abogado = get_object_or_404(Abogado, pk=pk)
    return render(request, 'Abogado.html',
                  {'abogado': abogado})

def abogado_new(request):
    if request.method == "POST":
        form = AbogadoForm(request.POST)
        if form.is_valid():
            abogado = form.save()
            return redirect('Abogado.html'
                            , pk=abogado.pk)
    else:
        form = AbogadoForm()
    return render(request, 'Abogado.html',
                  {'form': form})

def abogado_edit(request, pk):
    abogado = get_object_or_404(Abogado, pk=pk)
    if request.method == "POST":
        form = AbogadoForm(request.POST, instance=abogado)
        if form.is_valid():
            abogado = form.save()
            return redirect('abogado_detail', pk=abogado.pk)
    else:
        form = AbogadoForm(instance=abogado)
    return render(request, 'Abogado.html',
                  {'form': form})

def abogado_delete(request, pk):
    abogado = get_object_or_404(Abogado, pk=pk)
    if request.method == 'POST':
        abogado.delete()
        return redirect('abogado')
    return render(request, 'Abogado.html',
                  {'object': abogado})
